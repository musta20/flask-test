import sqlite3

connection = sqlite3.connect('data.db')

curser = connection.cursor()

#create_table = " CREATE TABLE if not exists items (item text,price real)"

#curser.execute(create_table)

#user = (2,'mustafa','Aa123456')

#select_query = "insert into items values ('test' , 12.12) "
#curser.execute(select_query)
for row in curser.execute("select * from items"):
   print(row)
    
connection.commit()

connection.close()