#!C:\Python27\python.exe
import socket
from settings import HOST, PORT, PASSWORD, BOT_USERNAME, CHANNEL


def open_socket():
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send("PASS " + PASSWORD + "\r\n")
    s.send("NICK " + BOT_USERNAME + "\r\n")
    s.send("JOIN #" + CHANNEL + "\r\n")
    return s


def send_message(s, message):
    message_temp = "PRIVMSG #" + CHANNEL + " :" + message
    s.send(message_temp + "\r\n")
    print("Sent: " + message_temp)