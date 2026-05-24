import socket
import threading
import json
import sys
import os

sys.path.append(os.path.abspath("../"))

from shared_key import cipher

HOST = "127.0.0.1"
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen()

print(f"Server listening on {PORT}")

def handle_client(client, address):
    print(f"Connected: {address}")

    while True:
        try:
            encrypted_data = client.recv(4096)

            if not encrypted_data:
                break

            decrypted_data = cipher.decrypt(encrypted_data)

            packet = json.loads(
                decrypted_data.decode()
            )

            print(
                f"[{packet['client']}] -> {packet['message']}"
            )

        except Exception as error:
            print(f"Error: {error}")
            break

    client.close()

while True:
    client, address = server.accept()

    thread = threading.Thread(
        target=handle_client,
        args=(client, address)
    )

    thread.start()