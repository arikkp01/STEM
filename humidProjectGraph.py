# importing the required module 
import matplotlib.pyplot as plt 
import pymysql

timeList = []
humidityList = []
temperatureList = []

# Open database connection
db = pymysql.connect("192.168.0.205","humid","password","sensor")

# Prepare a cursor object using cursor() method
cur = db.cursor(pymysql.cursors.DictCursor)
            
sql = "SELECT temperature FROM weather ORDER BY time DESC LIMIT 10";
sql2 = "SELECT humidity FROM weather ORDER BY time DESC LIMIT 10";
sql3 = "SELECT time FROM weather ORDER BY time DESC LIMIT 10";

# Execute SQL query using execute() method.
cur.execute(sql)
temp = cur.fetchall()

cur.execute(sql2)
humidity = cur.fetchall()

cur.execute(sql3)
time = cur.fetchall()
                
for row in temp:
  temperatureList.append(row['temperature'])

for row in humidity:
  humidityList.append(row['humidity'])

for row in time:
  timeList.append(str(row['time']))

print(timeList)
print(temperatureList)
print(humidityList)


# plotting the points  
timeList.reverse()
humidityList.reverse()
temperatureList.reverse()

fig, ax1 = plt.subplots(figsize=(20,5))
color = 'tab:red'
ax1.set_xlabel('Time')
ax1.set_ylabel('Temperature', color=color)
ax1.plot(timeList, temperatureList, color=color)
ax1.tick_params(axis='y', labelcolor=color)
plt.xticks(timeList, timeList, rotation=45)
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('Humidity', color=color)  # we already handled the x-label with ax1
ax2.plot(timeList, humidityList, color=color)
ax2.tick_params(axis='y', labelcolor=color)
plt.tight_layout()


plt.savefig('/var/www/html/graph.png')

plt.show()


# Disconnect from server
cur.close()
db.close()
