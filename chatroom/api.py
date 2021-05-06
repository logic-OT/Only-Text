import requests
import json


def video_info(search):
    url = "https://youtube-advanced-search.p.rapidapi.com/video/" + search

    headers = { 
        'x-rapidapi-key': "899d0d92d0msha9a3a6265b48229p1bbad9jsn752a67105fba",
        'x-rapidapi-host': "youtube-advanced-search.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    parsed_search = json.loads(response.text)
    #print(parsed['Data'])
    video_data = parsed_search['Data'][1]
    id = video_data['video_id']
    print (id)

    url = "https://youtube-to-mp32.p.rapidapi.com/yt_to_mp3"

    querystring = {"video_id":id}

    headers = {
        'x-rapidapi-key': "899d0d92d0msha9a3a6265b48229p1bbad9jsn752a67105fba",
        'x-rapidapi-host': "youtube-to-mp32.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.text
    parsed_link = json.loads(data)
    print(parsed_link)
    download_link = parsed_link['Download_url']

    return id,download_link

