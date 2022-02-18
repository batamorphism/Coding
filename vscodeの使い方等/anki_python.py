import sqlite3

dbname = 'C:\\Users\\Takanori\\Desktop\\プログラミング__競技プログラミング\\collection.anki2'
conn = sqlite3.connect(dbname)
c = conn.cursor()
c.execute("select * from sqlite_master where type='table'")
for row in c.fetchall():
    print(row)

conn.close()
# conn.execute('SELECT * FROM items')
