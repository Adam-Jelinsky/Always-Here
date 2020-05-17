import tkinter as tk
import cv2
import os

NAMEPATH = "./facedata/names.txt"

def save_name(name, filepath):
	namesdata = open(NAMEPATH,"r")
	if name+'\n'not in namesdata.readlines():
		namesfa = open(NAMEPATH,"a")
		facedata = namesfa.writelines([name+'\n',filepath+'\n'])

def createRegMenu():
	regmenu = tk.Tk()
	regmenu.title("Register Your Face")
	tk.Label(regmenu, text = "Enter Your Name: ").grid(row = 0)
	e1 = tk.Entry(regmenu)
	e1.grid(row = 0, column = 1)
	def onReturn(event):
		name = e1.get()
		name = name.replace(" ", "")
		video_capture = cv2.VideoCapture(0)
		ret, frame = video_capture.read()
		outpath = "./facedata/" + name + ".jpg"
		cv2.imwrite(outpath, frame)
		save_name(name,outpath)
		video_capture.release()
		regmenu.destroy()
		return
	e1.bind("<Return>",onReturn)
	regmenu.mainloop()


root = tk.Tk()
	
root.minsize(width=960,height=720)
root.maxsize(width=960,height=720)

root.title("")

root.resizable(width=False,height=False)

bkimg = tk.PhotoImage(file="./graphics/menu.png")
bkgrd = tk.Label(image=bkimg)
bkgrd.place(x=0,y=0)

def clicked(event):
    x, y = event.x, event.y
    if 95 < x and x < 452:
    	if 179 < y and y < 280:
    		#start button code here
    		print("start")
    		root.destroy()
    		exec(open("facerec.py").read())
    		exit()
    	if 289 < y and y < 395:
    		#settings button code here
    		print("settings")
    	if 409 < y and y < 504:
    		#register button code here
    		createRegMenu()
    		print("register")


root.bind('<1>', clicked)

root.mainloop()

