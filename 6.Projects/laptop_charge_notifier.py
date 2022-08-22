'''
pip install psutil
pip install plyer
''' 
import psutil
from plyer import notification
import time
from sys import exit
battery=psutil.sensors_battery()
print("\t\t\t\n\n\n\nWelcome To Battery Charge Notifier App\n\n")
# print(battery)
while True:
    percent=battery.percent
    notification.notify(title="Battery Percentage",
    message=str(percent)+"%  Battery remaining",
    timeout=100)
    time.sleep(10)
    option=input("If you want to stop program enter 'Y' otherwise enter any letter \n ->")
    if option=="y":
        break
    
print('You are now out of the program')    
        
    