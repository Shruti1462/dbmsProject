from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import sqlite3
import tkinter as tk

def main():
    root = Tk()
    app= Enquiry(root)
conn=sqlite3.connect("VIRTUAL_ART_GALLERY.db")
curr=conn.cursor()
class Enquiry:
    def __init__(self,master):
        self.master=master
        self.master.title("Want help? Contact us!")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="#8B4726")
        self.frame = Frame(self.master,bg="#8B4726")
        self.frame.pack()

        self.g_ID=IntVar()
        self.review=StringVar()
        self.date=StringVar()
        
        self.lblTitle = tk.Label(self.frame,text = "How did we do ?", font="Helvetica 20 bold",bg="#8B4726")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
       
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="#CDAA7D",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="#CDAA7D",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        
        self.lblgid=Label(self.LoginFrame,text="Galary ID",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
        self.lblgid.grid(row=1,column=0)
        self.lblgid=Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.g_ID)
        self.lblgid.grid(row=1,column=1)
        
        self.lblreview=Label(self.LoginFrame,text="Leave thy review here :  ",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
        self.lblreview.grid(row=3,column=0)
        self.lblreview=Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.review)
        self.lblreview.grid(row=3,column=1)
    
        self.lbldate=Label(self.LoginFrame,text="Date : ",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
        self.lbldate.grid(row=4,column=0)
        self.lbldate=Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.date)
        self.lbldate.grid(row=4,column=1)

        self.button_save = tk.Button(self.LoginFrame2,text="Save",width =10,font="Helvetica 14 bold",bg="#CDAA7D", command=self.save)
        self.button_save.grid(row=3,column=1)

        self.button_display = tk.Button(self.LoginFrame2,text="Display",width =10,font="Helvetica 14 bold",bg="#CDAA7D", command=self.display)
        self.button_display.grid(row=3,column=2)

        self.button_find = tk.Button(self.LoginFrame2,text="Find",width =10,font="Helvetica 14 bold",bg="#CDAA7D", command=self.eFind)
        self.button_find.grid(row=3,column=3)

        self.button_exit = tk.Button(self.LoginFrame2,text="Exit", width =10,font="Helvetica 14 bold",bg="#CDAA7D", command=self.exit_window)
        self.button_exit.grid(row=3,column=4)


    def exit_window(self):
        self.master.destroy()

    def save(self):
        
        g_id = self.g_ID.get()
        review = self.review.get()
        date = self.date.get()

        curr = conn.cursor()
        curr.execute("INSERT INTO ENQUIRY (g_ID, REVIEW, DATE) VALUES (?, ?, ?)",
                     (g_id,review,date))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Review saved successfully!")
        
    def display(self):
        curr = conn.cursor()
        curr.execute("SELECT * FROM ENQUIRY")
        rows = curr.fetchall()

        if rows:
            display_window = tk.Toplevel(self.master)
            display_window.title("Enquiry")
            display_frame = tk.Frame(display_window)
            display_frame.pack()

            for i, row in enumerate(rows):
                for j, value in enumerate(row):
                    label = tk.Label(display_frame, text=value)
                    label.grid(row=i, column=j)

        else:
            tkinter.messagebox.showerror("Info", "No enquiries found.")


    def eFind(self):
        self.newWindow= Toplevel(self.master)
        self.app = sMenu(self.newWindow)



class sMenu:
    def __init__(self,master):

        self.master=master
        self.master.title("ART GALLERY")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="#8B4726")
        self.frame = Frame(self.master,bg="#8B4726")
        self.frame.pack()

        
        self.lblTitle = Label(self.frame,text = "Search Window", font="Helvetica 20 bold",bg="#8B4726")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=25)

        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="#CDAA7D",bd=20)
        self.LoginFrame2.grid(row=2,column=0)

        self.searchB=Button(self.LoginFrame2,text="Search for Enquiry on a Gallery",width =30,font="Helvetica 14 bold",
                            bg="#EEC591",command=self.enqFind)
        self.searchB.grid(row=0,column=1)
        

    def enqFind(self):

        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="#CDAA7D",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        
        q=conn.execute("""SELECT ENQUIRY.REVIEW ,ENQUIRY.DATE, GALLERY.G_ID, GALLERY.G_NAME, GALLERY.location
                            FROM ENQUIRY
                            INNER JOIN GALLERY ON ENQUIRY.G_ID = GALLERY.G_ID""")
        for i in q:
            self.l1 = Label(self.LoginFrame,text="Review",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l1.grid(row=1,column=0)
            self.dis1= Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="#CDAA7D",text=i[0])
            self.dis1.grid(row=1,column=1)
            
            self.l2 = Label(self.LoginFrame,text="Date",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l2.grid(row=2,column=0)
            self.dis2=Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="#CDAA7D",text=i[1])
            self.dis2.grid(row=2,column=1)

            self.l3 = Label(self.LoginFrame,text="Gallery ID",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l3.grid(row=3,column=0)
            self.dis3  = Label(self.LoginFrame,font="Helvetica 14 bold",bg="#CDAA7D",bd=2,text=i[2])
            self.dis3.grid(row=3,column=1)

            self.l4 = Label(self.LoginFrame,text="Gallery Name",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l4.grid(row=4,column=0)
            self.dis4= Label(self.LoginFrame,font="Helvetica 14 bold",bg="#CDAA7D",bd=2,text=i[3])
            self.dis4.grid(row=4,column=1)

            self.l5 = Label(self.LoginFrame,text="Location",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l5.grid(row=9,column=0)
            self.dis5= Label(self.LoginFrame,font="Helvetica 14 bold",bg="#CDAA7D",bd=2,text=i[4])
            self.dis5.grid(row=9,column=1)
        
if __name__ == "__main__":
    main()
