import socket
import struct
import matplotlib.pyplot as plt
import os

# setup GUI
plt.ion()
fig, ax = plt.subplots(figsize=(6, 4))
labels = ['X', 'Y', 'Z']
bars = ax.bar(labels, [0, 0, 0], color=['r', 'g', 'b'])
ax.set_ylim(-1500, 1500)
ax.set_title('STM32 3D Accelerator Data')
ax.set_xlabel('Axis')
ax.set_ylabel('Value')
ax.grid(axis='y', linestyle='--', alpha=0.7)


# setup socket
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
            print(values)

            for bar, value in zip(bars, values):
                bar.set_height(value)

            for text in ax.texts:
                text.remove()

            for i, v in enumerate(values):
                ax.text(i, v+5, str(v), ha='center', fontsize=12, color='black', weight='bold')

            plt.draw()
            plt.pause(0.001)

        except:
            client_sock.close()
            print("closed server")
            break

    sock.close()
    break
