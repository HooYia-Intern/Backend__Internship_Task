import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('www.udemy.com', 80))
sock.sendall(b'GET / HTTP/1.1\r\nHost: www.example.com\r\n\r\n')

# Receive data
data = sock.recv(1024)
print("Received Data:", data.decode())
sock.close()
