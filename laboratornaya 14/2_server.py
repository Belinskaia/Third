# multiconn-server.py

import sys
import socket
import selectors
from time import time
import types

sel = selectors.DefaultSelector()

host, port = '127.0.0.1', 9999
clients = {}
unauthorized = []
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen()
print(f"Listening on {(host, port)}")
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)

def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print(f"Accepted connection from {addr}")
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"Enter your user-name")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)
    unauthorized.append(data)


def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            data.outb += recv_data.decode('ascii')
            if data in unauthorized:
                clients[str(recv_data)] = data
                unauthorized.remove(data)
                print(f'recieved name {str(recv_data)}')
                data.outb += b'Write (1) to see who is online. Write (2) {name} {message} to write a message'
            elif recv_data == '(1)':
                data.outb += (', '.join(list(clients.keys()))).encode('ascii')
            else:
                recv_data = recv_data.split()
                clients[recv_data[0][1:]].outb += (' '.join(recv_data[1:])).encode('ascii')
        else:
            print(f"Closing connection to {data.addr}")
            for i in clients:
                if clients[i].addr == data.addr:
                    clients.pop(i)
                    break
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            sent = sock.send(data.outb)  # Should be ready to write
            data.outb = data.outb[sent:]
        else:
            if int(time()) % 10 == 0:
                print(f"Echoing SPAM to {data.addr}")
                sent = sock.send(b'SPAM')  # Should be ready to write
try:
    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                service_connection(key, mask)
except KeyboardInterrupt:
    print("Caught keyboard interrupt, exiting")
finally:
    sel.close()
