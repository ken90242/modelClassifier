import socket
import sys
import json

query = sys.argv[1]

host = '40.71.194.227'

# The same port as used by the server
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall(query.encode('utf8'))
data = s.recv(1024).decode('utf8')
s.close()

print('Received', repr(json.loads(data)))
