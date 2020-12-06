
import datetime

from playsound import playsound

import os

os.system("clear")

alarm_hour= int(input("what hour do need to alarm:"))

alarm_Minute =int(input("what minute do need to alarm:"))

am_or_pm = str(input("am or pm:"))
# clearing the termunal 
os.system("clear")

if am_or_pm == "pm":
  
  alarm_hour = alarm_hour+12

while True:
  
  if (alarm_hour == datetime.datetime.now().hour and alarm_Minute ==datetime.datetime.now().minute):
    
    print("ringing......")
    playsound("your/path/mp3")
    break
    
  