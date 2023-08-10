import socket
import threading
from queue import Queue

target = "192.168.0.1" 
queue=Queue()
open_ports=[]
###closed_ports=[]   - we are printing only the open ports

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False

def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port{} is open!".format(port))
            open_ports.append(port) ##### it will print only the open ports
        ###else:
            ###print("Port{} is closed!".format(port))
            ###closed_ports.append(port)    ### it will print also the closed ports

port_list=range(1, 1024)
fill_queue(port_list)

thread_list =[]

### this will give 100x times the initial scanning speed
for t in range(100):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("Open ports are: ", open_ports)
###print("Closed ports are: ", closed_ports)


