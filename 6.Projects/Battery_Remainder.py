print("Starting")
import psutil
import plyer
import sys
battery=psutil.sensors_battery()
percent=int(battery.percent)
print(f'Current Battery Percent is {percent}%')
while True:
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
    option=input("y/n?\n->")
    if option=='y':
        sys.exit()
                                    
                              
