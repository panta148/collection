from array import array
import sys
from time import sleep


class Array:
    def __init__(self, my_array):
        self.my_array = my_array

    def insertelement(self, n):
        for i in range(n):
            num = int(input(f"Enter {i+1} element :: "))
            self.my_array.append(num)
        print(f'Congratulation {n} element are added into an array')
        sleep(1)

    def searchelement(self, s):
        found = False
        # searching number in an array
        for i in range(len(self.my_array)):
            if my_array[i] == s:
                print(f"{s}  is found in {i+1} position  !!")
                found = True
        # if number is not found then display the message
        if found == False:
            print(f"{s } is not found in array")

    def updatearray(self, position, newelement):
        self.my_array[position-1] = newelement
        print("\nArray list after updating")
        print('[', end='')
        for i in range(len(self.my_array)):
            print(f'{self.my_array[i]}', end=',')
        print(']')

    def deletearray(self):
        num = int(input("Enter the number you want to delete \n ->"))
        if num in self.my_array:
            self.my_array.remove(num)
            print(f"Array after the remove of {num}")
            print('[', end='')
            for i in range(len(self.my_array)):
                print(f'{self.my_array[i]}', end=',')
            print(']')

        else:
            print(f'{num} is not found in an array . Try with new number ')

    def showarray(self):
        if len(self.my_array) == 0:
            print(
                "Enter some element first in an array \n As there is no any eelement to Show at the moment")
        else:
            print("Element in an array:")
            print('[', end='')
            for i in range(len(self.my_array)):
                print(f'{self.my_array[i]}', end=',')
            print(']')

    @staticmethod
    def menu():
        print('''
        1.Enter element in array(insertion)
        2.Delete element from array
        3.Update an element from array
        4.Search an element from an array
        5.Show all element from an array
        0.Exist
        ''')
        option = int(input("Enter the option ::   "))
        return option


if __name__ == '__main__':
    # initializing an empty array
    print("\n\nAll Operation related to an Array")
    my_array = array('i', [])
    a = Array(my_array)
    while True:
        choice = a.menu()
        if choice == 1:
            # insertion of an array
            n = int(input("How many element  you want insert in an array::  "))
            a.insertelement(n)
        elif choice == 2:
            # deletion
            a.deletearray()
        elif choice == 3:
            # updating
            position = int(
                input("\nEnter the position on which you want to update :: \n -> "))
            new_element = int(
                input("Enter the new element you want to enter \n -> "))
            a.updatearray(position, new_element)
        elif choice == 4:
            # searching
            s = int(input("Enter an element  you want to search in an array::  "))
            a.searchelement(s)

        elif choice == 5:
            # traverse an array
            a.showarray()
        elif choice == 0:
            print("Thank you \n See you later")
            sleep(1)
            sys.exit(0)
        else:
            print("Enter the valid option mention above....")
