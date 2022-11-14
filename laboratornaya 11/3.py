from threading import Thread
import time
M = [150, 60, 80, 51, 61, 91]
start = time.time()
def matter(i, A):
    global s
    if i == 0:
        s = 0
    s += sum(A)

def run_threads(count):
    threads = []
    D = len(M)//count +1
    for i in range(count):
        A = M[i*D:(i+1)*D]
        t = Thread(target = matter, args=(i, A))
        threads.append(t)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

run_threads(4)
print(s)
print(time.time() - start)
