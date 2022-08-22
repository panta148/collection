"""
 write program that keep the number from the user and generate the number from 1 to 7 and display weekend
"""
import time
print("wel come to our week choice program\nEnter 1-7 number to choice the weekend\nEnter 0 to exit from the program")

while 1:
    choice = int(input("\nEnter the number to choice weekend..\n-> "))
    if choice == 1:
        print("sunday")
    elif choice == 2:
        print("Monday")
    elif choice == 3:
        print("Tuesday")
    elif choice == 4:
        print("Wednesday")
    elif choice == 5:
        print("Thursday")
    elif choice == 6:
        print("Friday")
    elif choice == 7:
        print("Saturday")
    elif choice==0:
        print("now you will go out from the program in 3 second")
        time.sleep(3)
        exit()
    else:
        print("invalid option ..please enter the correct one")


