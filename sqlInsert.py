import pymysql

#connecting database
db = pymysql.connect("localhost", "root", "password", "classroom")

#preparing object with cursor() method
cur = db.cursor(pymysql.cursors.DictCursor)

# entering new data
sql1 = "INSERT INTO students (name,age2,gradeLevel) VALUES ('Joe', 18, 9)"

# executing SQL query with execute() method
cur.execute(sql)
db.commit()
#printing record
print(mycursor.rowcount, "record inserted.")

sql2 = "SELECT * from students"
cur.execute(sql2)

data = cur.fetchall()
for row in data:
	print("Name: " + row['name'] + " Age: " + str(row['age2']) + " Grade level: " + str(row['gradeLevel'])) 

#disconnecting server
cur.close()
db.close()

# Most of my files will have a table called age2. 
# In my phpmyadmin, in my database students,
#I acidentally labelled a table age2 and never changed it
