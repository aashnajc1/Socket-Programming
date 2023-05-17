import socket
s = socket.socket()
host = socket.gethostname()
port = 1234
print('waiting for connection')
try:
    s.connect((host,port))
except socket.error as e:
    print(str(e))
    res = s.recv(1024)
    print(str(res,'utf=8'))
while True:
    Input = input("hey there")
    s.send(str.encode(Input))
    res = s.recv(1024)
    print(res.decode('utf-8'))
s.close()
