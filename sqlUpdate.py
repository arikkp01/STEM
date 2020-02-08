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
