import socket
s = socket.socket()
host = socket.gethostname()
port = 5000
s.connect((host,port))
while True:
    res1 = input(">>")
    s.send(res1.encode())
    message = s.recv(1024)
    print(">>",message.decode())
