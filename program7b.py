import sqlite3
carData=[
    (1,'Audi',2345),
    (2,'Mercedes',5172),
    (3,'Volvo',9999),
    (4,'toyota',8989),
    (5,'skoda',4567),
    (6,'Bently',3457),
    (7,'Hummer',786901)
    ]
import sqlite3 as lite
con = lite.connect('mtica.db')

cur=con.cursor()
cur.execute('DROP TABLE IF EXISTS Vehicles')
cur.execute(
    '''
CREATE TABLE   Vehicles(ID INT,NAME TEXT,PRICE INT)
'''    )


cur.executemany('INSERT INTO Vehicles values(?,?,?)',carData)
con.commit()
con.close()
print("values inserted")

    
