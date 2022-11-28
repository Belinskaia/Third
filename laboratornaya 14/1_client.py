# multiconn-client.py

import sys
import socket
import selectors
from time import sleep
import types
import random

sel = selectors.DefaultSelector()
messages = [b"Message 1 from client.", b"Message 2 from client."]


def start_connections(host, port, num_conns):
    server_addr = (host, port)
    for i in range(0, num_conns):
        connid = i + 1
        print(f"Starting connection {connid} to {server_addr}")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(server_addr)
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        data = types.SimpleNamespace(
            connid=connid,
            recv_total=0,
            messages=messages.copy(),
            outb=b"",
            name = i+2
        )
        sel.register(sock, events, data=data)

def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data == "Salute! Enter your name":
            sent = sock.send(data.name)  # Should be ready to write
            data.outb = data.outb[sent:]
        if not recv_data:
            print(f"Closing connection {data.connid}")
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        m = random.randint(1, 2)
        if m == 1:
            sent = sock.send(b'1')
            data.outb = data.outb[sent:]
        if m == 2:
            sent = sock.send(bytes(f'2 {random.randint()}'))  # Should be ready to write
            data.outb = data.outb[sent:]


host, port = '127.0.0.1', 4444
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.sendall(b"1")
    data = s.recv(1024).decode('ascii')
    print(f"Received {data}")
    sleep(1)
    s.sendall(b"Hello, world")
    data = s.recv(1024)
    print(f"Received {data}")
