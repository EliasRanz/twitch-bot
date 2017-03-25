#!C:\Python27\python.exe
from datetime import datetime
import time as t
import requests

from twitchbot.api.config import BASE_URL, HEADERS
from twitchbot.settings import CHANNEL


def recent_followers():
    response = requests.get(BASE_URL + '/channels/' + CHANNEL + '/follows?limit=100&order=DESC',
                                       headers=HEADERS).json()
    recent_followers_list = []
    followers = response['follows']
    for follower in followers:
        follow_time = datetime.strptime(follower['created_at'], '%Y-%m-%dT%H:%M:%SZ')
        time_elapsed = t.mktime(follow_time.timetuple())
        if time_elapsed >= 300:
            recent_followers_list.append(follower['user']['display_name'])
    return recent_followers_list
recent_followers()