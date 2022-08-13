from fileinput import filename
from importlib.resources import path
from tkinter import *
import tkinter.font as font
from tkinter import ttk
from tkinter import filedialog

def selectFile():
    global filename
    filename = filedialog.askdirectory()
    Label(win, text=filename, font=('Times 15')).pack()

if __name__ == "__main__":
    win = Tk()
    win.geometry("990x450") #window size
    myPath = StringVar() #soon-to-be global var
    
    Label(win, text="Select the folder inside which your reference papers are stored", font=('Times 15')).pack(pady=50)
    custFont = font.Font(family='Times')
    button = Button(text="BROWSE",height=2,width=40, fg='white', bg='light slate grey', command=selectFile)
    button['font'] = custFont
    button.pack()
    win.mainloop()
    print(filename)