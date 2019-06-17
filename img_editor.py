#/usr/bin/env python3
# Coded By : A_Asaker

import getopt
from sys import platform,argv
from mss import mss
from time import sleep
import cv2 as cv
import numpy as np
from subprocess import call

def usage():
	print('''\t \t Image Editor | By A_Asaker
Options :
	*[Open An Existing Image]:
		-i,--image  <path>	: image path
	*[Create A New Image]    :
		-c,--create 		: crate a new image
		-w,--width  <number>	: image width
		-h,--height <number>	: image height
		-b,--background <R,G,B> : image background color in RGB
		<width, height, background are optional>
	*[Capture A Screenshot]     :
		-s,--screenshot		: capture a screenshot
		-d,--delay		: time before capturing the screenshot
		<delay is optional>
	*[Output Options]:
		-o,--output <name> : the name of the saved edited image
		<output is optional>
Examples:
	~ ./img_editor.py -i some_img.jpg
	~ ./img_editor.py -s
	~ ./img_editor.py -s -d 4
	~ ./img_editor.py -c
	~ ./img_editor.py -c --width 600 -h 500 -b 234,124,65
''')

if len(argv)==1:
	usage()
	exit(0)
try:
	opts, args = getopt.gnu_getopt(argv[1:], 'cb:w:h:i:sd:o:',['create','background=','width=','height=','image=','screen','delay=','output='])
except:
	usage()
	exit(0)

font = cv.FONT_HERSHEY_COMPLEX
arg_action=""
dict_opts=dict(opts)
img_width=640
height=660
bg_color=(0,0,0)
clr=0
width=5
color=(0,0,255)
name="img.png"
img_action="no"
start_point=0
end_point=0
draw_mode=0
delay=1
colors=''' Choose a color :
	red   : r
	green : g
	yellow: y
	white : w
	aqua  : a
	orange: o
	pink  : p
	black : bk
	blue  : bl'''
modes=''' Modes/Options Keys : 
 [You Should Click On The Image's Window To Be Able To Use These Keys Bindings]
	rectangle : r
	line 	  : l
	draw      : d
	text      : t
	circle 	  : ci
	crop      : cr
	color     : co
	width     : [1-9]
	save      : s
	no mode   : n
	help      : h
	exit      : esc
	print mode  : m
	print width : w'''


if "-o" in dict_opts or "--output" in dict_opts:
	if "-o" in dict_opts:
		name=dict_opts["-o"]
	elif "--output" in dict_opts:
		name=dict_opts["--output"]

if "-c" in dict_opts or "--create" in dict_opts:
	arg_action='create'
elif "-s" in dict_opts or "--screenshot"in dict_opts:
	arg_action='screen'
else:
	arg_action='image'

if arg_action=="create":
	if "-w" in dict_opts:
		img_width=int(dict_opts["-w"])
	elif "--width" in dict_opts:
		img_width=int(dict_opts["--width"])
	if "-h" in dict_opts:
		height=int(dict_opts["-h"])
	elif "--height" in dict_opts:
		height=int(dict_opts["--height"])
	if "-b" in dict_opts:
		bg_color=tuple([int(x) for x in dict_opts["-b"].split(",")])
	elif "--background" in dict_opts:
		bg_color=tuple([int(x) for x in dict_opts["--background"].split(",")])
		#np.unit8 ==> 8-bit unsigned integer (0 to 255).
	img = np.full((height,img_width,3),bg_color[::-1],np.uint8)
elif arg_action=="screen":
	if "-d" in dict_opts:
		delay=int(dict_opts["-d"])
	elif "--delay" in dict_opts:
		delay=int(dict_opts["--delay"])
	sleep(delay)
	with mss() as sct:
		screen=sct.grab(sct.monitors[0])
	img=np.array(screen,np.uint8)
elif arg_action=="image":
	if "-i" in dict_opts :
		print("i")
		img = cv.imread(dict_opts["-i"])
	elif "--image" in dict_opts:
		img = cv.imread(dict_opts["--image"])

def events(event, x,y,flags,param):
	global 	start_point,end_point,draw_mode
	if event == cv.EVENT_LBUTTONDOWN:
		start_point=(x,y)
		if img_action!="":
			cv.circle(img,start_point,1,color[::-1],1,8)
		if img_action=="text":
			text(x,y)
		elif img_action=="draw":
			draw_mode=1
	elif event == cv.EVENT_LBUTTONUP:
		draw_mode=0
		end_point=(x,y)
		if img_action=="rect":
			d_rect(start_point,end_point)
		elif img_action=="circle":
			d_circle(start_point,end_point)
		elif img_action=="line":
			d_line(start_point,end_point)
		elif img_action=="crop":
			crop(start_point,end_point)
	elif event == cv.EVENT_MOUSEMOVE and draw_mode:
		cv.circle(img,(x,y),width,color[::-1],-1,8)

