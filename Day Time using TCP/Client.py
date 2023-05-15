import socket
s = socket.socket()
host = socket.gethostname()
port = 4455
s.connect((host,port))
s.send(b'todays day and time')
res1 = s.recv(1024)
print(res1)
s.close()
