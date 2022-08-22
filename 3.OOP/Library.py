import sys
from time import sleep


class Library:
    def __init__(self, booklist, name):
        self.booklist = booklist
        self.name = name
        self.lendDict = {}

    def displaybook(self):
        print("Following are the book available in the library :")
        l = len(self.booklist)
        for i in range(l):
            print(f"{i+1}:{self.booklist[i]}")

        sleep(1)

    def lendbook(self, u, b):
        if b not in self.lendDict.keys():
            if b in self.booklist:
                self.lendDict.update({b: u})
                print(
                    f"Book has been updated in database !!! now you can take the {b} book")
            else:
                print(
                    f"This {b} is not in our database so you can not lend this book")
        else:
            print(f"Sorry Book is already being used by {self.lendDict[b]}")

        sleep(1)

    def addbook(self, book):
        self.booklist.append(book)
        print(f"{book} book is added to the database..........")
        sleep(1)

    def Searchbook(self, d):
        if d not in self.lendDict.keys():
            print('This book is not lend by any student at the moment')
        else:
            for key, value in self.lendDict.items():
                if key == d:
                    print(f"{self.lendDict[d]} is using this book")

        sleep(1)

    def returnbook(self, book):
        if book not in self.lendDict.keys():
            print(
                "This book is not lend by any one .... you can lend this book and then return later..")

        else:
            self.lendDict.pop(book)
            print(f" Now {book} is being return and it can be used by other ..")
            sleep(1)

    def updatebook(self, b):
        newuser = input(
            "Enter the name of the student to whom this book is going to bee lend ::->")
        if b in self.lendDict.keys():
            self.lendDict.update({b: newuser})
            print(f"Updated successfully \n Now {b} is lend by {newuser}")
        else:
            print(
                f'{b} is not in not in lend book list\n Sorry Try again with valid name')


if __name__ == '__main__':
    l = Library(['nepali', 'english', 'math', 'social',
                 'science', 'omath', 'eph', 'computer'], 'Everest')
    while True:
        print("\n**********************************************************")
        print(f"\twel come to {l.name} Library Managment system")
        print("**********************************************************")
        sleep(1)
        print("\nEnter 1 for Display Book")
        print("Enter 2 for lend Book")
        print("Enter 3 for Add Book")
        print("Enter 4 for Return Book")
        print("Enter 5 for Update Book")
        print("Enter 6 for Search User(By Book name)")
        print("Enter 0 for Exit")
        choice = int(input("Enter the choice mention above \n ->"))
        if choice not in [1, 2, 3, 4, 5, 6, 0]:
            print(
                "Enter the choice mention above only .... you have enter the wrong option")
        else:
            if choice == 1:
                l.displaybook()
            elif choice == 2:
                u = input("Enter the username :->")
                b = input("Enter the bookname :->")
                l.lendbook(u.lower(), b.lower())
            elif choice == 3:
                book = input(
                    "Enter the book you want to add in the database::->")
                l.addbook(book)
            elif choice == 4:
                book = input(
                    "Enter the book you want to Return::->")
                l.returnbook(book)
            elif choice == 5:
                b = input("Enter the book you want to update::->")
                l.updatebook(b)
            elif choice == 6:
                print('You Can Search user by writing the boook name.....')
                sbook = input(
                    "Enter the book you want to search in database::->")
                l.Searchbook(sbook)

            elif choice == 0:
                print("See you again !!!!!!!!!!!!!!!!!! 👲👲👲")
                sys.exit(0)
