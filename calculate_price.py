import sqlite3
db=sqlite3.connect("LibStore.db")
cur=db.cursor()

total=0
while True:
    
    ttl=input("Enter book's title: ")

    sql="SELECT * FROM Lib WHERE title='"+ttl+"'"
    cur=db.cursor()
    cur.execute(sql)
    rec=cur.fetchone()
    if rec!=None:
        print (rec)
        pr=rec[3]
        qty=int(input("Enter number of books purchased: "))
        cost=pr*qty
        total=total+cost
    else:
        print ("Title Not Found")
    choice=input("add more books[Y/N]? : ")
    if choice=='N': break
print ("Total cost of Purchased Books",total)
db.close()
