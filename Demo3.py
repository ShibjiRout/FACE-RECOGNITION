from tkinter import *
from tkinter import messagebox
import cv2
import numpy as np
import os
from PIL import Image,ImageTk
import csv
import demo1 as d1
import main1 as m1


window = Tk()

window.title("FACE REOGNITION BASED ATTENDANCE SYSTEM")

l1 = Label(window,text = "FACE REOGNITION BASED ATTENDANCE SYSTEM",font = ('Algerian',20),bg='cyan')
l1.grid(column =1,row =0)



l2= Label(window,text = "Government College of Engineering, Keonjhar",font = ('times new roman',20),bg='cyan')
l2.grid(column =1,row =1)


b1= Button(window,text = "SIGN UP",font=('times new roman',15,'bold'),bg='dark turquoise',fg='black',command = d1.fst)
b1.grid(column = 1 ,row = 3)
l2= Label(window,text = "To Take Attendance Please Click START",font = ('times new roman',10),bg='cyan')
l2.grid(column =1,row =4)

l2= Label(window,text = "After Attendance Please Click 'q' !!!",font = ('times new roman',10),bg='cyan',fg='red')
l2.grid(column =1,row =6)


########################################################################################################################




b2= Button(window,text = "START",font=('times new roman',15,'bold'),bg='dark turquoise',fg='black',command = m1.detect)
b2.grid(column = 1 ,row = 5)



window.geometry('610x250')
window.configure(bg='cyan')
window.mainloop()