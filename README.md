# Архитектура высоконагруженных система. ДЗ №3
## Создание игры "Угадай число" с использованием TCP-сервера и клиента

## Цель:
> Написать сервер и клиент, общающиеся по протоколу TCP. Сервер должен реализовывать игру "Угадай число". Клиент угадывает число, получая текущий результат от сервера.
> 
> Сервер должен принимать запросы в формате `<команда> <аргумент>`.
> 
> Допустима команда `guess` с аргументом в виде числа.
> 
> Сервер отвечает одним из вариантов: `["more", "less", correct]` в зависимости от агрумента, переданного клиентом.
> 
> Также необходимо было захватить с помощью команды `tcpdump` полный лог одной игры и записать его в файл.


## Инструкция по установке:
1. Скачать/стянуть репозиторий
1. Перейти в папку репозитория
1. Первым всегд азапускается сервер командой `python3 server.py`
1. Далее запускается клиент командой `python3 client.py`
1. Пользуемся игрой
1. Когда клиент наиграется с сервером необходимо сервер остановить командой от нажатия клавиш `Ctrl+C`


## Плюшки:
* Клиент (человек) играет с сервером вводя числа в промежутке от 0 до 100
  * Включена проверка на вводимые данные
* Клиент получает ответы сервера (как указано в задании) и снова вводит своё число, пока не угадает
* Можно играть сразу с нескольких терминалов
  * Выставлено ограничение на слушание сразу 5 клиентов, но реальных подключений может быть и больше (проверено эмпирическим путем)
* Составлен log-файл трех игр (с разными параметрами):
  * `sudo tcpdump -vvv -i lo > log.txt`
  * `sudo tcpdump -vA -i lo >> log.txt`
  * `sudo tcpdump -vXX -i lo >> log.txt`



## Инструментарий:
- GIT (устанавливается командой `sudo apt install git -y`)
- Python (устанавливается командой `sudo apt install python3 -y`)
- Установщик пакетов Python PIP3 (устанавливается командой `sudo apt install python3-pip -y`)
- Установленные модули:
	+ random `sudo pip3 install random`
- tcpdump (устанавливается командой `sudo apt install tcpdump`)
