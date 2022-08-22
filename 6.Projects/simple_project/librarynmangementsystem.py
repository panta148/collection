class Library:
    def __init__(self, listofbook, name):
        self.booklist=listofbook
        self.name=name
        self.lendDict={}



    def displayBook(self):
        print(f"we have the  following book in the library:{self.name}")
        for book in self.booklist:
            print(book)


    def lendBook(self,user,book):
        if book  not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("book dictionary has been updated.you can take the book now")

    def addBook(self,book):
         self.booklist.append(book)
         print("book has been added to thr list")

    def returnBook(self,book):
         self.lendDict.pop(book)


if __name__ == '__main__':
    am=Library(['python','rich daddy poor daddy','harry potter','c++','algorithms'],"code_with_Amrit")
    while True:
        print(f"wel come to the {am.name} library.enter the choice to continue")
        print("1.display book")
        print("2.lend book")
        print("3.add book")
        print("4.return book")
        user_choice=input()
        if user_choice not in ['1','2','3','4']:
            print("enter the valid option")
            continue
        else:
            user_choice=int(user_choice)

        if user_choice==1:
            am.displayBook()
        elif user_choice==2:
            book=input("enter the book you want to lend")
            user=input("enter the name")
            am.lendBook(user,book)

        elif user_choice == 3:
            book=input("enter the bok name you want to add")
            am.addBook(book)

        elif user_choice == 4:
            book = input("enter the bok name you want return")
            am.returnBook(book)

        else:
            print("not a valid option ")
        print("press q to quit and c to continue")
        user_choice2 = ""
        while user_choice2!="c" and user_choice2!="q":

            user_choice2=input()
            if user_choice2 == 'q':
                exit()
            elif user_choice2 == "c":
                continue





