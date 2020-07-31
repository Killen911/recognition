import pygame
from random import choice, random, randint

images = [
	# Я
	(-1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, 1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, -1, -1, 1, 1, -1, -1, -1, -1, 1),
	(-1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1),
	(-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1),
	#(-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1),
	(-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1),
	#(-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, -1, -1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, 1, -1, -1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, -1, -1, -1, 1, 1, -1, -1, -1, -1, 1, -1),
	#(-1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, -1, -1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, 1, -1, -1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, -1, -1, -1, 1, 1, -1, -1, -1, -1, 1, -1),
	#(1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1),
	(1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1),
	(-1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1),
	#(1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1),
	(-1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1),
	(-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1),
	#(-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, -1, 1, 1, -1)
]

myimg = [-1 for a in range(100)]


def hopefield_r(signals):
	fields = len(signals)
	weights = [[0 for i in range(fields)] for j in range(fields)]
	# обучение
	for img in images:
		for i in range(fields):
			for j in range(fields):
				if i == j:
					continue
				weights[i][j] += img[i] * img[j]  # корректировка

	# распознавание
	counter = 0
	while counter < fields*4:
		d = 0.0  # накопитель
		r = randint(0, fields - 1)
		for i in range(fields):
			d += weights[i][r] * signals[i]  # change this for autoassociative hamming
		if d > 0.0:
			if signals[r] == 1:
				counter += 1 # not changed - counter ++
			else:
				counter = 0
				signals[r] = 1
		else:
			if signals[r] == -1:
				counter += 1 # not changed - counter ++
			else:
				counter = 0
				signals[r] = -1
	return signals


def auto_hamming(signals):
	fields = len(signals)
	counter = 0
	while counter < fields*4:
		T = list()
		for img in images:
			t = 0.0  # накопитель
			for i in range(fields):
				t += img[i]*signals[i]
			T.append(t)

		summator = 0.0
		r = randint(0, fields - 1)
		for s in range(len(images)):
			summator += images[s][r]*T[s]

		if summator > 0.0:
			if signals[r] == 1:
				counter += 1 # not changed - counter ++
			else:
				counter = 0
				signals[r] = 1
		else:
			if signals[r] == -1:
				counter += 1 # not changed - counter ++
			else:
				counter = 0
				signals[r] = -1
	return signals

