from tkinter import *
from tkinter import ttk
from tkinter import filedialog

if __name__ == "__main__":
    win = Tk()
    win.geometry("720x450") #window size
    def selectFile():
        path= filedialog.askopenfilename(title="Select a File", filetype=(('text files''*.txt'),('all files','*.*')))
        Label(win, text=path, font=13).pack()
    
    Label(win, text="Click the Button to Select a File", font=('Aerial 18 bold')).pack(pady=20)
    
    button= ttk.Button(win, text="Select", command= selectFile)
    button.pack(ipadx=5, pady=15)
    
    win.mainloop()