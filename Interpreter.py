#Tyler Robbins
#4/11/14
#Interpreter
#Interprets AGC files and displays them to the screen

import pygame, os, sys
from pygame.locals import *

WHITE = (255,255,255)

def shutdown():
	sys.exit()
	pygame.quit()

######Interpret the data######
def interpret(data):
	data = data.split("\n")
	H_DEF = int(data[0].split(":")[1])
	W_DEF = int(data[1].split(":")[1])
	h = H_DEF
	w = W_DEF
	rows = []
	scale = ""

	data.pop(0)
	data.remove(data[1])
	data.remove(data[2])
	filter(None,data)

	for i in data:
		if not i.startswith("("):
			continue
		else:
			rows.append(i)

	for i in rows:
		x = i.split("|")
		rows[rows.index(i)] = x

	return [(w,h),rows]

######Convert strings into tuples######
def STRtoTUP(string):
	for row in string:
		for p in row:
			pixel = []
			pos = row.index(p)
			
			#Turn each string (pixel) into a tuple of integers#
			p = p.split(", ")
			p[0] = p[0][1:]
			p[len(p)-1] = p[len(p) -1][:1]

			for i in p:
				if i == '':
					continue
				else:
					pixel.append(int(i))
			pixel = tuple(pixel)

			row[pos] = pixel

	return string

######Draw the Surface object######
def draw(rows,res):
	y=0
	x=0

	IMG = pygame.Surface(res)
	pixels = STRtoTUP(rows)

	print "result: " + str(pixels[0][0])

	#print pixels

	for row in pixels:
		for pixel in row:
		 	try:
			 	IMG.set_at((x,y), pixel)
			except: pass #print pixel
			x+=1
		y+=1
		x = 0

	res = list(res)

	#IMG = pygame.transform.scale(IMG,res)

	return [IMG,res]

def keycheck(event):
	if event == QUIT:
		print "SHUTDOWN!"
		shutdown()
	if event == KEYDOWN:
		if event.key == K_ESCAPE:
			print "SHUTDOWN!"
			shutdown()

pygame.init()

IMG_NAME = ""
IMG_DATA = ""
scale = ""
retry = 0
HEIGHT = 0
WIDTH = 0
returns = []
InfoObj = pygame.display.Info()
CONFIG = open("CONFIG.txt", "r").read()
CONFIG = CONFIG.split("\n")

######Get Image######
while IMG_NAME == "":
	print "Please move the file into the current folder (" + str(os.getcwd()) + ")."
	IMG_NAME = raw_input("Name of file to open:\n> ")

	if IMG_NAME not in os.listdir(os.getcwd()):
		print "File not found."
		retry+=1
		IMG_NAME = ""
	else: break

	if retry >= 5:
		shutdown()

returns = interpret(open(IMG_NAME, "r").read())
DISP = returns[0]
IMG_DISP = returns[0]
ROWS = returns[1]

returns = draw(ROWS,IMG_DISP)

res = returns[1]
IMG = returns[0]

print "DISP" + str(DISP)
print "IMG " + str(IMG_DISP)

display = pygame.display.set_mode(DISP)
display.fill(WHITE)

display.blit(IMG,(0,0))

while True:
	for event in pygame.event.get():
		keycheck(event)
		if event == KEYDOWN:
			if event.key == K_LEFTBRACKET:
				res = (res[0]-5,res[1]-5)
				IMG = pygame.transform.scale(IMG,res)
				display.blit(IMG,(0,0))
				print "smaller"

			elif event.key == K_RIGHTBRACKET:
				res = (res[0]+5,res[1]+5)
				IMG = pygame.transform.scale(IMG,res)
				display.blit(IMG,(0,0))
				print "bigger"

	pygame.display.update()

nuclear = u'\u2622'