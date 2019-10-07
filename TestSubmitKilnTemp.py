import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

host = socket.gethostbyname(socket.gethostname())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, PORT))
    s.sendall(b'X')
    data = s.recv(1024)
print('Response: [{0}]'.format (data.decode('utf-8')))