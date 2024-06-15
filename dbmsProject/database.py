import sqlite3 

conn=sqlite3.connect("VIRTUAL_ART_GALLERY.db")

cur=conn.cursor()

conn.execute("DROP TABLE IF EXISTS GALLERY")
conn.execute("""CREATE TABLE GALLERY (
                G_ID INT PRIMARY KEY,
                G_NAME VARCHAR (20),
                location VARCHAR (20))""")
print("Galery Table created successfully")

conn.execute("""INSERT INTO GALLERY VALUES 
                (0001, 'Snapshots Of Life', 'New Delhi'),
                (0002, 'Memories Lane', 'Norway'),
                (0003, 'Artful Haven', 'Croatia'),
                (0004, 'Palette Paradise', 'Hawaii'),
                (0005, 'Brushstroke Gallery', 'Switzerland'),
                (0006, 'Creative Art Gallery', 'Mumbai'),
                (0007, 'Arististic Alchemy', 'LA'),
                (0008, 'Surreal Spectrum', 'Paris'),
                (0009, 'The Art Vault', 'Greece'),
                (0010, 'Whimsical Wonders', 'Venice')""")

conn.execute("DROP TABLE IF EXISTS ENQUIRY")
conn.execute("""CREATE TABLE ENQUIRY (
                G_ID INT NOT NULL,
                REVIEW VARCHAR(100),
                DATE DATE,
                CONSTRAINT CHK_DATE CHECK (DATE IS NOT NULL),
                FOREIGN KEY (G_ID) REFERENCES GALLERY (G_ID))""")
print("Enquiry Table created successfully")

conn.execute(""" INSERT INTO ENQUIRY VALUES
                (0004, 'Best thing about Hawaii?', '2022-03-18'),
                (0004, 'It was really a paradise there','2024-01-22'),
                (0007, 'It was really a work of an alchemist', '2024-02-14'),
                (0008, 'Paris literally have the best exhibitions!!', '2024-03-25'),
                (0010, 'Did find all the wonders at Whimsical Wonders', '2024-01-20'),
                (0010, 'Are there works of Van Serena', '2024-01-17'),
                (0006, 'Creative art gallery is really...creative', '2024-02-27'),
                (0009, 'Lot of history was there indeed!!', '2024-03-20'),
                (0004, 'The place is perfect for the exhibition', '2024-05-22'),
                (0003, 'Loved it','2024-03-16')""")

conn.execute("DROP TABLE IF EXISTS EXHIBITION")
conn.execute("""CREATE TABLE EXHIBITION (
                EXB_ID INT PRIMARY KEY NOT NULL,
                G_ID INT NOT NULL,
                LOCATION VARCHAR (30),
                EXB_NAME VARCHAR (30),
                START_DATE DATE,
                END_DATE DATE,
                FOREIGN KEY(G_ID) REFERENCES GALLERY (G_ID))""")
print("Exhibition Table created successfully")

conn.execute("""INSERT INTO EXHIBITION VALUES
                (1237,0007,'MOSCOW','THE ARTISTIC TAPESTRY','2023-09-08','2023-10-15'),
                (1238,0008,'TORONTO','CELESTICAL BRUSHSTROKES','2023-08-06','2023-09-05'),
                (1239,0009,'BUENOS AIRES','CHROMATIC REVERIE','2024-03-23','2024-04-25'),
                (1240,0010,'ROME','EPHEMERAL EXPRESSIONS','2024-03-15','2024-04-16')""")

conn.execute("DROP TABLE IF EXISTS ARTISTS")
conn.execute("""CREATE TABLE ARTISTS(
                ARTIST_ID INT PRIMARY KEY NOT NULL,
                EXB_ID INT NOT NULL,
                G_ID INT NOT NULL,
                ARTIST_NAME VARCHAR (30),
                CONTACT INT,
                FOREIGN KEY(G_ID) REFERENCES GALLERY (G_ID),
                FOREIGN KEY (EXB_ID) REFERENCES EXHIBITION (EXB_ID))""")
print("Artists Table created successfully")

conn.execute("""INSERT INTO ARTISTS VALUES 
                (5501, 1231, 0001, 'Shruti Nandy',1234567),
                (5502, 1232, 0002, 'Luna Delmar',9876543),
                (5503, 1233, 0003, 'Jasper Wilde',2468135),
                (5504, 1234, 0004, 'Milo Everhart',3692580),
                (5505, 1235, 0005, 'Aurora Blake',7778888),
                (5506, 1236, 0006, 'Felix Montague',5551212), 
                (5507, 1237, 0007, 'Seraphina Rivers',8889999),
                (5508, 1238, 0008, 'Orion Sterling',4321098),
                (5509, 1239, 0009, 'Nova Valencia',6543210),
                (5510, 1240, 0010, 'Phoenix Monroe',3219876)""")

