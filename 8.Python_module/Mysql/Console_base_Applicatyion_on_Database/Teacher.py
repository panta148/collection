from DataBase import MyConnection
import sys
import time


def menu():
    print("\n\n***************************************************************************")
    print("WelCome to Student Management System")
    print("Enter 1 for Insert Data")
    print("Enter 2 for Delete Data")
    print("Enter 3 for Update Data")
    print("Enter 4 for Show Data")
    print("Enter 5 for Search Data")
    print("Enter 0 for Exit")
    print("\n\n***************************************************************************")
    Choice = int(input("\nEnter the choice mention above -> "))
    return Choice


if __name__ == '__main__':
    obj = MyConnection()
    while True:
        choice = menu()
        if choice == 1:
            print("\n\n")
            id = int(input("Enter the  new Userid to Insert ->"))
            name = input("Enter the  name ->")
            roll = int(input("Enter the  roll -> "))
            add = input("Enter the  address -> ")
            obj.insert(id, name, roll, add)
            time.sleep(3) 

        elif choice == 2:
            print("\n\n")
            id = int(input("Enter the Userid to delete"))
            obj.delete(id)
            time.sleep(3) 

        elif choice == 3:
            print("\n\n")
            id = int(input("Enter the Userid to update ->"))
            name = input("Enter the new name ->")
            roll = int(input("Enter the new roll -> "))
            add = input("Enter the new address -> ")
            obj.update(id, name, roll, add)
            time.sleep(3) 

        elif choice == 4:
            print("\n\n")
            obj.fetch_all()
            time.sleep(3) 

        elif choice == 0:
            sys.exit()
        elif choice == 5:
                print("\n\n")
                id=int(input("Enter the ID to search ->"))
                obj.search(id)   
                time.sleep(3) 
        else:
            print("Enter the correct Option ")
            time.sleep(3) 
