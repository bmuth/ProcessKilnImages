import socket
import struct
import os

PATH = "E:\\Utilities\\Qt\\ProcessKilnImages\\data"
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

host = socket.gethostbyname(socket.gethostname())

def recv_file(sock, file, n):
    # Helper function to recv n bytes or return None if EOF is hit
    total = 0
    while True:
        packet = sock.recv(min (4096,  n))
        if not packet:
            return
        file.write (packet)
        total += len(packet)
        print ("read {0} bytes".format (total))
        n -= len (packet)

def recv_command (sock):
    data = sock.recv (1)
    return data.decode('utf-8')

def recv_fileinfo (sock):
    data = sock.recv (104)
    (filesize, fn) = struct.unpack ('=I100s', data)
    filename = fn.decode ('utf-8')
    return (filename.strip(), filesize)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, PORT))
    s.listen()
    while True:
        sock, addr = s.accept()
        with sock:
            print('Connected by', addr)
            while True:
                c = recv_command (sock)
                if (c == 'X'):
                    print ("ReadKilnTempImage exiting.")
                    sock.sendall(b'Shutting down')
                elif (c == 'F'):
                    print ("Receiving a file...")
                    (filename, filesize) = recv_fileinfo (sock)
                    with open (os.path.join (PATH, filename), "wb") as file:
                        recv_file (sock, file, filesize)
                    print ("process file and return temperature")
                    sock.sendall(b'1702')
                elif (c == ''):
                    print ("remote application closed socket")
                    break
                else:
                    print ("Unexpected command: {0}".format (c))
                    sock.sendall(b'Unexpected command: ' + c.encode ('utf-8'))
                    break

