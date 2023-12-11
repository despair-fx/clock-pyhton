from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock - despir-fx")

def time():
    string = strftime("%I:%M:%S %p")
    label.config(text = string)
    label.after(1000, time)

label = Label(root, font = ("Product Sans",75), background = "black", foreground = "white")
label.pack(anchor = "center")

time()

mainloop()
