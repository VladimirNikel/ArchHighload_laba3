import socket
import threading
import random

host, port = 'localhost', 8007

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5) # max backlog of connections

print('Слушаю {}:{}'.format(host, port))


def handle_client_connection(client_socket):
	myNumber = random.randint(0,100)
	request = ""
	playerNumber = -1
	while (playerNumber != myNumber):
		request = client_socket.recv(4096)
		str_request = request.decode('utf-8')
		playerNumber = int(str_request[6:])
		if playerNumber < myNumber:
			client_socket.send('more'.encode())
		elif playerNumber > myNumber:
			client_socket.send('less'.encode())
		elif playerNumber == myNumber:
			client_socket.send('correct'.encode())
		else:	#вообще, это не должно произойти, но написал на всякий случай
			print("Я его не понимаю! Разберись с ним!")
			client_socket.send('Я тебя не пойму'.encode())
	client_socket.close()

while True:
	client_sock, address = server.accept()
	print('Новое подключение с {}:{}'.format(address[0], address[1]))
	client_handler = threading.Thread(
		target=handle_client_connection,
		args=(client_sock,)  # без запятой получаю... TypeError: handle_client_connection() argument after * must be a sequence, not _socketobject
	)
	client_handler.start()