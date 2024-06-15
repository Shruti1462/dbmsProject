from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font

from mainMenu import Menu

def main():
    root = Tk()
    app= MainWindow(root)

class MainWindow:
   
    def __init__(self,master):
        
        self.master = master
        self.master.title("ART GALLERY")
        self.master.geometry("800x500+0+0")
        self.master.config(bg="#5B5B5B")
        self.frame = Frame(self.master,bg="#5B5B5B")
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.lblTitle = Label(self.frame,text = "Art Gallery", font="Helvetica 20 bold",bg="#5B5B5B",fg="black")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=40)
        
        self.LoginFrame1 = Frame(self.frame,width=400,height=80,relief="ridge",bg="#8E8E8E",bd=20)
        self.LoginFrame1.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="#8E8E8E",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
      
        self.lblUsername = Label(self.LoginFrame1,text="Username",font="Helvetica 14 bold",bg="#8E8E8E",bd=22)
        self.lblUsername.grid(row=0,column=0)
        self.lblUsername = Entry(self.LoginFrame1,font="Helvetica 14 bold",textvariable= self.Username,bd=2)
        self.lblUsername.grid(row=0,column=1)
        self.lblPassword = Label(self.LoginFrame1,text="Password ",font="Helvetica 14 bold",bg="#8E8E8E",bd=22)
        self.lblPassword .grid(row=1,column=0)
        self.lblPassword  = Entry(self.LoginFrame1,font="Helvetica 14 bold",show="*",textvariable= self.Password,bd=2)
        self.lblPassword .grid(row=1,column=1)
       
        self.btnLogin = Button(self.LoginFrame2,text = "Login" ,font="Helvetica 10 bold", width =10 ,bg="#8E8E8E",command = self.Login_system)
        self.btnLogin.grid(row=3,column=0)
        self.btnExit = Button(self.LoginFrame2,text = "Exit" ,font="Helvetica 10 bold", width =10 ,bg="#8E8E8E",command = self.Exit)
        self.btnExit.grid(row=3,column=1)
  
    def Login_system(self):

        S1=(self.Username.get())
        S2=(self.Password.get())
        if(S1=='admin' and S2=='1234'):
            self.newWindow = Toplevel(self.master)
            self.app = Menu(self.newWindow)
        elif(S1=='root' and S2=='4321'):
            self.newWindow = Toplevel(self.master)
            self.app = Menu(self.newWindow)
        else:
            tkinter.messagebox.askretrycancel("Please enter valid Username and Password")
            
    def Exit(self):
        self.master.destroy()




if __name__ == "__main__":
    main()
