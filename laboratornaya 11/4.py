import urllib.request
import time
from threading import Thread


urls = [
    'https://www.yandex.ru', 'https://www.google.com',
    'https://habrahabr.ru', 'https://www.python.org',
    'https://isocpp.org',
]
start = time.time()

def read_url(i):
    with urllib.request.urlopen(urls[i]) as u:
        return u.read()

threads = []
for i in range(5):
    t = Thread(target = read_url, args=(i,))
    threads.append(t)
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print(time.time() - start)
