# referemce: https://docs.python.org/2/library/sqlite3.html

import sqlite3
conn = sqlite3.connect('person.db')

# create a cursor object 
c = conn.cursor()

# execute a sql query
# c.execute("CREATE TABLE persons(name TEXT,age INTEGER,location TEXT) ; ")

data = ('Prasanna','USA',25)
query = "INSERT INTO persons(name,location,age) VALUES  (?,?,?) "
c.execute(query,data)


#commit a query changes
conn.commit()
conn.close()