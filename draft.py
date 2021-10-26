import telebot


token = '2036573848:AAGC5yieyHy-nS0zW1_jyvGZ_w1UjlA7h-A'
chat_id = 495432329


import requests

api_token = 'MY_TOKEN'

requests.get(f'https://api.telegram.org/bot{token}/sendMessage', params=dict(chat_id=chat_id, text='Hello world!'))