from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import sqlite3
import tkinter as tk
def main():
    root = Tk()
    app= Artist(root)
    
conn= sqlite3.connect ("VIRTUAL_ART_GALLERY.db")

class Artist:
    def __init__(self,master):
        self.master= master
        self.master.title ("List of Artists available")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="#8B4726")
        self.frame = Frame(self.master,bg="#8B4726")
        self.frame.pack()

        self.ARTIST_ID= IntVar()
        self.EXB_ID= IntVar()
        self.g_ID= IntVar()
        self.ARTIST_NAME=StringVar()
        self.CONTACT= IntVar()

        self.lblTitle = Label(self.frame,text = "Artist Menu", font="Helvetica 20 bold",bg="#8B4726")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
       
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="#CDAA7D",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="#CDAA7D",bd=20)
        self.LoginFrame2.grid(row=2,column=0)

        
        self.lblartistid=Label(self.LoginFrame,text="Artist ID",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
        self.lblartistid.grid(row=0,column=0)
        self.lblartistid=Entry(self.LoginFrame,font="Helvetica 14 bold",textvariable=self.ARTIST_ID)
        self.lblartistid.grid(row=0,column=1)
       
        self.lblexhid=Label(self.LoginFrame,text="Exhibition ID",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
        self.lblexhid.grid(row=1,column=0)
        self.lblexhid=Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.EXB_ID)
        self.lblexhid.grid(row=1,column=1)

        self.lblgid=Label(self.LoginFrame,text="Galary ID",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
        self.lblgid.grid(row=2,column=0)
        self.lblgid=Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.g_ID)
        self.lblgid.grid(row=2,column=1)
        
        self.lblaname=Label(self.LoginFrame,text="Artist name ",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
        self.lblaname.grid(row=3,column=0)
        self.lblaname=Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.ARTIST_NAME)
        self.lblaname.grid(row=3,column=1)

        self.lblcontact= Label(self.LoginFrame,text= "Contact number ",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
        self.lblcontact.grid(row=4,column=0)
        self.lblcontact= Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.CONTACT)
        self.lblcontact.grid(row=4,column=1)


        self.button1=Button(self.LoginFrame2,text="Save",width =10,font="Helvetica 14 bold",bg="#EEC591",command=self.artiInsert)
        self.button1.grid(row=3,column=1)
        self.button2=Button(self.LoginFrame2,text="Update",width =10,font="Helvetica 14 bold",bg="#EEC591",command=self.artiUpdate)
        self.button2.grid(row=3,column=2)
        self.button3=Button(self.LoginFrame2,text="Delete",width =10,font="Helvetica 14 bold",bg="#EEC591",command=self.artiDisp)
        self.button3.grid(row=3,column=3)
        self.button4=Button(self.LoginFrame2,text="Display",width =10,font="Helvetica 14 bold",bg="#EEC591",command=self.artiAll)
        self.button4.grid(row=3,column=4)
        self.button5=Button(self.LoginFrame2,text="Find",width =10,font="Helvetica 14 bold",bg="#EEC591",command=self.aFind)
        self.button5.grid(row=3,column=5)
        self.button6=Button(self.LoginFrame2,text="Exit",width =10,font="Helvetica 14 bold",bg="#EEC591",command=self.Exit)
        self.button6.grid(row=3,column=6)

    def Exit(self):
        self.master.destroy()

    def artiInsert(self):
        global a1, a2, a3,a4,a5, conn
        conn=sqlite3.connect("VIRTUAL_ART_GALLERY.db")
        curr=conn.cursor()

        a1=self.ARTIST_ID.get()
        a2=self.EXB_ID.get()
        a3=self.g_ID.get()
        a4=self.ARTIST_NAME.get()
        a5=self.CONTACT.get()

        a= list(conn.execute("select * from ARTISTS where ARTIST_ID=?",(a1,)))
        x=len(a)
        if x==0:
            tkinter.messagebox.showerror("Error","Artist already exists")
        else:
            conn.execute("insert into ARTISTS values(?,?,?,?,?)",(a1, a2, a3, a4,a5))
            tkinter.messagebox.showinfo("Artist included successfully!!")
        conn.commit()

    def artiUpdate(self):
        global u1, u2, u3, u4, u5, conn
        conn=sqlite3.connect("VIRTUAL_ART_GALLERY.db")
        curr=conn.cursor()

        u1=self.ARTIST_ID.get()
        u2=self.EXB_ID.get()
        u3=self.g_ID.get()
        u4=self.ARTIST_NAME.get()
        u5=self.CONTACT.get()

        p=list(conn.execute("select * from ARTISTS where ARTIST_ID=?",(u1,)))
        if len(p)!= 0:
            conn.execute("Update ARTISTS set EXB_ID=?,ARTIST_NAME=?,CONTACT=? where g_id=?", (u2,u4,u5,u2,))
            tkinter.messagebox.showinfo("Details updated")
        
        else:
            tkinter.messagebox.showerror("Artist does not exist")
        conn.commit()
    def artiDisp(self):
        curr=conn.cursor()
        
        inp_d=self.g_ID.get()

        p=list(conn.execute("select * from ARTISTS where g_ID=?", (inp_d,)))
        
        if (len(p)==0):
            tkinter.messagebox.showerror("No records found")
        else:
            conn.execute('DELETE FROM ARTISTS where g_ID=?',(inp_d,))
            tkinter.messagebox.showinfo("Details Updated")
            
        conn.commit()
    def artiAll(self):
        win=Tk()
        win.geometry("700x700")
    
        x=conn.execute("""Select * from ARTISTS""")
        global i
        i=0   
        for row in x:
            for j in range(len(row)):
                e=Label(win,width=20,text=row[j],relief='ridge',anchor="w")
                e.grid(row=i,column=j)        
            i+=1
        win.mainloop()


    def aFind(self):
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

        self.searchB=Button(self.LoginFrame2,text="Search for Artists in a Gallery",width =30,font="Helvetica 14 bold",
                            bg="#EEC591",command=self.artiFind)
        self.searchB.grid(row=0,column=1)
        

    def artiFind(self):

        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="#CDAA7D",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        q=conn.execute("""SELECT ARTISTS.ARTIST_ID,ARTISTS.ARTIST_NAME,ARTISTS.CONTACT,GALLERY.G_ID,GALLERY.G_NAME
                            FROM ARTISTS
                            FULL JOIN GALLERY ON ARTISTS.G_ID = GALLERY.G_ID""")
        for i in q:
            self.l1 = Label(self.LoginFrame,text="Artist ID",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l1.grid(row=1,column=0)
            self.dis1= Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="#CDAA7D",text=i[0])
            self.dis1.grid(row=1,column=1)
            
            self.l2 = Label(self.LoginFrame,text="Artist Name",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l2.grid(row=2,column=0)
            self.dis2=Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="#CDAA7D",text=i[1])
            self.dis2.grid(row=2,column=1)

            self.l3 = Label(self.LoginFrame,text="Contact",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l3.grid(row=3,column=0)
            self.dis3  = Label(self.LoginFrame,font="Helvetica 14 bold",bg="#CDAA7D",bd=2,text=i[2])
            self.dis3.grid(row=3,column=1)

            self.l4 = Label(self.LoginFrame,text="Gallery ID",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l4.grid(row=4,column=0)
            self.dis4= Label(self.LoginFrame,font="Helvetica 14 bold",bg="#CDAA7D",bd=2,text=i[3])
            self.dis4.grid(row=4,column=1)

            self.l5 = Label(self.LoginFrame,text="Gallery Name",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l5.grid(row=4,column=0)
            self.dis5= Label(self.LoginFrame,font="Helvetica 14 bold",bg="#CDAA7D",bd=2,text=i[4])
            self.dis5.grid(row=4,column=1)

if __name__ == "__main__":
    main()
