import socket
import sys
from _thread import *


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)

host = 'localhost'
port = 5555

try:
	s.bind((host, port))
except socket.error as e:
	print(str(e))

print(f"Loading Connection on port {port}...")
s.listen(5)

def threaded_client(conn):
	# Messages sent out get encoded
	conn.send(str.encode("Welcome, type your info.\n"))

	# Keep client alive
	while True:
		data = conn.recv(2048)

		# Messages received get decoded
		reply = 'Server output: ' + data.decode('utf-8')
		if not data:
			break
		conn.sendall(str.encode(reply))

while True:
	conn, addr = s.accept()
	print('Connected to: ' + addr[0] + ":" + str(addr[1]))

	start_new_thread(threaded_client, (conn,))
