"""
in this code we discuss  the log and retrived from the file
record the three people we come to your gyms center and along with their food and the exercise schedule in the file
and retrive the data along with the name
"""
import datetime
import time
Customer_Name={
          1:"Anupa",2:"Amrit",3:"Manita",4:"Pragya"


}
Activity={
    1:"Exercise",2:"Food"
}
def C_menu():
    for key,value in Customer_Name.items():
        print(f'{key} for {value}')
def C_activity():
    for key,value in Activity.items():
        print(f'{key} for {value}')




if __name__ == '__main__':

   try:
       print("\n\n\t\t\tWel come to Amrit Fitness Center")
       print("Enter 1 for log Customer\nEnter 2 for  retrive Customer:\n->")
       option = int(input())
       if option == 1:
           C_menu()
           choice = int(input())
           if choice == 1:
               print("Enter 1 for food \n Enter 2 for Exercise")
               option = input()
               if option == "1":
                   with open("food.txt", "a") as f:
                       food = input("Enter the food of the customer")
                       time = (datetime.datetime.now().strftime("%H:%M%S"))
                       f.write(str(time)+"::"+food+"\n")
                       print(" Enter the data Successfully ")
               elif option == "2":
                   with open("Exercise.txt","a") as f:
                       exercise = input("Enter the Exercise of the customer")
                       time = (datetime.datetime.now().strftime("%H:%M%S"))
                       f.write(str(time) + "::" + exercise + "\n")
                       print(" Enter the data Successfully ")

   except Exception as e:
       print(e)
