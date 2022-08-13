from tkinter import *
from tkinter import ttk
from tkinter import filedialog

if __name__ == "__main__":
    win = Tk()
    win.geometry("990x450") #window size
    def selectFile():
        path= filedialog.askdirectory()
        Label(win, text=path, font=13).pack()
    
    Label(win, text="SELECT THE FOLDER INSIDE WHICH YOUR REFERENCE PAPERS ARE STORED", font=('Times 12 bold')).pack(pady=20)
    
    button= ttk.Button(win, text="BROWSE", command= selectFile)
    button.pack(ipadx=5, pady=15)
    
    win.mainloop()