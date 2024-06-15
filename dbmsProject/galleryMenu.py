from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import sqlite3
import tkinter as tk

def main():
    root = Tk()
    app= Gallery(root)
    
conn=sqlite3.connect("VIRTUAL_ART_GALLERY.db")
cur1=conn.cursor()
class Gallery:
    def __init__(self,master):
        self.master=master
        self.master.title("List of Galleries available")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="#8B4726")
        self.frame = Frame(self.master,bg="#8B4726")
        self.frame.pack()

        self.g_ID=IntVar()
        self.g_Name=StringVar()
        self.location=StringVar()

        self.lblTitle = tk.Label(self.frame,text = "Gallery Menu", font="Helvetica 20 bold",bg="#8B4726")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
       
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="#CDAA7D",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="#CDAA7D",bd=20)
        self.LoginFrame2.grid(row=2,column=0)

        #Attributes
        
        self.lblgid=Label(self.LoginFrame,text="Galary ID",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
        self.lblgid.grid(row=0,column=0)
        self.lblgid=Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.g_ID)
        self.lblgid.grid(row=0,column=1)

        self.lblgname=Label(self.LoginFrame,text="Galary Name",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
        self.lblgname.grid(row=1,column=0)
        self.lblgname=Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.g_Name)
        self.lblgname.grid(row=1,column=1)
        
        self.lbllocat=Label(self.LoginFrame,text="Situated At",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
        self.lbllocat.grid(row=3,column=0)
        self.lbllocat=Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.location)
        self.lbllocat.grid(row=3,column=1)

        #CRUD
        
        self.button1=Button(self.LoginFrame2,text="Save",width =10,font="Helvetica 14 bold",
                            bg="#CDAA7D",command=self.galInsert)
        self.button1.grid(row=3,column=1)
        self.button2=Button(self.LoginFrame2,text="Update",width =10,font="Helvetica 14 bold",
                            bg="#CDAA7D",command=self.galUpdate)
        self.button2.grid(row=3,column=2)
        self.button3=Button(self.LoginFrame2,text="Delete",width =10,font="Helvetica 14 bold",
                            bg="#CDAA7D",command=self.galDisp)
        self.button3.grid(row=3,column=3)
        self.button4=Button(self.LoginFrame2,text="Display",width =10,font="Helvetica 14 bold",
                            bg="#CDAA7D",command=self.galAll)
        self.button4.grid(row=3,column=4)
        self.button5=Button(self.LoginFrame2,text="Find",width =10,font="Helvetica 14 bold",
                            bg="#CDAA7D",command=self.sDisp)
        self.button5.grid(row=3,column=5)
        self.button6=Button(self.LoginFrame2,text="Exit",width =10,font="Helvetica 14 bold",
                            bg="#CDAA7D",command=self.Exit)
        self.button6.grid(row=3,column=6)

        
    def Exit(self):
        self.master.destroy()

    def galInsert(self):
        global g1,g2,g3,conn
        conn=sqlite3.connect("VIRTUAL_ART_GALLERY.db")
        curr=conn.cursor()

        g1=self.g_ID.get()
        g2=self.g_Name.get()
        g3=self.location.get()
        
        a= list(conn.execute("select * from GALLERY where g_ID=?",(g1,)))
        x=len(a)
        if x!= 0 :
            tkinter.messagebox.showerror("Error","Galary Already Exists")
        else :
           conn.execute("insert into GALLERY values(?,?,?)",(g1,g2,g3,))
           tkinter.messagebox.showinfo("Success!","Galary Set Succesfully!")
        conn.commit()
        
    def galUpdate(self):
        global u1,u2,u3,conn
        curr=conn.cursor()

        g1=self.g_ID.get()
        g2=self.g_Name.get()
        g3=self.location.get()

        conn=sqlite3.connect("VIRTUAL_ART_GALLERY.db")

        p=list(conn.execute("select * from GALLERY where g_ID=?",(g1,)))

        if len(p) != 0:
            conn.execute("Update GALLERY set g_Name=?,location=? where g_ID=?",(g2,g3,g1,))
            tkinter.messagebox.showinfo("Success","Details updated")
            conn.commit()
        else :
            tkinter.messagebox.showerror("Error","Galary does not exist")

    def galAll(self):
        win=Tk()
        win.geometry("700x700")
    
        x=conn.execute("""Select * from GALLERY""")
        global i
        i=0   
        for row in x:
            for j in range(len(row)):
                e=Label(win,width=20,text=row[j],relief='ridge',anchor="w")
                e.grid(row=i,column=j)        
            i+=1
        win.mainloop()
            
    def galDisp(self):
        
        curr=conn.cursor()
        
        inp_d=self.g_ID.get()

        p=list(conn.execute("select * from GALLERY where g_ID=?", (inp_d,)))
        
        if (len(p)==0):
            tkinter.messagebox.showerror("Error","No records found")
        else:
            conn.execute('DELETE FROM GALLERY where g_ID=?',(inp_d,))
            tkinter.messagebox.showinfo("Sucess","Details Updated")
        conn.commit()
        
    def sDisp(self):
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
        

        self.searchB=Button(self.LoginFrame2,text="Search for Artwork in a Gallery",width =30,font="Helvetica 14 bold",
                            bg="#EEC591",command=self.galFind)
        self.searchB.grid(row=0,column=1)
        

    def galFind(self):

        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="#CDAA7D",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        
        q=conn.execute("""SELECT GALLERY.G_ID, GALLERY.G_NAME, ARTWORK.ART_ID, ARTWORK.TITLE
                        FROM GALLERY
                        FULL JOIN ARTWORK ON GALLERY.G_ID=ARTWORK.G_ID""")
        for i in q:
            self.l1 = Label(self.LoginFrame,text="Gallery ID",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l1.grid(row=1,column=0)
            self.dis1= Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="#CDAA7D",text=i[0])
            self.dis1.grid(row=1,column=1)
            
            self.l2 = Label(self.LoginFrame,text="Gallery Name",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l2.grid(row=2,column=0)
            self.dis2=Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="#CDAA7D",text=i[1])
            self.dis2.grid(row=2,column=1)

            self.l3 = Label(self.LoginFrame,text="Art ID",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l3.grid(row=3,column=0)
            self.dis3  = Label(self.LoginFrame,font="Helvetica 14 bold",bg="#CDAA7D",bd=2,text=i[2])
            self.dis3.grid(row=3,column=1)

            self.l4 = Label(self.LoginFrame,text="Art Name",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l4.grid(row=4,column=0)
            self.dis4= Label(self.LoginFrame,font="Helvetica 14 bold",bg="#CDAA7D",bd=2,text=i[3])
            self.dis4.grid(row=4,column=1)
        
if __name__ == "__main__":
    main()
           
        

            

        
        
