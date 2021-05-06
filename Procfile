web: daphne -p 8001 Chat_project.asgi:application --port $PORT bind 0.0.0.0 -v2
chatworker: python manage.py runworker --settings=Chat.settings -v2
