import socket
try:
 global s
 s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
 print("Socket created\n")
except socket.error as msg:
 print("Socket creation error:"+str(msg))
h = socket.gethostname()
host = socket.gethostbyname(h)
port = 9999
s.bind((host, port))
s.listen(1)
conn, add = s.accept()
print("Ip Address of connected computer is :"+add[0])
print("Port number of connected computer is :"+str(add[1]))
while True:
   data = str(conn.recv(1024),"utf-8")
   if data == "exit":
     print("Connection terminated")
     break
   else:
     print("Received data from client end is as follows:",end=" ")
     print(data)
     conn.send(str.encode("Packet Received"))

