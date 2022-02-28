# Only-Text Group Chat + Youtube audio download
This project uses django channels to run a group chatroom service. Simply join an existing room or create one to begin texting. To download a Youtube video's audio, begin a text with '!' and type in the name of the video you want to download. This is very effective for music downloading. This project also has a voice note feature which makes the name _Only text_ quite misleading 

A live demo can be seen here [Only-text](https://only-text.herokuapp.com,'')
![Screenshot (7)](https://user-images.githubusercontent.com/61668807/155993538-43e2a667-fc63-45a6-8934-ba2fe8ec2f4c.png)

## Features
* Realtime chat fuctionality with django channels
* Voice note recording
* Youtube search and download api

## Setup and and requirements
* Clone project: git clone https://github.com/logic-OT/countries
* Create virtual environment: virtualenv myenv
* myenv\scripts\activate
* pip install -r requirements.txt
* python manage.py runserver
* Internet connection needed for youtube api to work
