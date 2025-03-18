import socket
import struct
import matplotlib as plt
import os

HOST = os.environ['STM32_SERVER_HOST']
PORT = int(os.environ['STM32_SERVER_PORT'])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((HOST, PORT))
sock.listen(1)
print(f"Server listned on {HOST}:{PORT}")

while True:
    (client_sock, address) = sock.accept()
    print(f"{address} connected.")

    while True:
        try:
            data = client_sock.recv(6)
            values = struct.unpack('<hhh', data)
            if data:
                print(values)
        except:
            client_sock.close()
            print("closed server")
            break

    sock.close()
    break
