from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import Window2
import Window1

try:

    def home():
        wind4.destroy()
        Window2.secondWindow()

    def Signout():
        wind4.destroy()
        Window1.firstWindow()

    def fourWindow():
        global wind4
        wind4 = Tk()

        Label(wind4,text="Profile",font=('Helvetica',15), fg="black",bg="white").place(x=500,y=10)
        # OPEN IMAGE
        logo= Image.open("Blank-profile.png")

        #RESIZE
        logo_resize = logo.resize((100,100), Image.ANTIALIAS)

        logo= ImageTk.PhotoImage(logo_resize)

        my_logo= Label(wind4, image=logo,bg="white")
        my_logo.place(x=10,y=100)
        Label(wind4,text="NAME ", font=('Helvetica',15), fg="black",bg="white").place(x=130, y=130)


        Label(wind4,text="MY PHOTO ", font=('Helvetica',15), fg="black",bg="white").place(x=50, y=250)

        # ***** IAMFES *****
        # **************fisrt iamge**************
        img1= Image.open("jo.png")
        #RESIZE
        img1_resize = img1.resize((100,100), Image.ANTIALIAS)
        img1= ImageTk.PhotoImage(img1_resize)
        my_img1= Label(wind4, image=img1)
        my_img1.place(x=50,y=300)

        # **************socend iamge**************
        img2= Image.open("jo.png")
        #RESIZE
        img2_resize = img2.resize((100,100), Image.ANTIALIAS)
        img2= ImageTk.PhotoImage(img2_resize)
        my_img2= Label(wind4, image=img2)
        my_img2.place(x=180,y=300)

        # **************third iamge**************
        img3= Image.open("jo.png")
        #RESIZE
        img3_resize = img3.resize((100,100), Image.ANTIALIAS)
        img3= ImageTk.PhotoImage(img3_resize)
        my_img3= Label(wind4, image=img3)
        my_img3.place(x=310,y=300)

        # **************four iamge**************
        img4= Image.open("jo.png")
        #RESIZE
        img4_resize = img4.resize((100,100), Image.ANTIALIAS)
        img4= ImageTk.PhotoImage(img4_resize)
        my_img4= Label(wind4, image=img4)
        my_img4.place(x=440,y=300)

        # **************five iamge**************
        img5= Image.open("jo.png")
        #RESIZE
        img5_resize = img5.resize((100,100), Image.ANTIALIAS)
        img5= ImageTk.PhotoImage(img5_resize)
        my_img5= Label(wind4, image=img5)
        my_img5.place(x=570,y=300)

        # **************six iamge**************
        img6= Image.open("jo.png")
        #RESIZE
        img6_resize = img6.resize((100,100), Image.ANTIALIAS)
        img6= ImageTk.PhotoImage(img6_resize)
        my_img6= Label(wind4, image=img6)
        my_img6.place(x=700,y=300)
    

        b3 = Button(wind4, text="HOME", bg="CornflowerBlue", width=8, fg="black", bd=0.5, font=0.5,activeforeground="black", activebackground="blue",command=home)
        b3.place(x=430, y=600)
        
        b2 = Button(wind4, text="SIGNOUT", bg="brown", width=8, fg="black", bd=0.5, font=0.5,activeforeground="darkblue", activebackground="red",command=Signout)
        b2.place(x=530, y=600)

        # ***** Main *****
        wind4.title("Profile")
        wind4.geometry("1000x1000")
        wind4['bg']="white"
        wind4.mainloop()


except Exception as e:
        print("Error ", e)