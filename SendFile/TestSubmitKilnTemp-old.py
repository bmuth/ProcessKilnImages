import socket
import os
import struct

HOST = '192.168.0.17'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
#PATH = "E:\\Utilities\Qt\\ProcessKilnImages\\data\\images"
PATH = "/home/pi/Documents/Projects/KilnProfiler"

def SubmitFile (orig_filename):
    host = socket.gethostbyname(HOST)

    filename = os.path.join (PATH, orig_filename)

    try:
        fs = int (os.path.getsize(filename))
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(3)
            s.connect((host, PORT))
            c = 'F'

            # 1 byte command
            # 4 bytes for file size
            # 100 bytes for file name
            # total 105 bytes to be sent
            data = struct.pack ('=cI100s', c.encode('utf-8'), fs, "{:<100}".format (orig_filename).encode ('utf-8'))
            s.send (data)
            total = 0
            with open(filename, "rb") as f:
                byte = f.read(4096)
                while byte != b"":
                    total += len(byte)
                    s.send (byte)
                    print ("Sent {0} bytes".format (total))
                    byte = f.read(4096)
                data = s.recv(1024)
                print('Response: [{0}]'.format (data.decode('utf-8')))
                return
    except ConnectionError as e:
        msg = "connection error for host {0} {1}".format(host, str(e))
        print (msg)
        raise

    except FileNotFoundError:
        msg = "file {0} not found".format (filename)
        print (msg)
        raise

    except IOError as e:
        msg = "transmission error on file {0} {1}".format(orig_filename, str(e))
        print (msg)
        raise

orig_filename = "K2019-09-23 06.34.14.png"

# c = 'F'
# fs = int (os.path.getsize(filename))
# # data = struct.pack ('I', fs)
# data = struct.pack ('c', c.encode('utf-8'))
# data = struct.pack ('=cI', c.encode('utf-8'), fs)
# # b = "{:<2}".format (filename).encode ('utf-8')
# # data = struct.pack ('50s', "{:<50}".format (filename).encode ('utf-8'))
# data = struct.pack ('=cI100s', c.encode('utf-8'), fs, "{:<100}".format (filename).encode ('utf-8'))
try:
    SubmitFile (orig_filename)
except Exception as e:
    print ("err: {0}".format (str(e)))

x = 4

