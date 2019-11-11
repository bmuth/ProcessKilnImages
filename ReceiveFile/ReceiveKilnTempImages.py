import socket
import os
from datetime import datetime

PATH = "E:\\Utilities\\Qt\\ProcessKilnImages\\data"
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

host = socket.gethostbyname(socket.gethostname())

def recv_file(sock, file):
    # Helper function to recv n bytes or return None if EOF is hit
    total = 0
    while True:
        packet = sock.recv(4096)
        if not packet:
            return
        file.write (packet)
        total += len(packet)
        print ("read {0} bytes".format (total))

def recv_char (sock):
    data = sock.recv (1)
    return data.decode('utf-8')

def client_thread (sock, ip, port):

    # read in the file name char by char
    
    filename = ""
    while True:
        char = recv_char (sock)
        if (char == '\0'):
            break
        filename += char

    with open (os.path.join (PATH, filename), "wb") as file:
        recv_file (sock, file)

    # could send response here
    # conn.sendall(response)  # send it to client
    sock.close()  # close connection
    print ("{0} created at {1}.".format (filename, datetime.now().strftime("%d/%m/%Y, %H:%M:%S")))
    print('Connection ' + ip + ':' + port + " ended")

def start_server():

    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this is for easy starting/killing the app
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print('Socket created')

    try:
        s.bind((host, PORT))
        print('Socket bind complete')
    except socket.error as msg:
        import sys
        print('Bind failed. Error : ' + str(sys.exc_info()))
        sys.exit()

    #Start listening on socket
    s.listen(10)
    print('Socket now listening')

    # for handling task in separate jobs we need threading
    from threading import Thread

    # this will make an infinite loop needed for 
    # not reseting server for every client
    while True:
        conn, addr = s.accept()
        ip, port = str(addr[0]), str(addr[1])
        print('Accepting connection from ' + ip + ':' + port)
        try:
            Thread (target=client_thread, args=(conn, ip, port)).start()
        except:
            print("Terrible error!")
            import traceback
            traceback.print_exc()
    s.close()

start_server()  

