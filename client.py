import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
h = socket.gethostname()
host = socket.gethostbyname(h)
port = 9999
s.connect((host,port))
print("Client Running")
while True:
    x = input("Enter the data\n")
    if x!='exit':
        s.send(str.encode(x))
        data = str(s.recv(1024), "utf-8")
        print(data)
    else:
        s.send(str.encode(x))
        print("exit")
        break