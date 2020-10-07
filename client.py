import socket

host, port = 'localhost', 8007
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((host, port))
response = ""
myNumber = -1

print("**************************************************\nНазвание: \"Угадай число\"\nОписание: Вам необходимо угадать загаданное число сервером (это число находится в интервале от 0 до 100). Игра длится до момента, пока Вы не угадаете число.\nАвтор: Ниемисто Владимир, М3О-117М-20, [Nikel] 2020 Moscow\n**************************************************\n")

while (response != "correct"):
	myNumber=input("Введите ваше предполагаемое число в интервале от 0 и до 100:\t")
	try:
		myNumber = int(myNumber)
		if myNumber >= 0 and myNumber <= 100:
			client.send(("guess "+str(myNumber)).encode())
			response = client.recv(4096).decode('utf-8')
			print (response)
		else:
			continue
	except ValueError:
		continue
