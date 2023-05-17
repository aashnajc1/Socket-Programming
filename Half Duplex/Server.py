import socket
s = socket.socket()
host = socket.gethostname()
port = 5000
s.bind((host,port))
c,addr = s.accept()
while True:
    req1 = c.recv(1024)
    req1 = str(req1,'utf-8')
    print(">>",req1)
    message = input(">>")
    c.sendto(message.encode())
    c.close()
