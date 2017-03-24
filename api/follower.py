#!C:\Python27\python.exe
from datetime import datetime, timedelta

import requests

from config import BASE_URL, API_VERSION_HEADER
from .. import settings


HEADERS = {
    'Accept': API_VERSION_HEADER,
}


def get_followers():
    response = requests.get(BASE_URL + '/channels/' + settings.CHANNEL + '/follows?client_id=' + settings.TWITCH_CLIENT_ID,
                                       headers=HEADERS).json()
    followers = response['follows']

    recent_followers = []
    now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    today = datetime.strptime(now, '%Y-%m-%dT%H:%M:%SZ')
    five_minutes_ago = today - timedelta(minutes=5)
    for follower in followers:
        follow_time = datetime.strptime(follower['created_at'], '%Y-%m-%dT%H:%M:%SZ')
        if follow_time < five_minutes_ago:
            recent_followers.append(follower['user']['display_name'])
    recent_followers[-1] = ' and %s' % recent_followers[-1]
    return recent_followers