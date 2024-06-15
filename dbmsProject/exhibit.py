from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import sqlite3
import tkinter as tk

def main():
    root = Tk()
    app= Exhibition(root)
    

conn = sqlite3.connect("VIRTUAL_ART_GALLERY.db")
curr=conn.cursor()
class Exhibition:
    def __init__(self, master):
        self.master = master
        self.master.title("List of Exhibitions")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="#8B4726")
        self.frame = Frame(self.master,bg="#8B4726")
        self.frame.pack()
        
        self.EXB_ID = IntVar()
        self.g_ID = IntVar()
        self.LOCATION = StringVar()
        self.EXB_NAME = StringVar()
        self.START_DATE = StringVar()
        self.END_DATE = StringVar()

        self.lblTitle = tk.Label(self.frame,text = "Exhibition Menu", font="Helvetica 20 bold",bg="#8B4726")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
       
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="#CDAA7D",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="#CDAA7D",bd=20)
        self.LoginFrame2.grid(row=2,column=0)

        
        self.lbl_exb_id = Label(self.LoginFrame,text="Exhibition ID",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
        self.lbl_exb_id.grid(row=0,column=0)
        self.lbl_exb_id = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.EXB_ID)
        self.lbl_exb_id.grid(row=0,column=1)


        self.lbl_exb_name = Label(self.LoginFrame,text="Exhibition Name",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
        self.lbl_exb_name.grid(row=1,column=0)
        self.lbl_exb_name = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.EXB_NAME)
        self.lbl_exb_name.grid(row=1,column=1)

        self.lblgid=Label(self.LoginFrame,text="Galary ID",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
        self.lblgid.grid(row=2,column=0)
        self.lblgid=Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.g_ID)
        self.lblgid.grid(row=2,column=1)

        self.lbllocatt=Label(self.LoginFrame,text="Situated At",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
        self.lbllocatt.grid(row=3,column=0)
        self.lbllocatt=Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.LOCATION)
        self.lbllocatt.grid(row=3,column=1)

        self.lbl_start_date =Label(self.LoginFrame,text="Start Date",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
        self.lbl_start_date.grid(row=4,column=0)
        self.lbl_start_date =Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.START_DATE)
        self.lbl_start_date.grid(row=4,column=1)

        self.lbl_end_date = Label(self.LoginFrame,text="End Date",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
        self.lbl_end_date.grid(row=5,column=0)
        self.lbl_end_date =Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.END_DATE)
        self.lbl_end_date.grid(row=5,column=1)

        self.button_save = Button(self.LoginFrame2,text="Save",width =10,font="Helvetica 14 bold",bg="#CDAA7D", command=self.save_exhibition)
        self.button_save.grid(row=3,column=1)
        self.button_update = Button(self.LoginFrame2,text="Update",width =10,font="Helvetica 14 bold",bg="#CDAA7D", command=self.update_exhibition)
        self.button_update.grid(row=3,column=2)
        self.button_delete = Button(self.LoginFrame2,text="Delete", width =10,font="Helvetica 14 bold",bg="#CDAA7D",command=self.delete_exhibition)
        self.button_delete.grid(row=3,column=3)
        self.button_display = Button(self.LoginFrame2,text="Display", width =10,font="Helvetica 14 bold",bg="#CDAA7D",command=self.display_exhibitions)
        self.button_display.grid(row=3,column=4)
        self.button_find = Button(self.LoginFrame2,text="Find", width =10,font="Helvetica 14 bold",bg="#CDAA7D",command=self.exFind)
        self.button_find.grid(row=3,column=5)
        self.button_exit = Button(self.LoginFrame2,text="Exit",width =10,font="Helvetica 14 bold",bg="#CDAA7D", command=self.exit_window)
        self.button_exit.grid(row=3,column=6)

    def exit_window(self):
        self.master.destroy()

    def save_exhibition(self):
        global exb_id,g_id,location,exb_name,start_date,end_date
        exb_id = self.EXB_ID.get()
        g_id = self.g_ID.get()
        location = self.LOCATION.get()
        exb_name = self.EXB_NAME.get()
        start_date = self.START_DATE.get()
        end_date = self.END_DATE.get()

        curr = conn.cursor()
        curr.execute("INSERT INTO EXHIBITION (EXB_ID, G_ID, LOCATION, EXB_NAME, START_DATE, END_DATE) VALUES (?, ?, ?, ?, ?, ?)",
                     (exb_id, g_id, location, exb_name, start_date, end_date))
        
        tkinter.messagebox.showinfo("Exhibition saved successfully!")
        conn.commit()

    def update_exhibition(self):
        exb_id = self.EXB_ID.get()
        g_id = self.g_ID.get()
        location = self.LOCATION.get()
        exb_name = self.EXB_NAME.get()
        start_date = self.START_DATE.get()
        end_date = self.END_DATE.get()

        curr = conn.cursor()
        curr.execute("UPDATE EXHIBITION SET LOCATION=?, EXB_NAME=?, START_DATE=?, END_DATE=? WHERE EXB_ID=?",
                     (location, exb_name, start_date, end_date, exb_id))
        
        tkinter.messagebox.showinfo("Success", "Exhibition updated successfully!")
        conn.commit()

    def delete_exhibition(self):
        exb_id = self.EXB_ID.get()

        curr = conn.cursor()
        curr.execute("DELETE FROM EXHIBITION WHERE EXB_ID=?", (exb_id,))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Exhibition deleted successfully!")

    def display_exhibitions(self):
        curr = conn.cursor()
        curr.execute("SELECT * FROM EXHIBITION")
        rows = curr.fetchall()

        if rows:
            display_window = tk.Toplevel(self.master)
            display_window.title("Exhibitions")
            display_frame = tk.Frame(display_window)
            display_frame.pack()

            for i, row in enumerate(rows):
                for j, value in enumerate(row):
                    label = tk.Label(display_frame, text=value)
                    label.grid(row=i, column=j)

        else:
            tkinter.messagebox.showinfo("Info", "No exhibitions found.")

    def exFind(self):
        self.newWindow= Toplevel(self.master)
        self.app = sMenu(self.newWindow)



