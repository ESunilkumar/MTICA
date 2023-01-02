import sqlite3 as lite
con=lite.connect('mtica.db')
cur=con.cursor()
cur.execute('''
delete from vehicles
where name='volvo'
''')
con.commit()
con.close()
print("data deleted")
