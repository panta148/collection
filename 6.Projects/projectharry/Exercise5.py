''''
health management system
in this sf , we take care about thee client exercise and diiet paln strictly
wee keep all log in the file and keep record of all details
'''
import time


def gettime():
    return time.ctime()


client = {
    1: "Amrit",
    2: "Manita",
    3: "pragya",
    4: "Anupa"
}
plan = {
    1: "Exercise",
    2: "Diets"
}
print("\n\n\n*****************************************************************************")
print("\n\nWel come to Gyms Management System....")
print("\n\t\t\t Keep Healthy, Health is Wealth")

while 1:
    print()
    print("\n\n\n*****************************************************************************")
    for index, value in client.items():
        print(f'{index}:{value}')
    cid = int(input("\nChoose User Name ( with your id ) ->"))
    print()
    print("Enter 1 for See your data")
    print("Enter 2 for log your data")
    choice = int(input("Enter your chooice -> "))
    if choice == 1:
        print("\n\n")
        print()
        print("Enter 1 for See your Exercise log")
        print("Enter 2 for See your Diet Log")
        op = int(input("Enter the option -> "))
        if op == 1:
            with open(f'{client[cid]}_Exercise.txt') as f:
                content = f.readlines()
                for line in content:
                    print(line, end='')
        else:
            with open(f'{client[cid]}_Diet.txt') as f:
                content = f.readlines()
                for line in content:
                    print(line, end='')

    elif choice == 2:
        for index, value in plan.items():
            print(f'{index}:{value}')
        pid = int(input("\n\n Enter the option for log...(Exercise or Diet) -> "))
        if pid == 1:
            ex = input("Which exercise did you do ?  ")
            with open(f'{client[cid]}_Exercise.txt', 'a') as f:
                f.write(
                    f'\n I have done {ex} Exercise in time ::  {gettime()} ')
        elif pid == 2:
            dd = input("Which Diet did you Take ?  ")
            with open(f'{client[cid]}_Diet.txt', 'a') as f:
                f.write(
                    f'\n I have take {dd} Diet in  time::  {gettime()} time')
        else:
            print("Enter the correct option man...")
    else:
        print("Enter the correct option man...")

    option = input("\n\nEnter q for quit -> ")
    if option == 'q':
        break

print("\n\n\n*****************************************************************************")
