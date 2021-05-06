from channels.generic.websocket import AsyncWebsocketConsumer
import json
from datetime import datetime
from . import api

from asgiref.sync import async_to_sync

class chat(AsyncWebsocketConsumer):
	async def connect(self):
		await self.accept()
		self.room_name = self.scope['url_route']['kwargs']['room_name']
		self.username = self.scope['url_route']['kwargs']['username']

		await self.channel_layer.group_add(self.room_name , self.channel_name)

	async def receive(self,text_data):
		packaged_data = json.loads(text_data)
		text = packaged_data['message']

		date_time = datetime.now()
		time = date_time.strftime('%H:%M')
		packaged_data['time'] = time
		packaged_data['username']=self.username

		try:
			if text[0] == '!':
				info = api.video_info(text[1:])
				packaged_data['id']=info[0]
				packaged_data['download_link'] = info[1]
		except:
			packaged_data['message'] = "Sorry we couldn't process your request. Please Try again."
			
		await self.channel_layer.group_send(self.room_name,{'type':'received.data','packaged_data':packaged_data})
		

	async def disconnect(self,close_code):
		await self.channel_layer.group_discard(self.room_name,self.channel_name)


	async def received_data(self,event):
		await self.send(json.dumps(event['packaged_data']))