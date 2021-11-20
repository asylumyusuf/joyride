import tkinter as tk
from tkinter import*
from PIL import ImageTk  #pip
from tkinter import messagebox
import os


def msg():
    messagebox.showinfo("Password", "PASSWORD SUCCESFULLY CHANGED")

def msg1():
    messagebox.showinfo("OTP","845101")


root =Tk()
root.title("forget password")
root.geometry("650x650+100+50")
root.resizable(False, False)

def selection1():
    os.system('newlogin.py')
    print("Hi")

# Login frame
Frame_login = Frame(root, bg="#bf00ff")
Frame_login.place(x=130, y=150,width=400,height=400)

#username

lbl_use = Label(Frame_login, text="Enter valid Email/Mobile No.", font=("Goudy old style", 15, "bold"), fg="black", bg="#bf00ff").place(x=50,
                                                                                                                   y=100)
Username= Entry(Frame_login, font=("Goudy old style", 15,), bg="#E7E6E6")
Username.place(x=50,y=130,width=320, height=35)

forget= Button(Frame_login,  text="SEND OTP", bd=0,cursor="hand2",command=msg1,font=("Goudy old style", 12), fg="blue", bg="#bf00ff").place(x=50,
                                                                                                                   y=165)


lbl_use = Label(Frame_login, text="Enter OTP", font=("Goudy old style", 15), fg="black", bg="#bf00ff").place(x=50,
                                                                                                                   y=220)
Username= Entry(Frame_login, font=("Goudy old style", 15,), bg="#E7E6E6")
Username.place(x=50,y=250,width=320, height=35)
Submit = Button(Frame_login,  cursor="hand2",text="Change Password", command= msg,bd=0, font=("Goudy old style", 15, "bold"), bg="#6162FF",fg="white").place(x=170, y=310,width=180,height=40)

Submit = Button(Frame_login,  cursor="hand2", text="BACK",command=selection1, bd=0, font=("Goudy old style", 15, "bold"), bg="#6162FF",fg="white").place(x=75, y=310,width=80,height=40)


root.mainloop()