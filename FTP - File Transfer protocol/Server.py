import socket
host = socket.gethostname()
port = 12345
def main():
    s = socket.socket()
    s.bind((host,port))
    s.listen(5)
    print('server is listening')
    while True:
        c,addr = s.accept()
        filename = c.recv(1024).decode('utf-8')
        print(f'receving filename')
        file = open(filename, "w")
        c.send("receving filename".encode('utf-8'))
        data = c.recv(1024).decode('utf-8')
        print(f'receiving file data')
        file.write(data)
        print(data)
        c.send("file data received".encode('utf-8'))
        file.close()
        c.close()
if __name__ == "__main__":
    main()
