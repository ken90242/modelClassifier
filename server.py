import socket
import json
from src.splitProcess import outputRes

# Symbolic name meaning all available interfaces
host = '127.0.0.1'
# Arbitrary non-privileged port
port = 12345


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

print('Server Ready.')

while True:
	conn, addr = s.accept()
	print('Connected by', addr)
	query = conn.recv(1024).decode('utf8')
	res = outputRes(query)
	json_res = json.dumps(res).encode('utf8')

	if not query:
		break
	conn.sendall(json_res)
conn.close()
