import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 6789
s.connect((host,port))
message = b'Hello'
s.sendto(message,(host,port))