class sMenu:
    def __init__(self,master):
        global inp_s,s_gid,searchB

        self.master=master
        self.master.title("Exhibition")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="#8B4726")
        self.frame = Frame(self.master,bg="#8B4726")
        self.frame.pack()

        self.g_ID=IntVar()
        self.EXB_ID=StringVar()
        
        self.lblTitle = Label(self.frame,text = "Search Window", font="Helvetica 20 bold",bg="#8B4726")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=25)

        
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="#CDAA7D",bd=20)
        self.LoginFrame2.grid(row=2,column=0)


        self.searchB=Button(self.LoginFrame2,text="Search Exhibition of an Artwork",width =40,font="Helvetica 14 bold",bg="#EEC591",command=self.eArtwFind)
        self.searchB.grid(row=0,column=0)

        self.searchB=Button(self.LoginFrame2,text="Search Exhibition of an Artist",width =40,font="Helvetica 14 bold",bg="#EEC591",command=self.eArtiFind)
        self.searchB.grid(row=1,column=0)

        self.searchB=Button(self.LoginFrame2,text="Search Exhibition in a Gallery",width =40,font="Helvetica 14 bold",bg="#EEC591",command=self.eGalFind)
        self.searchB.grid(row=2,column=0)
        

    def eArtwFind(self):

        curr=conn.cursor()
        
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="#CDAA7D",bd=20)
        self.LoginFrame.grid(row=1,column=0)
    
        q=conn.execute("""SELECT EXHIBITION.EXB_ID, EXHIBITION.EXB_NAME, EXHIBITION.LOCATION, EXHIBITION.START_DATE, EXHIBITION.END_DATE, ARTWORK.ART_ID, ARTWORK.ART_IMAGE
                            FROM EXHIBITION
                            LEFT JOIN ARTWORK ON EXHIBITION.EXB_ID= ARTWORK.EXB_ID""")
        for i in q:
            self.l1 = Label(self.LoginFrame,text="Exhibition ID",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l1.grid(row=1,column=0)
            self.dis1= Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="#CDAA7D",text=i[0])
            self.dis1.grid(row=1,column=1)
            
            self.l2 = Label(self.LoginFrame,text="Exhibition Name",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l2.grid(row=2,column=0)
            self.dis2=Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="#CDAA7D",text=i[1])
            self.dis2.grid(row=2,column=1)

            self.l3 = Label(self.LoginFrame,text="Location",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l3.grid(row=3,column=0)
            self.dis3  = Label(self.LoginFrame,font="Helvetica 14 bold",bg="#CDAA7D",bd=2,text=i[2])
            self.dis3.grid(row=3,column=1)

            self.l4 = Label(self.LoginFrame,text="Start Date",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l4.grid(row=4,column=0)
            self.dis4= Label(self.LoginFrame,font="Helvetica 14 bold",bg="#CDAA7D",bd=2,text=i[3])
            self.dis4.grid(row=4,column=1)

            self.l5 = Label(self.LoginFrame,text="Start Date",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l5.grid(row=5,column=0)
            self.dis5 = Label(self.LoginFrame,font="Helvetica 14 bold",bg="#CDAA7D",bd=2,text=i[4])
            self.dis5.grid(row=5,column=1)

            self.l6 = Label(self.LoginFrame,text="End Date",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l6.grid(row=6,column=0)
            self.dis6 = Label(self.LoginFrame,font="Helvetica 14 bold",bg="#CDAA7D",bd=2,text=i[5])
            self.dis6.grid(row=6,column=1)

            self.l7 = Label(self.LoginFrame,text="Image",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l7.grid(row=7,column=0)
            self.dis7= Label(self.LoginFrame,font="Helvetica 14 bold",bg="#CDAA7D",bd=2,text=i[6])
            self.dis7.grid(row=7,column=1)
       

    def eArtiFind(self):
    
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="#CDAA7D",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        
        q=conn.execute("""SELECT EXHIBITION.EXB_ID, EXHIBITION.EXB_NAME,EXHIBITION.LOCATION,  ARTISTS.ARTIST_ID,ARTISTS.ARTIST_NAME,ARTISTS.CONTACT
                            FROM EXHIBITION
                            FULL JOIN ARTISTS ON EXHIBITION.EXB_ID = ARTISTS.EXB_ID""")
        for i in q:
            self.l1 = Label(self.LoginFrame,text="Exhibition ID",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l1.grid(row=1,column=0)
            self.dis1= Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="#CDAA7D",text=i[0])
            self.dis1.grid(row=1,column=1)
            
            self.l2 = Label(self.LoginFrame,text="Exhibition Name",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l2.grid(row=2,column=0)
            self.dis2=Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="#CDAA7D",text=i[1])
            self.dis2.grid(row=2,column=1)

            self.l3 = Label(self.LoginFrame,text="Location",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l3.grid(row=3,column=0)
            self.dis3  = Label(self.LoginFrame,font="Helvetica 14 bold",bg="#CDAA7D",bd=2,text=i[2])
            self.dis3.grid(row=3,column=1)

            self.l4 = Label(self.LoginFrame,text="Artist ID",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l4.grid(row=4,column=0)
            self.dis4= Label(self.LoginFrame,font="Helvetica 14 bold",bg="#CDAA7D",bd=2,text=i[3])
            self.dis4.grid(row=4,column=1)

            self.l5 = Label(self.LoginFrame,text="Artist Name",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l5.grid(row=5,column=0)
            self.dis5 = Label(self.LoginFrame,font="Helvetica 14 bold",bg="#CDAA7D",bd=2,text=i[4])
            self.dis5.grid(row=5,column=1)

            self.l6 = Label(self.LoginFrame,text="Contact",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l6.grid(row=6,column=0)
            self.dis6 = Label(self.LoginFrame,font="Helvetica 14 bold",bg="#CDAA7D",bd=2,text=i[5])
            self.dis6.grid(row=6,column=1)
            
    def eGalFind(self):
        
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="#CDAA7D",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        q=conn.execute("""SELECT EXHIBITION.EXB_ID, EXHIBITION.EXB_NAME, EXHIBITION.LOCATION,  GALLERY.G_ID,GALLERY.G_NAME
                            FROM EXHIBITION
                            LEFT JOIN GALLERY ON EXHIBITION.G_ID = GALLERY.G_ID""")
        for i in q:
            self.l1 = Label(self.LoginFrame,text="Exhibition ID",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l1.grid(row=1,column=0)
            self.dis1= Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="#CDAA7D",text=i[0])
            self.dis1.grid(row=1,column=1)
            
            self.l2 = Label(self.LoginFrame,text="Exhibition Name",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l2.grid(row=2,column=0)
            self.dis2=Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="#CDAA7D",text=i[1])
            self.dis2.grid(row=2,column=1)

            self.l3 = Label(self.LoginFrame,text="Location",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l3.grid(row=3,column=0)
            self.dis3  = Label(self.LoginFrame,font="Helvetica 14 bold",bg="#CDAA7D",bd=2,text=i[2])
            self.dis3.grid(row=3,column=1)

            self.l4 = Label(self.LoginFrame,text="Gallery ID",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l4.grid(row=4,column=0)
            self.dis4= Label(self.LoginFrame,font="Helvetica 14 bold",bg="#CDAA7D",bd=2,text=i[3])
            self.dis4.grid(row=4,column=1)

            self.l5 = Label(self.LoginFrame,text="Gallery Name",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
            self.l5.grid(row=5,column=0)
            self.dis5 = Label(self.LoginFrame,font="Helvetica 14 bold",bg="#CDAA7D",bd=2,text=i[4])
            self.dis5.grid(row=5,column=1)   

           
if __name__ == "__main__":
    main()
