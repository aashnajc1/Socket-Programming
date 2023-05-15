import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 6789
s.bind((host,port))
while True:
    c,addr = s.recvfrom(1024)
    print("Message : ", c)
