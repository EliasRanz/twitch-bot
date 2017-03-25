#!C:\Python27\python.exe
import string
import random

from threading import Timer

from twitchbot.read import get_user, get_message
from twitchbot.connection import open_socket, send_message
from twitchbot.initialize import join_room
from twitchbot.api.follower import recent_followers
from twitchbot.api.uptime import stream_uptime


def get_recent_followers():
    followers = recent_followers()
    if len(followers) > 0:
        s = open_socket()
        send_message(s, 'Thanks for the follow: '+','.join(followers) + '!')
    Timer(300, get_recent_followers).start()


def init():
    s = open_socket()
    join_room(s)
    read_buffer = ""
    # Run get_recent_followers every 5 minutes
    # cron(600.0, get_recent_followers)
    # get_recent_followers()

    while True:
        read_buffer = read_buffer + s.recv(1024)
        temp = string.split(read_buffer, "\n")
        read_buffer = temp.pop()

        for line in temp:
            print(line)
            if "PING" in line:
                s.send(line.replace("PING", "PONG"))
                break
            user = get_user(line)
            message = get_message(line)
            print(user + " typed :" + message)
            if "you suck" in message.lower():
                send_message(s, "No, you suck!")
                break

            if "!roulette" in message:
                spin = random.randint(1, 10)
                print spin
                if spin == 3:
                    send_message(s, "@" + user + " You got lucky this time unfortunately. "
                                                 "I was getting excited for a minute.")
                else:
                    send_message(s, "/timeout " + user + " 1")
                    send_message(s, "@" + user + " You lost better luck next time!")

            if "!uptime" in message:
                send_message(s, stream_uptime())


init()
