from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Menu, Canvas
from PIL import Image, ImageTk
import Window1
import Window3
import profile


try:

    def Signout():
        wind2.destroy()
        Window1.firstWindow()

    def showimage():
        wind2.destroy()
        Window3.thirdWindow()

    def showprofile():
        wind2.destroy()
        profile.fourWindow()

    def secondWindow():
        global wind2
        wind2 = Tk()

        # ***** IAMFES *****
        # ***** FIRST IAMFES *****
        for x in range(4):
            logo= Image.open("logo.png")

            #RESIZE
            logo_resize = logo.resize((100,100), Image.ANTIALIAS)

            logo= ImageTk.PhotoImage(logo_resize)

            my_logo= Label(wind2, image=logo)
            my_logo.place(x=160*x,y=10)
            Label(wind2,text="SHAREPHOTO APP", font=('Helvetica',15), fg="black",bg="white").place(x=100*x, y=120)


        # ***** FOUR IAMFES *****
        
        


        # ***** Variables *****
        text = StringVar()  # work signin or no #LAbel
        global FirstName, SecondName, Email, vr, FirstNameEn, SecondNameEn, EmailEn
        FirstName = StringVar()
        SecondName = StringVar()
        Email = StringVar()
        cc = IntVar()
        vr = IntVar()  # vr = variable radiobutton

        # ***** Label *****
        Label(wind2,text="Share Photo App", font=70, fg="black",bg="white").place(x=250, y=20)






        # ***** Button *****
        b1 = Button(wind2, text="Profile", bg="CornflowerBlue", width=8, fg="black", bd=0.5, font=0.5,activeforeground="black", activebackground="blue",command=showprofile)
        b1.place(x=830, y=580)
        b2 = Button(wind2, text="Sign-out", bg="brown", width=8, fg="black", bd=0.5, font=0.5,activeforeground="darkblue", activebackground="red",command=Signout)
        b2.place(x=900, y=580)
        b3 = Button(wind2, text="Add", bg="CornflowerBlue", width=8, fg="black", bd=0.5, font=0.5,activeforeground="black", activebackground="blue",command=showimage)
        b3.place(x=755, y=580)
        

        # ***** Main *****
        wind2.title("HOME")
        wind2.geometry("1000x1000")
        wind2['bg']="white"
        wind2.mainloop()

except Exception as e:
        print("Error ", e)