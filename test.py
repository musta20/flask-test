import sqlite3

connection = sqlite3.connect('data.db')

curser = connection.cursor()

create_table = " CREATE TABLE if not exists items (id INTEGER PRIMARY KEY,store_id INTEGER ,item text  ,price real)"
create_table1 = " CREATE TABLE if not exists users (id INTEGER PRIMARY KEY , username text , password text)"
create_table2 = " CREATE TABLE if not exists store (id INTEGER PRIMARY KEY , name text)"

curser.execute(create_table)
curser.execute(create_table1)
curser.execute(create_table2)

#user = (2,'mustafa','Aa123456')

#select_query = "insert into items values ('test' , 12.12) "
#curser.execute(select_query)
#for row in curser.execute("select * from items"):
  # print(row)
    
connection.commit()

connection.close()