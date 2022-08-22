import schedule
import time
import psutil
import plyer
import sys

def Remainder():
    battery=psutil.sensors_battery()
    percent=int(battery.percent)
    print(f'Current Battery Percent is {percent}%')
    if percent<40:
        print("Charge the device quickly")
        plyer.notification.notify(title="Battery Remainder",
                            message=f"Charge the laptop on Time\nYour Charger at the moment is {percent}%",
                            timeout=10
                            # app_icon="low.jpg"
                            )  
        
    else:
        print("You are at the safe Zone......")  
        plyer.notification.notify(title="Battery Remainder",
                                message=f"Charge at the moment is {percent}%",
                                timeout=10,
                                # app_icon="full.jpg"
                                )
    
def thank():
    print('Thank to all for wishing the birthday for me') 
# time  
schedule.every(5).seconds.do(Remainder)
schedule.every(10).seconds.do(thank)
while True:
    schedule.run_pending()
    time.sleep(1)     