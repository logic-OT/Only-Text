from django.forms import ModelForm
from .models import*

class Create_roomname_form(ModelForm):
	class Meta:
		model = Room_name
		fields = '__all__'