
from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Menu, Canvas
from PIL import Image, ImageTk
import Window1
import Window2


try:

    def Signout():
        wind3.destroy()
        Window2.secondWindow()

    # def loadImage():
    #     img = Image.open("KL.png")
    #     filename = ImageTk.PhotoImage(img)
    #     canvas = Canvas(wind3,height=100,width=100)
    #     canvas.image = filename  # <--- keep reference of your image
    #     canvas.create_image(0,0,anchor='nw',image=filename)
    #     canvas.place(x=20,y=20)

    #     button1 = Button(wind3, text = "LIKE", anchor = W)
    #     button1.configure(width = 5, activebackground = "#33B5E5", relief = FLAT)
    #     button1.place(x=20,y=130)
        
    #     Label(wind3,text="a7aaaa ya bshooy", font=25, fg="black",bg="white").place(x=20,y=150)

    #     # button1_window = canvas.create_window(10, 10, anchor=NW, window=button1)
    def showimage():
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="select Image File",filetypes=(("JPG file","*.jpg"),("PNG file","*.png"),("All Files","*.*")))
        img = Image.open(fln)
        img_resize = img.resize((150,150), Image.ANTIALIAS)
        img= ImageTk.PhotoImage(img_resize)
        lbl.configure(image=img)
        lbl.image=img 
        lbl.place(x=100,y=76)      

    
    def thirdWindow():
        global wind3
        wind3 = Tk()


        # ***** Variables *****
        text = StringVar()  # work signin or no #LAbel
        global FirstName, SecondName, Email, vr, FirstNameEn, SecondNameEn, EmailEn
        FirstName = StringVar()
        SecondName = StringVar()
        Email = StringVar()
        cc = IntVar()
        vr = IntVar()  # vr = variable radiobutton

        # ***** Label *****
        Label(wind3,text="ADD PHOTO", font=25, fg="black",bg="white").place(x=250, y=20)
        global lbl
        lbl=Label(wind3)
        lbl.pack()

        Label(wind3,text="Caption", font=25, fg="black",bg="white").place(x=30, y=235)
        global caption_photo
        caption_photo = StringVar()
        cap= Entry(wind3,textvariable=caption_photo)
        cap.place(x=100,y=235,height=22,width=180)

        # ***** Button *****
        b1 = Button(wind3, text="Add", bg="CornflowerBlue", width=8, fg="black", bd=0.5, font=0.5,activeforeground="black", activebackground="blue",command=showimage)
        b1.place(x=130, y=320)
        b3 = Button(wind3, text="DONE", bg="CornflowerBlue", width=8, fg="black", bd=0.5, font=0.5,activeforeground="black", activebackground="blue")
        b3.place(x=230, y=320)
        
        b2 = Button(wind3, text="BACK", bg="brown", width=8, fg="black", bd=0.5, font=0.5,activeforeground="darkblue", activebackground="red",command=Signout)
        b2.place(x=330, y=320)
        

        # ***** Main *****
        wind3.title("add")
        wind3.geometry("500x500")
        wind3['bg']="white"
        wind3.mainloop()

except Exception as e:
        print("Error ", e)