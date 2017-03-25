#!C:\Python27\python.exe
from twitchbot.settings import TWITCH_CLIENT_ID
API_VERSION_HEADER = 'application/vnd.twitchtv.v3+json'
BASE_URL = 'https://api.twitch.tv/kraken'

HEADERS = {
    'Accept': API_VERSION_HEADER,
    'Client-ID': TWITCH_CLIENT_ID,
}