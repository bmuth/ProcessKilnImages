import socket
import os

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server


def SubmitFile (filename):
    host = socket.gethostbyname(socket.gethostname())

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, PORT))
            with open(filename, "rb") as f:
                byte = f.read(4096)
                while byte != b"":
                    sa.send (byte)
                    byte = f.read(4096)
                data = s.recv(1024)
                print('Response: [{0}]'.format (data.decode('utf-8')))
    except ConnectionError as e:
        print ("connection error for host {0} {1} {2}".format(HOST, e.errno, e.strerror))

    except IOError as e:
        print ("transmission error on file {0} {1} {2}".format(filename, e.errno, e.strerror))

filename = "./data/image/xxx.png"
SubmitFile (filename)

