from threading import Thread
import time

start = time.time()
def matter(i):
    M = [150, 60, 80, 51, 61, 91]
    global s
    if i == 0:
        s = 0
    s += M[i]

def run_threads(count):
    threads = []
    for i in range(count):
        t = Thread(target = matter, args=(i,))
        threads.append(t)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

run_threads(6)
print(s)
print(time.time() - start)
