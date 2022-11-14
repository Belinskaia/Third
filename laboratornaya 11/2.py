import os, re
import threading


received_packages = re.compile(r"(\d) received")
status = ("no response", "alive but losses", "alive")

def calling_ip (i):
    ip = "192.168.178." + str(i+20)
    ping_out = os.popen("ping -q -c2 " + ip, "r")
    print("... pinging ", ip)
    while True:
        line = ping_out.readline()
        if not line:
            break
        n_received = received_packages.findall(line)
        if n_received:
            print(ip + ": " + status[int(n_received[0])])
            
threads = [threading.Thread(target=calling_ip, args=(i,)) for i in range(10)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