pygame.init()
window = pygame.display.set_mode((1280, 720))
font = pygame.font.SysFont("arial", 14)
cc = []  # коэфициенты коррелляции
work = True
familiar = None
noise = 0.2
while work:
	pyevents = pygame.event.get()
	mouse_position = pygame.mouse.get_pos()
	click = False
	hamming = False
	for event in pyevents:
		if event.type == pygame.QUIT:
			work = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			click = True
	window.fill((0,0,0))
	x = 10
	y = 10
	size = 4
	for img in images:
		for i, elem in enumerate(img):
			if elem == 1:
				color = (240, 240, 240)
			else:
				color = (50, 50, 50)
			pygame.draw.rect(window, color, ((x,y), (size, size)))
			if click and mouse_position[0] in range(x, x+size) and mouse_position[1] in range(y, y+size):
				myimg = list(img)
				#print(myimg)
			if (i+1) % 10 == 0:  # new line
				x = 10
				y += size
			else:
				x += size
		x = 10
		y += size

	x = 250
	y = 10
	size = 40
	for i, elem in enumerate(myimg):
		if elem == 1:
			color = (240, 240, 240)
		else:
			color = (50, 50, 50)
		pygame.draw.rect(window, color, ((x, y), (size, size)))
		pygame.draw.rect(window, (200, 200, 200), ((x, y), (size, size)), 1)  # сетка
		if click and mouse_position[0] in range(x, x+size) and mouse_position[1] in range(y, y+size):
			#print(myimg)
			myimg[i] *= -1
		if (i+1) % 10 == 0:  # new line
			x = 250
			y += size
		else:
			x += size

	# noise button
	pygame.draw.rect(window, (200, 0, 0), (x, y, size, size))
	window.blit(font.render("Шум", 0, (30, 30, 30)), (x, y))
	if click and mouse_position[0] in range(x, x + size) and mouse_position[1] in range(y, y + size):
		for i in range(len(myimg)):
			if noise > random():
				myimg[i] *= -1
		familiar = None
	x += size

	pygame.draw.rect(window, (60,150,40), (x, y, size, size))
	window.blit(font.render("Хэм.", 0, (30, 30, 30)), (x, y))
	if click and mouse_position[0] in range(x, x+size) and mouse_position[1] in range(y, y+size):
		hamming = True
		cc = list()

	x += size

	pygame.draw.rect(window, (255, 192, 203), (x, y, size, size))
	window.blit(font.render("Авт. Хэм.", 0, (30, 30, 30)), (x, y))
	if click and mouse_position[0] in range(x, x + size) and mouse_position[1] in range(y, y + size):
		myimg = auto_hamming(myimg)
		try:
			familiar = images.index(tuple(myimg))
		except ValueError:
			familiar = None

	x += size

	# Хоупфилд рандомизированный
	pygame.draw.rect(window, (200, 200, 0), (x, y, size, size))
	window.blit(font.render("Х.р.", 0, (30, 30, 30)), (x, y))
	if click and mouse_position[0] in range(x, x + size) and mouse_position[1] in range(y, y + size):
		myimg = hopefield_r(myimg)
		try:
			familiar = images.index(tuple(myimg))
		except ValueError:
			familiar = None
	x += size
	# save button
	pygame.draw.rect(window, (0, 200, 200), (x, y, size, size))
	window.blit(font.render("Сохр.", 0, (30, 30, 30)), (x, y))
	if click and mouse_position[0] in range(x, x + size) and mouse_position[1] in range(y, y + size):
		images.append(tuple(myimg))
		myimg = [-1 for a in range(100)]

	x += size
	# clear button
	pygame.draw.rect(window, (0, 200, 200), (x, y, size, size))
	window.blit(font.render("Очист.", 0, (30, 30, 30)), (x, y))
	if click and mouse_position[0] in range(x, x + size) and mouse_position[1] in range(y, y + size):
		myimg = [-1 for a in range(100)]

	x = 250
	y += size*2
	if click and mouse_position[0] in range(x, x + size) and mouse_position[1] in range(y, y+size) and noise > 0.0:
		pygame.draw.rect(window, (255, 165, 0), (x, y, size, size))
		noise = round(noise - 0.05, 2)
	else:
		pygame.draw.rect(window, (200, 100, 0), (x, y, size, size))

	x += size
	window.blit(font.render("{:.0%}".format(noise), 0, (200, 200, 200)), (x, y))

	x += size
	if click and mouse_position[0] in range(x, x + size) and mouse_position[1] in range(y, y+size) and noise < 1.0:
		pygame.draw.rect(window, (0, 255, 0), (x, y, size, size))
		noise = round(noise + 0.05, 2)
	else:
		pygame.draw.rect(window, (0, 200, 0), (x, y, size,size))


	# рисуем распознанное
	y = 10
	x = 250 + 11*size
	if isinstance(familiar, int):
		for i, elem in enumerate(images[familiar]):
			if elem == 1:
				color = (240, 240, 240)
			else:
				color = (50, 50, 50)
			pygame.draw.rect(window, color, ((x, y), (size, size)))
			pygame.draw.rect(window, (200, 200, 200), ((x, y), (size, size)), 1)  # сетка
			if (i + 1) % 10 == 0:  # new line
				x = 250 + 11*size
				y += size
			else:
				x += size

	y = 10
	x = 250 + 11 * size
	# Хэмминг
	if hamming:
		pygame.draw.rect(window, (0, 200, 0), (x-4, y-4, 10*size+8, y+10*size+8))
		for img in images:
			c = 0
			for i, elem in enumerate(img):
				c += elem * myimg[i]
			c *= 1 / len(img)
			cc.append(c**2)
		#print(cc)
		familiar = cc.index(max(cc))
		#print(familiar, max(cc))

	pygame.time.Clock().tick(30)
	pygame.display.flip()
#for elem in images:
#	print(elem)
