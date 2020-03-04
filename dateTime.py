#Use the datetime object to crerate and manipulate date and time
#Import modules need from datetime

#datetime = liberary
from datetime import time
from datetime import date
from datetime import datetime

#create a main loop so this module can be imported

def main():
  #create a new date time object that holds the current datetime 
  currentTime = datetime.now()
  
  print(currentTime)
  
  #print only the time from the datetime object
  print(datetime.time(currentTime))
  
  #Use strftime to print only the year from the dattime object
  #%Y will show full 2020 ear vs %y show only 20 as year
  print("Current Year: ", currentTime.strftime("%Y"))
   
  #Use strftime to print a very human readable date
  print("Current Date: ",currentTime.strftime("%a, %B %d, %Y"))
  
#% string substitution
#need help? search strf python

#if__name__ == "__main__":
  #main()  
