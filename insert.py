import sqlite3
db=sqlite3.connect("LibStore.db")
cur=db.cursor()
cur.execute('''CREATE TABLE Lib (
BookID INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT (50) NOT NULL,
author TET(20),
price REAL);''')
for x in range(5):
    
    ttl=input("Enter book's title: ")
    aut=input("Enter name of author: ")
    pr=float(input("Enter price: "))
    sql="INSERT INTO Lib (title, author, price) VALUES ('"+ttl+"','"+aut+"','"+str(pr)+"');"

    try:
        cur=db.cursor()
        cur.execute(sql)
        db.commit()
        print ("One record added successfully")
    except:
        print ("Error in operation")
        db.rollback()
db.close()
