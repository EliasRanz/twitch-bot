#!C:\Python27\python.exe
import string
from twitchbot.socket import send_message


def join_room(s):
    read_buffer = ""
    loading = True
    while loading:
        read_buffer = read_buffer + s.recv(1024)
        temp = string.split(read_buffer, "\n")
        read_buffer = temp.pop()

        for line in temp:
            print(line)
            loading = loading_complete(line)
    # send_message(s, "Hello everyone.")


def loading_complete(line):
    if "End of /NAMES list" in line:
        return False
    else:
        return True
