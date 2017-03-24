#!C:\Python27\python.exe
import requests

from twitchbot.api.config import BASE_URL
from twitchbot import settings


def stream_uptime():
    response = requests.get(BASE_URL + '/streams/' + settings.CHANNEL + 'client').json()
    print response
    # return uptime

