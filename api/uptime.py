#!C:\Python27\python.exe
import requests

from config import BASE_URL
from .. import settings


def stream_uptime():
    response = requests.get(BASE_URL + '/streams/' + settings.CHANNEL + 'client').json()
    print response
    # return uptime

stream_uptime()