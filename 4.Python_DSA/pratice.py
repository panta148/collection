''''
library management system
'''


class Library:
    def __init__(self, book, lend_book):
        print("\n\n\n**************************************************************************************")
        print("\n\n\n\t\t\tWelcome to Library Manageement System..")
        self.book = book
        self.lend_book = lend_book

    def Login(self):
        print("\n\n\n")
        username = input("\t\t\t\tEnter Username::\n\t\t\t\t -> ")
        password = input("\t\t\t\tEnter Password::\n\t\t\t\t -> ")
        if username == 'admin' and password == 'admin':
            self.Operation(self.menu())
        else:
            print("\n\n\t\tEnter the correct Username and Password for login in system\n")
            self.Login()

    def menu(self):
        print("Enter 1 for see all book")
        print("Enter 2 for lend book")
        print("Enter 3 for Return book")
        print("Enter 4 for your detail")
        print("Enter 5 for upadate your Detail")
        print("Enter 0 for exit")
        print("")
        option = int(input("Enter the option -> "))
        return option

    def Operation(self, data):
        if data == 0:
            exit()
        elif data == 1:
            for item, value in self.book.items():
                print(item, ":", value)
            self.Operation(self.menu())
        elif data == 2:
            name = input("Enter Your name ->")
            book = input("Enter book name ->")
            for id, bname in self.book.items():
                if book == bname:
                    lend_book[book] = name
                    print(f'{book} Book is now recorded for {name} \n Thank you')

            self.Operation(self.menu())
        elif data == 1:
            pass
        elif data == 1:
            pass
        elif data == 1:
            pass
        elif data == 1:
            pass
        elif data == 1:
            pass
        elif data == 1:
            pass
        else:
            print("Enter the correct option mention ...")
            exit()


book = {1: "English", 2: "Nepali", 3: "Math", 4: "Science"}
lend_book = {}
l = Library(book, lend_book)
l.Login()
# while True:
#     l.menu()
