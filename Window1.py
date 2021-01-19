
from tkinter import *
from tkinter import messagebox

import Window2
import Window3

#  ***** functions *****
def SigninButton():
    Email.set(Email.get().strip())
    if Email.get()=="admin" and Password.get()=="admin" :
        wind1.destroy()
        Window2.secondWindow()
    if Email.get()=="khaled" and Password.get()=="khaled" :
        wind1.destroy()
        Window3.thirdWindow()
    else :
        Label(wind1,text="wrong",fg="red",bg='#49A').place(x=290,y=350)

def cancelButton():
    messagebox.showwarning("Alert", "canceled")
    wind1.destroy()

def firstWindow():
    global wind1
    wind1 = Tk()
    wind1.title("Login_in")
    wind1.geometry("420x390+500+150")

    # ***** Variables *****
    global Email, Password
    Email = StringVar()
    Password = StringVar()

   

    
    
   
 

    #  ***** Labels *****
    Label(wind1,text="Sign-In ",font=15, fg="black",bg="white").place(x=10,y=40)
    Label(wind1,text="Password",font=15, fg="black",bg="white").place(x=10,y=100)


    # ***** Entry *****
    name = Entry(wind1,font= 20,textvariable=Email)
    name.place(x=90,y=40,height=22,width=180)
    name.focus()
    Entry(wind1,textvariable=Password,font= 20,justify=CENTER,show='*').place(x=90,y=100,height=22,width=180)

    #  ***** Buttons *****
    Signin = Button(wind1,text="Sign in",width=8,fg="black",bd=0.5,font=0.5,activeforeground="black",activebackground="blue",command=SigninButton)
    Signin.place(x=230,y=320)

    cancel = Button(wind1,text="cancel",width=8,fg="black",bd=0.5,font=0.5,activeforeground="darkblue",activebackground="red",command=cancelButton)
    cancel.place(x=330,y=320)



    # ***** Main *****
    wind1['bg'] = 'white'
    wind1.mainloop()


if __name__ == "__main__":
    firstWindow()

