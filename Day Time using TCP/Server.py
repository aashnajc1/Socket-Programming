import socket
s = socket.socket()
host = socket.gethostname()
port = 4455
s.bind((host,port))
print('server is listening..')
s.listen(5)
while True:
    c,addr = s.accept()
    print('got connection from', addr)
    req1 = c.recv(1024)
    req1 = str(req1,'utf-8')
    if(req1 == 'todays day and time'):
        print(b'Sun Nov 27 19:23 2022')
    c.close()
