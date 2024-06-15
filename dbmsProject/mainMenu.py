from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import sqlite3
from database import *
from enquiry_menu import *
from artists_menu import *
from galleryMenu import *
from arts import *
from exhibit import *

def main():
    root = Tk()
    app= Menu(root)
conn=sqlite3.connect("Virtual_ART_GALLERY.db")

print("DATABASE CONNECTION SUCCESSFUL")

  
class Menu:
    def __init__(self,master):
        self.master = master
        self.master.title("Art Galary")
        self.master.geometry("800x600+0+0")
        self.master.config(bg="#778899")
        self.frame = Frame(self.master,bg="#778899")
        self.frame.pack()
       
        self.lblTitle = Label(self.frame,text = "Welcome to our Galary", font="Helvetica 20 bold",bg="#778899")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="#EED5B7",bd=20)
        self.LoginFrame.grid(row=1,column=0)
    
        self.button1 = Button(self.LoginFrame,text = "Gallery Menu", width =30,font="Helvetica 14 bold",bg="#EED5B7",command=self.gallery)       
        self.button1.grid(row=1,column=0,pady=10)
        
        self.button2 = Button(self.LoginFrame, text="Enquiry Menu",width =30,font="Helvetica 14 bold",bg="#EED5B7",command=self.ask)
        self.button2.grid(row=2,column=0,pady=10)
        
        self.button3 = Button(self.LoginFrame, text="Artist Menu",width =30,font="Helvetica 14 bold",bg="#EED5B7",command=self.arti)
        self.button3.grid(row=3,column=0,pady=10)
    
        self.button4 = Button(self.LoginFrame, text="Art Menu",width =30,font="Helvetica 14 bold",bg="#EED5B7",command=self.artsy)
        self.button4.grid(row=4,column=0,pady=10)
        
        self.button5 = Button(self.LoginFrame, text="Exhibition Menu",width =30,font="Helvetica 14 bold",bg="#EED5B7",command=self.exhi)
        self.button5.grid(row=5,column=0,pady=10)
        
        self.button6 = Button(self.LoginFrame, text="EXIT",width =30,font="Helvetica 14 bold",bg="#EED5B7",command = self.Exit)
        self.button6.grid(row=6,column=0,pady=10)
        
   
    def Exit(self):
        self.master.destroy()

      
    def gallery(self):
        self.newWindow = Toplevel(self.master)
        self.app = Gallery(self.newWindow)
          

    def ask(self):
        self.newWindow = Toplevel(self.master)
        self.app = Enquiry(self.newWindow)

    def arti(self):
        self.newWindow = Toplevel(self.master)
        self.app = Artist(self.newWindow)

    def artsy(self):
        self.newWindow = Toplevel(self.master)
        self.app = Artwork(self.newWindow)

    def exhi(self):
        self.newWindow = Toplevel(self.master)
        self.app = Exhibition(self.newWindow)
        
if __name__ == "__main__":
    main()    
