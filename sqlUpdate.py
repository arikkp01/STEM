#importing pymysql
import pymysql

#connecting to data base pymysql
db = pymysql.connect ("localhost", "root", "password,"classroom")

#using cursor() method to prepare cursor
cur = db.cursor(pymysql.cursors.DictCursor)

#Updating data
sql = "UPDATE students SET age=14 WHERE name= 'Boa'"

#executing SQL query
#execute() method

cur.execute(sql)

#changes to database
db.commit()

#disconnect
cur.close()
db.close()

# Most of my files will have a table called age2. 
# In my phpmyadmin, in my database students,
#I acidentally labelled a table age2 and never changed it
