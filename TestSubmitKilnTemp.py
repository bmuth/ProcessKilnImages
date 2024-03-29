import socket
import os
import struct
from datetime import datetime

HOST = '192.168.0.17'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
PATH = "E:\\Utilities\\Qt\\ProcessKilnImages\\data\\Oct 22 2019"
#PATH = "/home/pi/Documents/Projects/KilnProfiler"

def SubmitFile (orig_filename):
    host = socket.gethostbyname(HOST)

    filename = os.path.join (PATH, orig_filename)

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(3)
            s.connect((host, PORT))
 
            s.send ((orig_filename).encode ('utf-8'))
            with open(filename, "rb") as f:
                byte = f.read(4096)
                while byte != b"":
                    s.send (byte)
                    date_time = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
                    byte = f.read(4096)
                print('{0} sent'.format (orig_filename))
                return
            s.close()
    except ConnectionError as e:
        msg = "connection error for host {0} {1}".format(host, str(e))
        print (msg)
        raise

    except FileNotFoundError:
        msg = "file {0} not found".format (filename)
        print (msg)
        raise

    except IOError as e:
        msg = "socket connect {1} on file {0}".format(orig_filename, str(e))
        print (msg)


for file in os.listdir(PATH):
    if file.endswith(".png"):
        try:
            SubmitFile (file)
        except Exception as e:
            print ("err: {0}".format (str(e)))

x = 4

