# Tyler Robbins
# 4/10/14
# Converter
# Converts *.png, *.jpg, etc. to *.agc (ASCII Graphics)

import pygame,os,sys
from pygame.locals import *

def shutdown():
	sys.exit()
	pygame.quit()

OLDIMG_NAME = ""
NEWIMG_NAME = ""
NEWIMG = ""
EXT = ".AGC"
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
	else: break

	if retry >= 5:
		shutdown()

print OLDIMG_NAME

OLDIMG = pygame.image.load(OLDIMG_NAME)

NEWIMG_NAME = OLDIMG_NAME.split(".",1)
NEWIMG_NAME = NEWIMG_NAME[0] + EXT

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

nuclear = u'\u2622'