# Подключение всех необходимых библиотек
# Нам нужно: speech_recognition, os, sys, webbrowser
# pyautogui для открытия программ
# Для первой бибилотеки прописываем также псевдоним
import sys
import pyautogui as pg
import webbrowser
import speech_recognition as sr
import mod
import random

# Функция, позволяющая проговаривать слова
# Принимает параметр "Слова" и прогроваривает ихщгтеук-ыекшлу

def talk(words):
	print(words) # Дополнительно выводим на экран

# Вызов функции и передача строки 
# именно эта строка будет проговорена компьютером
talk("Привет, Я Йен 1.0 - Ваш персональный голосовой ассистент.\nВот список моих навыков:"
	 "\n- Запуск онлайн игр на Вашем ПК"
	 "\n- Генерирование случайной игры"
	 "\n- Запуск сайтов"
	 "\nДля взаимодействия со мной включите английскую раскладку и задайте голосовую команду"
	 "\nЧтобы узнать подробнее, скажите: 'список команд'")

""" 
	Функция command() служит для отслеживания микрофона.
	Вызывая функцию мы будет слушать что скажет пользователь,
	при этом для прослушивания будет использован микрофон.
	Получение данные будут сконвертированы в строку и далее
	будет происходить их проверка.
"""
def command():
	# Создаем объект на основе библиотеки
	# speech_recognition и вызываем метод для определения данных
	r = sr.Recognizer()

	# Начинаем прослушивать микрофон и записываем данные в source
	with sr.Microphone() as source:
		# Просто вывод, чтобы мы знали когда говорить
		print("Говорите")
		# Устанавливаем паузу, чтобы прослушивание
		# началось лишь по прошествию 1 секунды
		r.pause_threshold = 1
		# используем adjust_for_ambient_noise для удаления
		# посторонних шумов из аудио дорожки
		r.adjust_for_ambient_noise(source, duration=1)
		# Полученные данные записываем в переменную audio
		# пока мы получили лишь mp3 звук
		audio = r.listen(source)

	try: # Обрабатываем все при помощи исключений
		""" 
		Распознаем данные из mp3 дорожки.
		Указываем что отслеживаемый язык русский.
		Благодаря lower() приводим все в нижний регистр.
		Теперь мы получили данные в формате строки,
		которые спокойно можем проверить в условиях
		"""
		zadanie = r.recognize_google(audio, language="ru-RU").lower()
		# Просто отображаем текст что сказал пользователь
		print("Вы сказали: " + zadanie)
	# Если не смогли распознать текст, то будет вызвана эта ошибка
	except sr.UnknownValueError:
		# Здесь просто проговариваем слова "Я вас не поняла"
		# и вызываем снова функцию command() для
		# получения текста от пользователя
		talk("Команда не распознана")
		zadanie = command()

	# В конце функции возвращаем текст задания
	# или же повторный вызов функции
	return zadanie

