import DFimport
import tkinter.font as font


from tkinter import *
from tkinter import filedialog


def selectFile():
    global pathName
    pathName = filedialog.askdirectory()
    Label(win, text=pathName, font=('Times 15')).pack()

def finishTask():
    print("IT IS DONE")

def showButton():
    finishButton = Button( text="FINISH", height=2,width=8, fg='white', bg='green', bd=3, relief=GROOVE, activebackground='forest green', command=finishTask)
    finishButton['font'] = custFont
    finishButton.pack(pady=(170, 0))

if __name__ == "__main__":
    win = Tk()
    win.geometry("990x450") #window size
    win["bg"] = "cornsilk"
    
    Label(win, text="Select the folder inside which your reference papers are stored", font=('Times 15'), bg='cornsilk').pack(pady=50)
    custFont = font.Font(family='Times')
    
    button = Button(text="BROWSE",height=2,width=40, fg='white', bg='light slate grey', command=selectFile)
    button['font'] = custFont
    button.pack()

    win.mainloop()
    DFimport.dfImport(pathName)