conn.execute("DROP TABLE IF EXISTS ARTWORK")
conn.execute("""CREATE TABLE ARTWORK(
                ART_ID  VARCHAR(20) PRIMARY KEY,
                ARTIST_ID INT NOT NULL,
                EXB_ID  INT NOT NULL,
                G_ID INT NOT NULL,
                PRICE INT,
                ART_TYPE VARCHAR (30),
                TITLE VARCHAR(30),
                ART_IMAGE BLOB ,
                FOREIGN KEY(G_ID) REFERENCES GALLERY (G_ID),
                FOREIGN KEY(EXB_ID) REFERENCES EXHIBITION(EXB_ID),
                FOREIGN KEY(ARTIST_ID) REFERENCES ARTISTS(ARTIST_ID))""")
print("Artwork Table created successfully")

entries = [
    ('AR2',5502,1231,2,200000000, 'Painting', 'Into The Unknown','C:/Users/shrut/OneDrive/Documents/dbmsProject/dbmsProject/intoTheUnkown.jpg'),
    ('AR3',5503,1231,3,1500000, 'Poetry', 'The Coffee Torments','C:/Users/shrut/OneDrive/Documents/dbmsProject/dbmsProject/theCoffeeTorments.jpg'),
    ('AR4',5504,1231,4,5000000, 'Architecture', 'Elizabeth Diller','C:/Users/shrut/OneDrive/Documents/dbmsProject/dbmsProject/elizabethDiller.jpg'),
    ('AR5',5505,1231,5,3500000, 'Music', 'Symphony Of Heart','C:/Users/shrut/OneDrive/Documents/dbmsProject/dbmsProject/SymphonyOfArt.jpg'),
    ('AR6',5506,1231,6,40000000, 'Abstract Art', 'Arquitectura Viva','C:/Users/shrut/OneDrive/Documents/dbmsProject/dbmsProject/arquitecturaViva.jpg'),
    ('AR7',5507,1231,7,6700000, 'Cinema And Theatre', 'End Of The World','C:/Users/shrut/OneDrive/Documents/dbmsProject/dbmsProject/endOfTheWorld.jpg'),
    ('AR8',5508,1231,8,5600000, 'Digital Art', 'Culture Deed','C:/Users/shrut/OneDrive/Documents/dbmsProject/dbmsProject/culturalDeed.jpg'),
    ('AR9',5509,1231,9,8000000, 'Modern Art', 'Luna Rising','C:/Users/shrut/OneDrive/Documents/dbmsProject/dbmsProject/lunaRising.jpg'),
    ('AR10',5510,1231,10,15000000, 'Bio Art', 'A truer reciprocity','C:/Users/shrut/OneDrive/Documents/dbmsProject/dbmsProject/aTrueReciprocity.jpg'),
    ]

for entry in entries :
    art_id, artist_id, exb_id, g_id, price, art_type, title, image_path = entry
    with open(image_path, 'rb') as file:
        image_data = file.read()
    
    insert_query = """INSERT INTO ARTWORK(ART_ID, ARTIST_ID, EXB_ID, G_ID, PRICE, ART_TYPE, TITLE, ART_IMAGE)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
    
    
    conn.execute(insert_query, (art_id, artist_id, exb_id, g_id, price, art_type, title, image_data))

#print([row for row in conn.execute("SELECT * FROM ARTWORK").fetchall()])

conn.execute("DROP TABLE IF EXISTS CUSTOMER")
conn.execute("""CREATE TABLE CUSTOMER (
                CUST_ID varchar(10) PRIMARY KEY,
                ART_ID varchar(20) NOT NULL,
                NAME VARCHAR (20),
                CONTACT_NO CHAR (10) UNIQUE,
                ADDRESS VARCHAR(100) DEFAULT 'NOT AVAILABLE',
                foreign key(ART_ID) REFERENCES ARTWORK(ART_ID))""")
print("Customer Table created successfully")

conn.execute("""INSERT INTO CUSTOMER VALUES 
                ('CU01', 'AR1', 'Khushi Gupta', 1234567890, '567 Willow Street, Anytown' ),
                ('CU02', 'AR2', 'Emily Johnson', 2345678901, '890 Cedar Avenue, Somewhereville'),
                ('CU03', 'AR3', 'Liam Anderson', 3456789012, '234 Birch Road, Anywhere City'),
                ('CU04', 'AR4', 'Sophia Martinez', 5678901234, '789 Spruce Lane, Nowhereville'),
                ('CU05', 'AR5', 'Ethan Thompson', 6789012345, '012 Magnolia Drive, Anytown'),
                ('CU06', 'AR6', 'Olivia Davis', 7890123456, '345 Sycamore Court, Somewhereville'), 
                ('CU07', 'AR7', 'Noah Wilson', 8901234567, '678 Juniper Lane, Anywhere City'),
                ('CU08', 'AR8', 'Ava Thomas', 9012345678, ' 901 Pineapple Street, Nowhereville'),
                ('CU09', 'AR9', 'Lucas Garcia', 0123456789, '567 Strawberry Road, Somewhereville'),
                ('CU10', 'AR10', 'Mia Clark', 4567890123, '456 Oak Avenue, Somewhereville')""")

conn.commit()
conn.close()