# Данная функция служит для проверки текста, 
# что сказал пользователь (zadanie - текст от пользователя)
def makeSomething(zadanie):
	# Попросту проверяем текст на соответствие
	# Если в тексте что сказал пользователь есть слова
	# "открыть вк", то выполняем команду


	if 'список команд' in zadanie:
		talk("вот список распознаваемых мною команд"
			 "\n'открой vk'"
			 "\n'открой youtube'"
			 "\n'открой twitch'"
			 "\n'выбери игру'"
			 "\n'запусти dota'"
			 "\n'запусти cs go'"
			 "\n'запусти калибр'"
			 "\n'запусти world of tanks'"
			 "\n'запусти world of warships'"
			 "\n'запусти war thunder'"
			 "\n'запусти overwatch'"
			 "\n'запусти heroes of the storm'"
			 "\n'запусти warcraft'"
			 "\n'запусти hearthstone'"
			 "\n'запусти pubg'"
			 "\n'запусти fortnite'"
			 "\n'запусти rust'"
			 "\n'запусти league of legends'"
			 "\n'запусти team fortress'"
			 "\n'запусти кроссаут'"
			 "\n'запусти warface'"
			 "\n'запусти rainbow six'"
			 "\n'запусти valorant'"
			 "\n'запусти minecraft'"
			 "\n'запусти call of duty'"
			 "\n'запусти gta'"
			 "\n'запусти fifa'"
			 "\n'запусти battlefield'"
			 "\n'запусти mortal kombat'"
			 "\n'открой origin'"
			 "\n'открой steam'"
			 "\n'открой epic games'"
			 "\n'открой wargaming'"
			 "\n'открой blizzard'"
			 "\n'открой discord'"
			 "\n'стоп'")

	elif 'открой vk' in zadanie:
		# Проговариваем текст
		talk("Уже открываю")
		# Указываем сайт для открытия
		url = 'https://vk.com/feed'
		# Открываем сайт
		webbrowser.open(url)
		sys.exit()
	# открыть ютюб
	elif 'открой youtube' in zadanie:
		talk("Уже открываю")
		url = 'https://www.youtube.com'
		webbrowser.open(url)
		sys.exit()

	# открыть твич
	elif 'открой twitch' in zadanie:
		talk("Уже открываю")
		url = 'https://www.twitch.com'
		webbrowser.open(url)
		sys.exit()

	# если было сказано "стоп", то останавливаем прогу
	elif 'стоп' in zadanie:
		# Проговариваем текст
		talk("Да, конечно, без проблем")
		# Выходим из программы
		sys.exit()

	# Рандомный выбор игры
	elif 'выбери игру' in zadanie:
		talk("Напишите игры, из которых мне сделать выбор.")
		print("Названия игр запишите на английском языке. (Если в названии содержатся пробелы, замените их на _)")
		lst = list(input().split())
		a = random.choice(lst)
		print("Ваша игра - ", a)

	# Открыть доту
	elif 'запусти dota' in zadanie:
		talk("Секунду...")
		mod.dota()

	# Открыть кс го
	elif 'запусти cs go' in zadanie:
		talk("Секунду...")
		mod.csgo()

	# Открыть калибр
	elif 'запусти калибр' in zadanie:
		talk("Секунду...")
		mod.caliber()

	# Открыть танки
	elif 'запусти world of tanks' in zadanie:
		talk("Секунду...")
		mod.tanks()

	# Открыть корабли
	elif 'запусти world of warships' in zadanie:
		talk("Секунду...")
		mod.warships()

	# Открыть war thunder
	elif 'запусти war thunder' in zadanie:
		talk("Секунду...")
		mod.warthunder()

	# Открыть овервотч
	elif 'запусти overwatch' in zadanie:
		talk("Секунду...")
		mod.overwatch()

	# Открыть герои шторма
	elif 'запусти heroes of the storm' in zadanie:
		talk("Секунду...")
		mod.hos()

	# Открыть warcraft
	elif 'запусти warcraft' in zadanie:
		talk("Секунду...")
		mod.warcraft()

	# Открыть хартстоун
	elif 'запусти hearthstone' in zadanie:
		talk("Секунду...")
		mod.hearthstone()

	# Открыть пубг
	elif 'запусти pubg' in zadanie:
		talk("Секунду...")
		mod.pubg()

	# Открыть фортнайт
	elif 'запусти fortnite' in zadanie:
		talk("Секунду...")
		mod.fortnite()

	# Открыть раст
	elif 'запусти раст' in zadanie:
		talk("Секунду...")
		mod.rust()

	# Открыть lol
	elif 'запусти league of legends' in zadanie:
		talk("Секунду...")
		mod.lol()

	# Открыть тим фортресс
	elif 'запусти team fortress' in zadanie:
		talk("Секунду...")
		mod.tf()

	# Открыть тим фортресс
	elif 'запусти apex legends' in zadanie:
		talk("Секунду...")
		mod.apex()

	# Открыть кроссаут
	elif 'запусти кроссаут' in zadanie:
		talk("Секунду...")
		mod.crossout()

	# Открыть варфэйс
	elif 'запусти warface' in zadanie:
		talk("Секунду...")
		mod.warface()

	# Открыть rainbowsix
	elif 'запусти rainbow six' in zadanie:
		talk("Секунду...")
		mod.rainbowsix()

	# Открыть валорант
	elif 'запусти валорант' in zadanie:
		talk("Секунду...")
		mod.valorant()

	# Открыть майнкрафт
	elif 'запусти minecraft' in zadanie:
		talk("Секунду...")
		mod.minecraft()

	# Открыть колду
	elif 'запусти call of duty' in zadanie:
		talk("Секунду...")
		mod.cod()

	# Открыть гта

	elif 'запусти gta' in zadanie:
		talk("Секунду...")
		mod.GTA()

	# Открыть фифа
	elif 'запусти fifa' in zadanie:
		talk("Секунду...")
		mod.FIFA()

	# Открыть батлфилд
	elif 'запусти battlefield' in zadanie:
		talk("Секунду...")
		mod.battlefield()

	# Открыть мортуху
	elif 'запусти mortal kombat' in zadanie:
		talk("Секунду...")
		mod.mk()

	# Открыть origin
	elif 'открой ориджин' in zadanie:
		talk("Секунду...")
		mod.origin()

	# Открыть дискорд
	elif 'открой discord' in zadanie:
		talk("Секунду...")
		mod.discord()

	# Открыть стим
	elif 'открой steam' in zadanie:
		talk("Секунду...")
		mod.steam()

	# Открыть эпик
	elif 'открой epic games' in zadanie:
		talk("Секунду...")
		mod.epic( )

	# Открыть варгейминг
	elif 'открой wargaming' in zadanie:
		talk("Секунду...")
		mod.wargaming( )

	# Открыть близард
	elif 'открой blizzard' in zadanie:
		talk("Секунду...")
		mod.blizzard()

# Вызов функции для проверки текста будет

# осуществляться постоянно, поэтому здесь
# прописан бесконечный цикл while

while True:
	makeSomething(command())