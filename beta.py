import Adafruit_DHT
import time
import csv
import sys

csvfile = "temp.csv"
als = True

While als:
  humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 18)
  
  if humidity is not None and temperature is not None:
  humidity = round(humdity, 2)
  temperature = round(temperature, 2)
  print('Temperature = {:0.1f}*C Humidity = {1:0.1f}%'.format(temperature, humidity)
  
  else:
    print('unable to connect')
    
  timeC = time.strftime("%I")=':' +time.strftime("%M")+ ':' +time.strftime("%S")
  data = [temperature, timeC]
  
  with open(csvfile, "a") as output:
    writer = csv.writer(output, delimiter= ",", lineterminator = '/n')
    wrtier.writerow(data)
time.sleep(5)
