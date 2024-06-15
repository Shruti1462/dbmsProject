from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import sqlite3

def main():
    root = Tk()
    app= Customer(root)
conn= sqlite3.connect ("VIRTUAL_ART_GALLERY.db")

class Customer:
    def __init__(self, master):
        self.master=master
        self.master.title("List of our customer")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="#8B4726")
        self.frame = Frame(self.master,bg="#8B4726")
        self.frame.pack()
        
        self.CUST_ID= StringVar()
        self.ART_ID= StringVar()
        self.NAME=StringVar()
        self.CONTACT_NO= IntVar()
        self.ADDRESS= StringVar()

        self.lblTitle = Label(self.frame,text = "Customer Menu", font="Helvetica 20 bold",bg="#8B4726")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
       
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="#CDAA7D",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="#CDAA7D",bd=20)
        self.LoginFrame2.grid(row=2,column=0)

        
        self.lblcustID=Label(self.LoginFrame,text="Customer ID",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
        self.lblcustID.grid(row=0,column=0)
        self.lblcustID=Entry(self.LoginFrame,font="Helvetica 14 bold",textvariable=self.CUST_ID)
        self.lblcustID.grid(row=0,column=1)

        self.lblartID=Label(self.LoginFrame,text="Art ID",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
        self.lblartID.grid(row=1,column=0)
        self.lblartID=Entry(self.LoginFrame,font="Helvetica 14 bold",textvariable=self.ART_ID)
        self.lblartID.grid(row=1,column=1)

        self.lblname=Label(self.LoginFrame,text="NAME",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
        self.lblname.grid(row=2,column=0)
        self.lblname=Entry(self.LoginFrame,font="Helvetica 14 bold",textvariable=self.NAME)
        self.lblname.grid(row=2,column=1)

        self.lblcontact_NO=Label(self.LoginFrame,text=" CONTACT NO.",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
        self.lblcontact_NO.grid(row=3,column=0)
        self.lblcontact_NO=Entry(self.LoginFrame,font="Helvetica 14 bold",textvariable=self.CONTACT_NO)
        self.lblcontact_NO.grid(row=3,column=1)

        self.lbladdress=Label(self.LoginFrame,text="ADDRESS OF CUSTOMER",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
        self.lbladdress.grid(row=4,column=0)
        self.lbladdress=Entry(self.LoginFrame,font="Helvetica 14 bold",textvariable=self.ADDRESS)
        self.lbladdress.grid(row=4,column=1)

        self.button1=Button(self.LoginFrame2,text="Save",width =10,font="Helvetica 14 bold",bg="#EEC591",command=self.custInsert)
        self.button1.grid(row=3,column=1)
        self.button2=Button(self.LoginFrame2,text="Update",width =10,font="Helvetica 14 bold",bg="#EEC591",command=self.Update)
        self.button2.grid(row=3,column=2)
        self.button3=Button(self.LoginFrame2,text="Delete",width =10,font="Helvetica 14 bold",bg="#EEC591",command=self.custDel)
        self.button3.grid(row=3,column=3)
        self.button4=Button(self.LoginFrame2,text="Display",width =10,font="Helvetica 14 bold",bg="#EEC591",command=self.custDisp)
        self.button4.grid(row=3,column=4)
        self.button5=Button(self.LoginFrame2,text="Find",width =10,font="Helvetica 14 bold",bg="#EEC591",command=self.cFind)
        self.button5.grid(row=3,column=5)
        self.button6=Button(self.LoginFrame2,text="Exit",width =10,font="Helvetica 14 bold",bg="#EEC591",command=self.Exit)
        self.button6.grid(row=3,column=6)

    def Exit(self):
        self.master.destroy()

    def custInsert(self):
        global c1,c2,c3,c4,c5,conn
        conn=sqlite3.connect("VIRTUAL_ART_GALLERY.db")
        curr=conn.cursor()
        
        c1=self.CUST_ID.get()
        c2=self.ART_ID.get()
        c3=self.NAME.get()
        c4=self.CONTACT_NO.get()
        c5=self.ADDRESS.get()

        a= list(conn.execute("select* from CUSTOMER where CUST_ID=?",(c1,)))
        x=len(a)
        if x != 0:
            tkinter.messagebox.showerror("Error","Account already exists")
        else:
            conn.execute("insert into CUSTOMER values(?,?,?,?,?)",(c1,c2,c3,c4,c5,))
            tkinter.messagebox.showinfo("Success!","Set Succesfully!")
        conn.commit()
    def Update(self):
        global v1,v2,v3,v4,v5,conn
        curr=conn.cursor()

        c1=self.CUST_ID.get()
        c2=self.ART_ID.get()
        c3=self.NAME.get()
        c4=self.CONTACT_NO.get()
        c5=self.ADDRESS.get()

        conn=sqlite3.connect("VIRTUAL_ART_GALLERY.db")

        p=list(conn.execute("select * from CUSTOMER where CUST_ID=?",(c1,)))

        if len(p) != 0:
            conn.execute("Update CUSTOMER set CUST_ID=?,ART_ID=?,NAME=?,CONTACT_NO=?,ADDRESS=?",(c1,c2,c3,c4,c5,))
            tkinter.messagebox.showinfo("Succes","Details updated")
        
        else :
            tkinter.messagebox.showerror("Error","Account does not exist")
        conn.commit()
         
    def custDisp(self):
        
        win=Tk()
        win.geometry("700x700")
    
        x=conn.execute("""Select * from CUSTOMER""")
        global i
        i=0   
        for row in x:
            for j in range(len(row)):
                e=Label(win,width=20,text=row[j],relief='ridge',anchor="w")
                e.grid(row=i,column=j)        
            i+=1
        win.mainloop()

    def custDel(self):
        global inp_d,del_custID

        curr=conn.cursor()
        inp_d=self.CUST_ID.get()

        p=list(conn.execute("select* from CUSTOMER where CUST_ID=?", (inp_d,)))

        if(len(p)==0):
            tkinter.messagebox.showerror("Ooops","No records found")
        else:
            conn.execute('DELETE FROM CUSTOMER where CUST_ID=?',(inp_d,))
            tkinter.messagebox.showinfo("Succes","Details deleted")
        conn.commit()
        
    def cFind(self):
        self.newWindow= Toplevel(self.master)
        self.app = sMenu(self.newWindow)



class sMenu:
    def __init__(self,master):

        self.master=master
        self.master.title("Customer Information")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="#8B4726")
        self.frame = Frame(self.master,bg="#8B4726")
        self.frame.pack()
        
        self.lblTitle = Label(self.frame,text = "Search Window", font="Helvetica 20 bold",bg="#8B4726")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=25)

        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="#CDAA7D",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        

        self.searchB=Button(self.LoginFrame2,text="Search for Customer of an Artwork",width =30,font="Helvetica 14 bold",
                            bg="#EEC591",command=self.custFind)
        self.searchB.grid(row=0,column=1)
        

    def custFind(self):

        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="#CDAA7D",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        q=conn.execute("""SELECT CUSTOMER.CUST_ID, CUSTOMER.NAME, CUSTOMER.CONTACT_NO, ARTWORK.ART_ID, ARTWORK.TITLE
                            FROM ARTWORK
                            RIGHT JOIN CUSTOMER ON ARTWORK.ART_ID=CUSTOMER.ART_ID""")
        for i in q:
            self.l1 = Label(self.LoginFrame,text="Customer ID",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l1.grid(row=1,column=0)
            self.dis1= Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="#CDAA7D",text=i[0])
            self.dis1.grid(row=1,column=1)
            
            self.l2 = Label(self.LoginFrame,text="Customer Name",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l2.grid(row=3,column=0)
            self.dis2=Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="#CDAA7D",text=i[1])
            self.dis2.grid(row=3,column=1)

            self.l3 = Label(self.LoginFrame,text="Contact",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l3.grid(row=5,column=0)
            self.dis3  = Label(self.LoginFrame,font="Helvetica 14 bold",bg="#CDAA7D",bd=2,text=i[2])
            self.dis3.grid(row=5,column=1)

            self.l4 = Label(self.LoginFrame,text="Art ID",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l4.grid(row=7,column=0)
            self.dis4= Label(self.LoginFrame,font="Helvetica 14 bold",bg="#CDAA7D",bd=2,text=i[3])
            self.dis4.grid(row=7,column=1)

            self.l5 = Label(self.LoginFrame,text="Art Name",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l5.grid(row=9,column=0)
            self.dis5= Label(self.LoginFrame,font="Helvetica 14 bold",bg="#CDAA7D",bd=2,text=i[4])
            self.dis5.grid(row=9,column=1)
                         


   

        
if __name__ == "__main__":
    main()
        
            

        
        
