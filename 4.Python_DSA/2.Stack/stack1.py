"""
Stack is a linear data structure which follows a particular order in which the operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out).

There are many real-life examples of a stack. Consider an example of plates stacked over one another in the canteen. The plate which is at the top is the first one to be removed, i.e. the plate which has been placed at the bottommost position remains in the stack for the longest period of time. So, it can be simply seen to follow LIFO(Last In First Out)/FILO(First In Last Out) order.
"""

import sys


class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        if self.stack == []:
            return True
        else:
            return False

    def push(self):
        try:
            value = int(input("Enter the value you want to PUSH -> "))
            self.stack.append(value)
            print(f'{value} is added to the stack....')
            print()
        except:
            print("Enter the number only !!! You have enter the other character..")

    def pop(self):
        if self.stack == []:
            print("No Element to POP , Stack is Empty at the moment")
        else:
            l = self.stack.pop()
            print(f'{l} value is pop from the stack')

    def stop(self):
        print("Thanks for the operation....... have an nice day ahead")
        sys.exit()

    def search(self, f):
        count = 0
        for i in range(len(self.stack)):
            if self.stack[i] == f:
                print(f'{f} found in {i+1} Position')
                count += 1
        if count == 0:
            print(f'{f} is not found in our stack')

    def update(self):
        #do in future1
        pass

    def show(self):
        if self.stack == []:
            print("Stack is Empty...\n So Enter Element First")
        else:
            print("Element in the stack are::::")
            # to make the latest enter element at the top we reverse the list
            for i in self.stack[::-1]:
                print(i)
        print()

    @staticmethod
    def menu():
        print("""
        Enter 1 for PUSH(C)
        Enter 2 for Traverse(R)
        Enter 3 for Update(U)
        Enter 4 for POP(D)
        Enter 5 for Search
        Enter 6 for size of stack
        Enter 7 for check empty or not
        Enter 0 for Exit
        """)
        try:
            choice = int(input("Enter your choice \n -> "))
            return choice
        except:
            print("Enter Number only ... You havee Enter the Other Character..")
            print()


s = Stack()
while True:
    print()
    print('********** Welcome to Stack Opeartion ********************')
    print()
    c = Stack.menu()
    if c == 1:
        s.push()
    elif c == 2:
        s.show()
    elif c == 3:
        s.update()
    elif c == 4:
        s.pop()
    elif c == 5:
        try:
            f = int(input("Enter the element you want to search... "))
            s.search(f)
        except ValueError:
            print("Enter integer value only for search")
    elif c == 6:
        print(s.size())
        print()
    elif c == 7:
        print(s.isEmpty())
        print()
    elif c == 0:
        s.stop()
    else:
        print("Invalid Option !!!! Please Enter the correct option")
        print()
