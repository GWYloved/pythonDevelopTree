import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("127.0.0.1", 8000))
server.listen(3)

try:
	while True:
		sock, addr = server.accept()
		data = sock.recv(1024)
		sock.send(data)
		sock.close()
finally:
	server.close()