import tkinter as tk
import cv2

NAMEPATH = "./facedata/names.txt"

def save_name(name, filepath):
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
		exit()
	e1.bind("<Return>",onReturn)
	regmenu.mainloop()

