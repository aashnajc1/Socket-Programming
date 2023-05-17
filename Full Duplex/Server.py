import socket
import os
from _thread import *
s = socket.socket()
host = socket.gethostname()
port = 1234
threadcount = 0
try:
    s.bind((host,port))
except socket.error as e:
    print(str(e))
    print('server is listening...')
s.listen(5)
def multi_threaded_client(connection):
    connection.send(str.encode('server is working'))
    while True:
        data = connection.recv(2048)
        response = 'server message' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(response))
    connection.close()
while True:
    c,addr = s.accept()
    print("connected to :" + addr[0] + ":" + str(addr[1]))
    start_new_thread(multi_threaded_client,(c, ))
    threadcount += 1
    print("thread count : " + str(threadcount))
s.close()
