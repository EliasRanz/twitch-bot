#!C:\Python27\python.exe
import requests
from datetime import datetime

from twitchbot.api.config import BASE_URL, API_VERSION_HEADER
from twitchbot.settings import CHANNEL, TWITCH_CLIENT_ID

HEADERS = {
    'Accept': API_VERSION_HEADER,
    'Client-ID': TWITCH_CLIENT_ID,
}


def stream_uptime():
    # response = requests.get(BASE_URL + '/streams/' + CHANNEL + 'client').json()
    response = requests.get(BASE_URL + '/streams/' + CHANNEL, headers=HEADERS).json()
    if response['stream'] is not None:
        start_time = datetime.strptime(response['stream']['created_at'], '%Y-%m-%dT%H:%M:%SZ')
        now = datetime.utcnow()
        uptime = now - start_time
        hours = uptime.seconds / 3600
        minutes = (uptime.seconds - hours * 3600) / 60
        if hours is not 0:
            return "The stream has been online for %s hours and %s minutes." % (hours, minutes)
        else:
            return "The stream has been online for %s minutes." % minutes
    else:
        return "Stream is currently offline."