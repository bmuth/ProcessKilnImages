import socket

#HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

host = socket.gethostbyname(socket.gethostname())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((host, PORT))
	s.listen()
	while True:
		conn, addr = s.accept()
		with conn:
			print('Connected by', addr)
			while True:
				data = conn.recv(1024)
				if not data:
					print ("closing connection")
					break
				str = data.decode('utf-8')
				print ("Received: [{0}]".format(str))
				if (str[0] == 'R'):
					print ("read file and process")
					conn.sendall(b'1702')
				elif (str[0] == 'X'):
					print ("ReadKilnTempImage exiting.")
					conn.sendall(b'Shutting down')
					exit ()
				else:
					print ("Unexpected command: {0}".format (str))
					conn.sendall(b'Unexpected command: ' + data)
					break

