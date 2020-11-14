# -*- coding: utf-8 -*-
'''
	Press Esc to quit, press q to quit from fullscreen
'''
from tkinter import *
from tkinter import font
from PIL import Image
import os
import random
import time
import xlsxwriter
from datetime import datetime, date
import pyaudio
import numpy as np

#create screen and get screen info
screen = Tk()
w, h = screen.winfo_screenwidth(), screen.winfo_screenheight()

#vectors that images' infos are stored
fa1s = []
fa2s = []
fa3s = []
fa4s = []

#vector that possible correct button responses will be stored
correct_resp_imgs = []

#variables for excel workbook
workbook = None
row = 0
column = 0
file = None

#vector which will store answers and reaction times
answers = []
rts = []

#number of trials, which is used in clean_write() function
count = 0

#reaction time initilization
start_time = 0

#sound
p = pyaudio.PyAudio()

#initiliaze index for selected images in phase2()
i = 0

#FUNCTIONS------------------------------------------------------------------------------------

#Screen Functions

def open_screen():
	global screen

	screen.attributes("-fullscreen", True)
	screen.bind("<Escape>", exit)
	screen.bind("<q>", exitfullscreen)

def exitfullscreen():
	global screen

	screen.attributes("-fullscreen", False)

#Sound Functions
def create_sound(f):
	'''f is sine frequency'''
	volume = 0.5
	fs = 44100  # sampling rate, Hz, must be integer
	duration = 1.0   # in seconds, may be float
	# generate samples, note conversion to float32 array
	samples = (np.sin(2 * np.pi * np.arange(fs * duration) * f / fs)).astype(np.float32)

	# for paFloat32 sample values must be in range [-1.0, 1.0]
	stream = p.open(format = pyaudio.paFloat32, channels = 1, rate = fs, output = True)

	# play. May repeat with different volume values (if done interactively) 
	stream.write(volume * samples)

#Excel Functions

def open_output_file(name):
	global workbook

	workbook = xlsxwriter.Workbook(name)
	worksheet = workbook.add_worksheet("results_withFeedback")
	worksheet.write(row, column, 'Answer')
	next_column()
	worksheet.write(row, column, 'ReactionTime')

	return worksheet

def next_row():
	global column
	global row

	column = 0
	row += 1

def next_column():
	global column

	column += 1

def close_output_file():
	global workbook

	workbook.close()

#PHASE-1 Functions

def fa1_generator(n):
	'''Creates random fa1 image. n = number of images'''
	global fa1s

	for i in range(n):
		randomfa1 = random.choice(os.listdir("C:\\Users\\Lenovo\\Desktop\\learningexp\\Fa1"))
		fa1s.append(randomfa1)
	
	return fa1s


def phase1(seconds, n):
	'''Creates fa1 fullscreen display which will be shown to participant for given seconds
	Then, cleans the display from the screen
	n = number of trials
	'''
	global w, h, screen

	fa1_disp_dirs = fa1_generator(n)  
	i = random.randint(0, (n))

	#resize fa1 image as fullscreen
	display =Image.open("C:\\Users\\Lenovo\\Desktop\\learningexp\\Fa1" + "\\" + fa1_disp_dirs[i])
	display = display.resize((w, h), Image.ANTIALIAS)
	display.save("display1.ppm", "ppm")
	disp = PhotoImage(file = "display1.ppm")
	#create fullscreen button for fa1 image
	buttondisp = Button(screen, width = w, height = h)
	buttondisp.config(image = disp)
	buttondisp.image = disp
	#place it to center
	buttondisp.place(relx = 0.5, rely = 0.5, anchor = CENTER)

	screen.update()
	time.sleep(seconds)
	buttondisp.destroy()

#PHASE-2 Functions

#-----Button functions:

def fa2_generator(n):
	'''Creates random fa2 image. n = number of images'''
	global fa2s

	for i in range(n):
		randomfa2 = random.choice(os.listdir("C:\\Users\\Lenovo\\Desktop\\learningexp\\Fa2"))
		fa2s.append(randomfa2)
	
	return fa2s