def d_rect(start_point,end_point):
	cv.rectangle(img, start_point,end_point, color[::-1],width, cv.LINE_AA)
from math import sqrt
def d_circle(start_point,end_point):
	d=((end_point[0]-start_point[0])**2+(end_point[1]-start_point[1])**2)**.5
	cv.circle(img,start_point,round(d),color[::-1],width,8)

def d_line(start_point,end_point):
	cv.line(img, start_point, end_point, color[::-1], width, cv.LINE_AA)

def crop(start_point,end_point):
	global img
	if start_point[1]<=end_point[1]:
		start_y=start_point[1]
		end_y=end_point[1]
	else:
		end_y=start_point[1]
		start_y=end_point[1]
	if start_point[0]<=end_point[0]:
		start_x=start_point[0]
		end_x=end_point[0]
	else:
		end_x=start_point[0]
		start_x=end_point[0]
	img=img[start_y:end_y, start_x:end_x]

def text(x,y):
	i = 0
	cap=0
	k=""
	print("* text field : started ,press [esc] after finishing")
	while True:
		k = cv.waitKey(0)
		if k == 27:
			break
		elif k in [225,226]:
			k = cv2.waitKey(0)-32
		elif k is 229:
			cap = not cap
			k = 0
		elif k is 13:
			y+=68
			i = 0
			k = 0
		elif k is 8:
			print(color)
			cv.rectangle(img, (x+i-42,y-48),(x+i+20,y+20),bg_color[::-1], -1, 8)
			k=0
			i-=80
		if cap :
			k = k-32
		try:
			cv.putText(img, chr(k) , (x+i,y), font,1.5, color, width*2, cv.LINE_AA)
			cv.putText(img, chr(k) , (x+i,y), font,1.5, color[::-1],width , cv.LINE_AA)
			i+=40
		except:
			i+=40
		cv.imshow('image',img)
	print("* text field : canceled.")

def save():
	cv.imwrite(name,img)
	print(">> saved as",name)

cv.imshow('image',img)
cv.setMouseCallback('image',events)

undo_crop=img
while True:
	cv.imshow('image',img)
	k=cv.waitKey(1)
	if not clr: 
		pf=platform
		print(pf)
		if pf.lower() == "linux":
			call('clear',shell=True)
		elif pf.lower() == "windows":
			call('cls',shell=True)
		clr=1
		print(modes)
	if k == 27:
		img_action=""
		print(">>> Do You Want To Save The Image? [y|n]")
		k=cv.waitKey(0)
		if k==ord("y"):
			save()
		break
	elif k == 99:#c
		k = cv.waitKey(0)
		if k==105:
			img_action="circle"
			print(">> mode : {} mode ".format(img_action))
		elif k==114:
			img_action="crop"
			print(">> mode : {} mode ".format(img_action))
		elif k==111:
			print(colors)
			k=cv.waitKey(0)
			if k==114:
				color=(255,0,0)
			elif k==103:
				color=(0,255,0)
			elif k==121:
				color=(0, 255, 255)
			elif k==119:
				color=(255,255,255)
			elif k==111:
				color=(255,69,0)
			elif k==ord("a"):
				color=(255,255,0)
			elif k==ord("p"):
				color=(255, 0, 255)
			elif k==98:
				k=cv.waitKey(0)
				if k==107:#k
					color=(0,0,0)
				elif k==108:#l
					color=(0,0,255)
			else:print(">Unknown Color !")
			print(">> color(RGB)_ = {} ".format(color))
		else:print(">Unknown Command !")
	elif k == 108:
		img_action="line"
		print(">> mode : {} mode ".format(img_action))
	elif k == 114:
		img_action="rect"
		print(">> mode : {} mode ".format(img_action))
	elif k == 100:
		img_action="draw"
		print(">> mode : {} mode ".format(img_action))
	elif k == 116:
		img_action="text"
		print(">> mode : {} mode ".format(img_action))
	elif k in [ord(str(x)) for x in range(1,10)]:
		width=int(chr(k))
		print(">> width = {} ".format(width))
	elif k == 115:
		save()
	elif k == ord('n'):
		img_action=""
		print(">> mode : no mode")
	elif k == ord('u'):
		img=undo_crop
		print(">> crop undone")
	elif k == ord('h'):
		print(modes)
	elif k == ord('w'):
		print(">> width = {} ".format(width))
	elif k == ord('m'):
		print(">> mode : {} mode ".format(img_action))
cv.destroyAllWindows()
