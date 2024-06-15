from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import sqlite3
import tkinter as tk
from PIL import Image,ImageTk
from io import BytesIO

conn = sqlite3.connect("VIRTUAL_ART_GALLERY.db")
    
class Artwork:
    def __init__(self, master):
        self.master = master
        self.master.title("Manage Artwork")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="#8B4726")
        self.frame = Frame(self.master,bg="#8B4726")
        self.frame.pack()
        
        self.ART_ID = tk.StringVar()
        self.ARTIST_ID = tk.IntVar()
        self.EXB_ID = tk.IntVar()
        self.g_ID = tk.IntVar()
        self.PRICE = tk.IntVar()
        self.ART_TYPE = tk.StringVar()
        self.TITLE = tk.StringVar()

        self.lblTitle = tk.Label(self.frame,text = "Art Menu", font="Helvetica 20 bold",bg="#8B4726")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
       
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="#CDAA7D",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="#CDAA7D",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        
        self.lbl_art_id = tk.Label(self.LoginFrame,text="Artwork ID",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
        self.lbl_art_id.grid(row=0,column=0)
        self.lbl_art_id = tk.Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.ART_ID)
        self.lbl_art_id.grid(row=0,column=1)

        self.lbl_artist_id = tk.Label(self.LoginFrame,text="Artist ID",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
        self.lbl_artist_id.grid(row=1,column=0)
        self.lbl_artist_id = tk.Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.ARTIST_ID)
        self.lbl_artist_id.grid(row=1,column=1)

        self.lbl_exb_id = tk.Label(self.LoginFrame,text="Exhibition ID",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
        self.lbl_exb_id.grid(row=2,column=0)
        self.lbl_exb_id = tk.Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.EXB_ID)
        self.lbl_exb_id.grid(row=2,column=1)

        self.lbl_g_id = tk.Label(self.LoginFrame,text="Gallery ID",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
        self.lbl_g_id.grid(row=3,column=0)
        self.lbl_g_id = tk.Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.g_ID)
        self.lbl_g_id.grid(row=3,column=1)

        self.lbl_price = tk.Label(self.LoginFrame,text="Price",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
        self.lbl_price.grid(row=4,column=0)
        self.lbl_price = tk.Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.PRICE)
        self.lbl_price.grid(row=4,column=1)

        self.lbl_art_type = tk.Label(self.LoginFrame,text="Art Type",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
        self.lbl_art_type.grid(row=5,column=0)
        self.lbl_art_type = tk.Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.ART_TYPE)
        self.lbl_art_type.grid(row=5,column=1)

        self.lbl_title = tk.Label(self.LoginFrame,text="Title",font="Helvetica 14 bold",bg="#CDAA7D",bd=22)
        self.lbl_title.grid(row=6,column=0)
        self.lbl_title = tk.Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.TITLE)
        self.lbl_title.grid(row=6,column=1)

        self.button_save = tk.Button(self.LoginFrame2,text="Save",width =10,font="Helvetica 14 bold",bg="#EEC591", command=self.save_artwork)
        self.button_save.grid(row=3,column=1)
        self.button_update = tk.Button(self.LoginFrame2,text="Update",width =10,font="Helvetica 14 bold",bg="#EEC591", command=self.update_artwork)
        self.button_update.grid(row=3,column=2)
        self.button_delete = tk.Button(self.LoginFrame2,text="Delete",width =10,font="Helvetica 14 bold",bg="#EEC591", command=self.delete_artwork)
        self.button_delete.grid(row=3,column=3)
        self.button_display = tk.Button(self.LoginFrame2,text="Display",width =10,font="Helvetica 14 bold",bg="#EEC591", command=self.display_artwork)
        self.button_display.grid(row=3,column=4)
        self.button_find = tk.Button(self.LoginFrame2,text="Find",width =10,font="Helvetica 14 bold",bg="#EEC591",  command=self.find_artwork)
        self.button_find.grid(row=3,column=5)
        self.button_exit = tk.Button(self.LoginFrame2,text="Exit", width =10,font="Helvetica 14 bold",bg="#EEC591", command=self.exit_window)
        self.button_exit.grid(row=3,column=6)

    def exit_window(self):
        self.master.destroy()

    def save_artwork(self):
        art_id = self.ART_ID.get()
        artist_id = self.ARTIST_ID.get()
        exb_id = self.EXB_ID.get()
        g_id = self.g_ID.get()
        price = self.PRICE.get()
        art_type = self.ART_TYPE.get()
        title = self.TITLE.get()

        curr = conn.cursor()
        curr.execute("INSERT INTO ARTWORK (ART_ID, ARTIST_ID, EXB_ID, g_ID, PRICE, ART_TYPE, TITLE) VALUES (?, ?, ?, ?, ?, ?, ?)",
                     (art_id, artist_id, exb_id, g_id, price, art_type, title))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Artwork saved successfully!")

    def update_artwork(self):
        art_id = self.ART_ID.get()
        artist_id = self.ARTIST_ID.get()
        exb_id = self.EXB_ID.get()
        g_id = self.g_ID.get()
        price = self.PRICE.get()
        art_type = self.ART_TYPE.get()
        title = self.TITLE.get()

        curr = conn.cursor()
        curr.execute("UPDATE ARTWORK SET ARTIST_ID=?, EXB_ID=?, g_ID=?, PRICE=?, ART_TYPE=?, TITLE=? WHERE ART_ID=?",
                     (artist_id, exb_id, g_id, price, art_type, title, art_id))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Artwork updated successfully!")

    def delete_artwork(self):
        art_id = self.ART_ID.get()

        curr = conn.cursor()
        curr.execute("DELETE FROM ARTWORK WHERE ART_ID=?", (art_id,))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Artwork deleted successfully!")

    def display_artwork(self):
        window = tk.Toplevel()
        window.title("Artwork Information")
        
        connection = sqlite3.connect("VIRTUAL_ART_GALLERY.db")
        cursor = connection.cursor()
        
        
        select_query = """SELECT ART_ID, ARTIST_ID, EXB_ID, G_ID, PRICE, ART_TYPE, TITLE, ART_IMAGE
                          FROM ARTWORK"""
        cursor.execute(select_query)
        rows = cursor.fetchall()
        
        for row in rows:
            art_id, artist_id, exb_id, g_id, price, art_type, title, image_data = row
            
            
            image = Image.open(BytesIO(image_data))
            photo = ImageTk.PhotoImage(image)
            
            
            attributes_label = tk.Label(window, text=f"Art ID: {art_id}\nArtist ID: {artist_id}\nExhibition ID: {exb_id}\nGallery ID: {g_id}\nPrice: {price}\nArt Type: {art_type}\nTitle: {title}")
            attributes_label.pack()
            
            image_label = tk.Label(window, image=photo)
            image_label.photo = photo  
            image_label.pack()

        

    def find_artwork(self):
        art_id = self.ART_ID.get()

        curr = conn.cursor()
        curr.execute("SELECT * FROM ARTWORK WHERE ART_ID=?", (art_id,))
        row = curr.fetchone()

        if row:
            display_window = tk.Toplevel(self.master)
            display_window.title("Artwork Details")
            display_frame = tk.Frame(display_window)
            display_frame.pack()

            for i, value in enumerate(row):
                label = tk.Label(display_frame, text=value)
                label.grid(row=0, column=i)
        else:
            tkinter.messagebox.showerror("Info", "Artwork not found.")


