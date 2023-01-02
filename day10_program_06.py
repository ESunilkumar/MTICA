import sqlite3 as lite
con = lite.connect('mtica.db')

cur=con.cursor()
cur.execute('DROP TABLE IF EXISTS CARS')
cur.execute('''CREATE TABLE   CARS(ID INT,NAME TEXT,PRICE INT)''')
print("TABLE CARS CREATED")
cur.execute("INSERT INTO CARS VALUES(1,'AJAY',1234)")
cur.execute("INSERT INTO CARS VALUES(2,'AMUL',1274)")





cur.execute("INSERT INTO CARS VALUES(3,'AMIT',1257)")
cur.execute("INSERT INTO CARS VALUES(1,'AJAY',3234)")
cur.execute("INSERT INTO CARS VALUES(1,'AJAY',5234)")


cur.execute("INSERT INTO CARS VALUES(1,'AJAY',7234)")



con.commit()
print("values in the table inserted CARS:")
