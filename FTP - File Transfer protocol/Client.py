import socket
host = socket.gethostname()
port = 12345
def main():
    s = socket.socket()
    s.connect((host,port))
    file = open("demo1.txt","r")
    data = file.read()
    s.send("demo1.txt".encode('utf-8'))
    message = s.recv(1024).decode('utf-8')
    print(f'[Server]: {message}')
    s.send(data.encode('utf-8'))
    message = s.recv(1024).decode('utf-8')
    print(f'[Server]:{message}')
    file.close()
    s.close()
if __name__ == "__main__":
          main()
