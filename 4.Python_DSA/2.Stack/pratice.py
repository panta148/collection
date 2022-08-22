# this is user define module
from stack2 import Stack
from time import sleep
s = Stack()
while True:
    print("""
    enter 1 for push
    enter 2 for pop
    enter 3 traverse
    enter 4 size
    enter 5 for isEmpty
    enter 0 for exit
    """)
    c = int(input("Enter your choice ->"))
    if c == 1:
        value = int(input("Enter the value you want to enter ->"))
        s.push(value)
        sleep(1)
    elif c == 2:
        element = s.pop()
        print(f'{element} is pop from the stack')
        sleep(1)
    elif c == 3:
        list = s.traverse()
        for i in list:
            print(i)
        sleep(1)
    elif c == 4:
        print(s.size())
        sleep(1)
    elif c == 5:
        print(s.isEmpty())
        sleep(1)
    elif c == 0:
        print("thanks for the operation")
        exit()
    else:
        print("Enter the valid option mention above")
        sleep(1)
