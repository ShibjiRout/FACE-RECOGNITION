from tkinter import *
from tkinter import messagebox
import cv2
import numpy as np
import os
from PIL import Image,ImageTk
import csv


def fst():
    window = Tk()

    window.title("FACE REOGNITION BASED ATTENDANCE SYSTEM")

    l1 = Label(window, text="Name", font=('Algerian', 20), bg='skyblue')
    l1.grid(column=0, row=0)
    t1 = Entry(window, width=50, bd=5)
    t1.grid(column=1, row=0)

    l2 = Label(window, text="REDG.NO.", font=('Algerian', 20), bg='skyblue')
    l2.grid(column=0, row=1)
    t2 = Entry(window, width=50, bd=5)
    t2.grid(column=1, row=1)

    l3 = Label(window, text="MAIL ID", font=('Algerian', 20), bg='skyblue')
    l3.grid(column=0, row=2)
    t3 = Entry(window, width=50, bd=5)
    t3.grid(column=1, row=2)

    l4 = Label(window, text="UNIQUE ID", font=('Algerian', 20), bg='skyblue')
    l4.grid(column=0, row=3)
    t4 = Entry(window, width=50, bd=5)
    t4.grid(column=1, row=3)

    #####################################################################################################################
    def click():
        messagebox.showinfo("Result", "Click 'Space Bar' to save  picture and 'q' to exit")
        numCascade1 = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        cam = cv2.VideoCapture(0)

        while True:
            ret, img = cam.read()
            imgResize = img
            imgGray = cv2.cvtColor(imgResize, cv2.COLOR_BGR2GRAY)
            face = numCascade1.detectMultiScale(imgGray, 1.1, 5)
            for (x, y, w, h) in face:
                area = w * h
                if area > 50:
                    imgROI = imgResize[y:y + h, x:x + w]
                cv2.imshow("Test", imgROI)

                if not ret:
                    break

            k = cv2.waitKey(1)

            if cv2.waitKey(27) == ord('q'):
                break
            elif k % 256 == 32:
                    file = 'Training_images/' + t4.get() + '.jpg'
                    cv2.imwrite(file, imgROI)
                    messagebox.showinfo("Result", "Image Saved !!!")

        '''cam.release
        cv2.destroyAllWindows'''

    b1 = Button(window, text="Take Picture", font=('times new roman', 15, 'bold'), bg='skyblue', fg='black',
                command=click)
    b1.grid(column=1, row=4)

    ######################################################################################################################
    def save():
        if (t1.get() == '' or t2.get() == '' or t3.get() == '' or t4.get() == ''):
            messagebox.showinfo("Result", "Please Provide Complete Imformation!!!")
        else:
            with open('data.csv', 'r+') as dt:
                rd = dt.readline()
                dt.writelines(f'\n{t1.get()},{t2.get()},{t3.get()},{t4.get()}')
            messagebox.showinfo("Result", "Data Saved !!!")

    b2 = Button(window, text="SAVE", font=('times new roman', 15, 'bold'), bg='skyblue', fg='black', command=save)
    b2.grid(column=0, row=4)
    #######################################################################################################################

    window.geometry('500x250')
    window.configure(bg='skyblue')
    window.mainloop()
