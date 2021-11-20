from tkinter import *
from PIL import ImageTk
import os

def selection3():
    os.system('demo.py')
    print("demo")

def selection4():
    os.system('ChessMain.py')
    print("demo1")


class Login:
    def _init_(self,root):
        self.root = root
        self.root.title("WELCOME IN OUR GAMEZONE")
        self.root.geometry("1199x850+100+50")

        # Background Image
        self.im1= ImageTk.PhotoImage(file="CARss1.jpg")
        self.im1_Image = Label(self.root, image=self.im1).place(x=230, y=200)

        self.im = ImageTk.PhotoImage(file='2ndf1.jpg')
        self.im_Image = Label(self.root, image=self.im).place(x=700, y=200 )

        Submit = Button(self.root, cursor="hand2", text="BRAIN RUNNING",command=selection4, bd=0, font=("Goudy old style", 15, "bold"), bg="#bf00ff",
                        fg="white").place(x=750, y=590, width=259, height=50)

        Submit = Button(self.root, cursor="hand2", text="JOYRIDE", command=selection3, bd=0, font=("Goudy old style", 15, "bold"),
                        bg="#bf00ff",
                        fg="white").place(x=270, y=590, width=259, height=50)

root = Tk()
obj = Login(root)
root.mainloop()