def fa3_generator(n):
	'''Creates random fa3 image. n = number of images'''
	global fa3s

	for i in range(n):
		randomfa3 = random.choice(os.listdir("C:\\Users\\Lenovo\\Desktop\\learningexp\\Fa3"))
		fa3s.append(randomfa3)

	return fa3s

def fa4_generator(n):
	'''Creates random fa4 image. n = number of images'''
	global fa4s

	for i in range(n):
		randomfa4 = random.choice(os.listdir("C:\\Users\\Lenovo\\Desktop\\learningexp\\Fa4"))
		fa4s.append(randomfa4)

	return fa4s

def img_open(v, i):
	'''opens image from given vector v with index i from the dir "C:\\Users\\Lenovo\\Desktop\\learningexp\\FAs" . 
	e.g.; v[i]
	'''
	img = Image.open("C:\\Users\\Lenovo\\Desktop\\learningexp\\FAs" + "\\" + v[i])
	return img

def img_resize(img):
	'''Resizes given image img  to size 200x300'''
	imag = img.resize((200, 300), Image.ANTIALIAS)
	return imag    

def img_save(img):
	'''Saves given image img as "img.ppm"
	It turns image into ppm format to avoid troubles that python can create'''
	img.save("img.ppm", "ppm")

def photo_img(img):
	'''Converts image.ppm to photoimage for button'''
	img = PhotoImage(file = "img.ppm")
	return img
		
def create_button(img, x, y, image):
	'''img = image input
	x and y = button place coordinants
	'''
	global screen, worksheet
	
	img = img_resize(img)
	img_save(img)
	img = photo_img(img)

	button = Button(screen, width = 200, height = 300,  command = lambda: [get_resp(image),clean_write()])
	button.config(image = img)
	button.image = img
	button.place(relx = x, rely = y, anchor = CENTER)
		
					  
def create_text(textt, relx, rely, font):
	t = Label(text = textt, fg = "black", font = font)
	t.place(relx = relx, rely = rely, anchor = NW)

def phase2(n, i):
	'''Asks participants to which of the 4 choices belongs to the same family with the display that is shown in phase1.
	n = number of trials
	'''
	global correct_resp_imgs, file, feedbback_ind, start_time
	
	start_time = datetime.now()

	fa1s = fa1_generator(n)
	fa2s = fa2_generator(n)
	fa3s = fa3_generator(n)
	fa4s = fa4_generator(n)
	

	for j in range(n):
		correct_img = img_open(fa1s, j)
		correct_resp_imgs.append(correct_img)
	
	random.shuffle(correct_resp_imgs)

	create_text("Aşağıdaki görsellerden hangisi az önce gördüğünüz görsel ile aynı aileye aittir?", 0.05, 0.01, "Times 18 bold")
	img1 = correct_resp_imgs[i]
	img2 = img_open(fa2s, i)
	img3 = img_open(fa3s, i)
	img4 = img_open(fa4s, i)
				
	images = [img1, img2, img3, img4]
	random.shuffle(images)
	feedbback_ind = images.index(img1)
		
	x = 0.7
	y = 0.5

	for img in images:
			button = create_button(img, x, y, img)
			x = x - 0.2
	
#---Button command functions
def get_resp(img):
	'''Gets clicked image as response and saves it to an excel file'''
	global answers

	if img in correct_resp_imgs:
		create_sound(4000)
		answers.append("True")
	else:
		create_sound(400)
		answers.append("False")


def clean_write():
	'''Cleans the screen and opens new trial. Then, writes the data to an excel file.
	Count is the number of trials'''

	global count, screen, file, row, column, rts, i


	tdelta = datetime.now() - start_time
	rt = tdelta.total_seconds()
	rts.append(rt)

	for child in screen.winfo_children():
		child.destroy()
	
	phase1(0.3, 16)
	phase2(16, i)
	count += 1
	i += 1

	
	if count > 4:
		file = open_output_file("deneme" + ".xlsx")
		for i in range(len(answers)):
			next_row()
			file.write(row, column, answers[i])
			next_column()
			file.write(row, column, rts[i])
		close_output_file()

		screen.destroy()


#EXPERIMENT--------------------------------------------------------------------------------
if __name__ == '__main__':

	open_screen()

	phase1(0.3, 16)
	phase2(16, 1)


