import tkinter as tk
from tkinter import*
from PIL import ImageTk  #pip

import os


root =Tk()
root.title("Login System")
root.geometry("1199x650+100+50")
root.resizable(False, False)

def selection():
    os.system('pyhame.py')
    print("Hit")

def selection2():
    os.system('loginpage.py')
    print("H")


#Background Image
bg=ImageTk.PhotoImage(file="images.jpg")
bg_image=Label(root, image= bg).place(x=0,y=0, relwidth=1, relheight=1)


# Login frame
Frame_login = Frame(root, bg="white")
Frame_login.place(x=330, y=150,width=500,height=400)



#Title &subtitle
title = Label(Frame_login, text="Login Here", font=("Impact",35,"bold"), fg="#6162FF", bg="white").place(x=90, y=30)
subtitle = Label(Frame_login, text="member login Area", font=("Goudy old style", 15, "bold"), fg="#1d1d1d", bg="white").place(x=90,
                                                                                                                   y=100)
          #username
lbl_use = Label(Frame_login, text="Username", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(x=90,
                                                                                                                   y=140)
Username= Entry(Frame_login, font=("Goudy old style", 15,), bg="#E7E6E6")
Username.place(x=90,y=170,width=320, height=35)


#Password
lbl_Password = Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(x=90, y=210)
Password = Entry(Frame_login, show='*',font=("Goudy old style", 15,), bg="#E7E6E6")
Password.place(x=90, y=240, width=320, height=35)



          #button
forget= Button(Frame_login,  text="Forget password?",command=selection2, bd=0,cursor="hand2",font=("Goudy old style", 12), fg="#6162FF", bg="white").place(x=90,
                                                                                                                   y=280)
Submit = Button(Frame_login, command=selection,  cursor="hand2", text="login", bd=0, font=("Goudy old style", 15), bg="#6162FF",fg="white").place(x=90, y=340,width=180,height=40)

root.mainloop()