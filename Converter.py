# Tyler Robbins
# 4/10/14
# Converter
# Converts binary images to *.agc (ASCII Graphics Color)
# Also converts *.agc back to binary images

import pygame,os,sys
from pygame.locals import *

def shutdown():
	sys.exit()
	pygame.quit()

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

######Interpret the data######
def interpret(data):
	data = data.split("\n")
	print data[0]
	h = int(data[0].split(":")[1])
	w = int(data[1].split(":")[1])
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

######Create Surface object######
def draw(rows,res):
	y=0
	x=0

	IMG = pygame.Surface(res)
	pixels = STRtoTUP(rows)

	for row in pixels:
		for pixel in row:
		 	try:
			 	IMG.set_at((x,y), pixel)
			except: pass
			x+=1
		y+=1
		x = 0

	return IMG

OLDIMG_NAME = ""
NEWIMG_NAME = ""
NEWIMG = ""
EXT = "AGC"
EXTS = ("jpg","png","bmp","tga") #Valid file types
isAGC = False
retry = 0
x = 0
y = 0

pygame.init()

while OLDIMG_NAME == "":
	print "Please move the file into the current folder (" + str(os.getcwd()) + ")."
	OLDIMG_NAME = raw_input("Name of file to convert:\n> ")

	if OLDIMG_NAME not in os.listdir(os.getcwd()):
		print "File not found."
		retry+=1
		OLDIMG_NAME = ""

	elif len(OLDIMG_NAME.split(".")) > 2:
		print "Please make sure there are no '.'s in your file's name before trying to convert it."
		OLDIMG_NAME = ""

	else: print "Valid file name."

	if retry >= 5:
		shutdown()

print OLDIMG_NAME

######Allow user to convert AGC to JPG, PNG, etc.######
if OLDIMG_NAME.split(".")[1] == EXT:
	isAGC = True

	while True:
		entry = raw_input("Convert " + OLDIMG_NAME + " to file type: ").lower()

		if entry not in EXTS:
			print "Not a valid extension!"

		else:
			print "Converting " + OLDIMG_NAME + " to " + ".".join([OLDIMG_NAME.split(".")[0], entry]) + "."
			EXT = entry
			break
else:
	OLDIMG = pygame.image.load(OLDIMG_NAME)

NEWIMG_NAME = OLDIMG_NAME.split(".")[0]
NEWIMG_NAME = ".".join([NEWIMG_NAME, EXT])

######Convert binary images to AGC######
if not isAGC:
	NEWIMG += "HEIGHT:" + str(OLDIMG.get_height()) + "\n"
	NEWIMG += "WIDTH:" + str(OLDIMG.get_width()) + "\n\n"

	print NEWIMG

	for y in range(OLDIMG.get_height()):
		for x in range(OLDIMG.get_width()):
			NEWIMG += str(OLDIMG.get_at((x,y))) + "|"
			x+=1
			print x,

		NEWIMG += "\n"
		x = 0

	open(NEWIMG_NAME, "w").write(NEWIMG)

######Convert AGC to binary images######
else:
	print NEWIMG_NAME
	returns = interpret(open(OLDIMG_NAME, "r").read())
	IMG_DISP = returns[0]
	ROWS = returns[1]

	OLDIMG = draw(ROWS,IMG_DISP)
	pygame.image.save(OLDIMG, NEWIMG_NAME)

nuclear = u'\u2622'