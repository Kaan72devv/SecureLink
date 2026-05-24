import socket
import json
import sys
import os

sys.path.append(os.path.abspath("../"))

from shared_key import cipher

HOST = "127.0.0.1"
PORT = 5555

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client.connect((HOST, PORT))

name = input("Name: ")

while True:
    message = input("Message: ")

    packet = {
        "client": name,
        "message": message
    }

    json_packet = json.dumps(packet)

    encrypted_packet = cipher.encrypt(
        json_packet.encode()
    )

    client.send(encrypted_packet)