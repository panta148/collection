"""
this is the notifiacation app on your desk top
"""
import time
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(title="Hi..Amrit  please drink water ",
              message="you have to drink a lot of the water to be the happy and the healthy",
              timeout=5)
        print("Notification is already methon")
    