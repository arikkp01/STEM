import pymysql

#connecting to database
db = pymysql.connect("localhost", "root", "password", "classroom")

#preparing object with cursor()
mycursor = db.cursor(pymysql.cursors.DictCursor)

#show tables/data
sql1 = "SELECT * from students"

#executing SQL query with execute()
mycursor.execute(sql1)

data = cur.fetchall()
for row in data:
	print("Name: " + row['name'] + " Age: " + str(row['age2']) + " Grade level: " + str(row['gradeLevel'])) 

#server disconnecting
cur.close()
db.close()

# Most of my files will have a table called age2. 
# In my phpmyadmin, in my database students,
#I acidentally labelled a table age2 and never changed it
