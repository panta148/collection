"""
write the program ot print the area of the rectangle by creating the class name Area taking the length
and the breadth as the parameter of the constructor and having a method name returnArea which return 
the area of the rectangle
length and the  breadth are enter by the user
"""


class Area:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def Returnarea(self):
        return self.length*self.breadth


while True:
    try:
        print("\n\n ************* Hello welcome to rectangle area calculation program **************")
        l = int(input("Enter the length of the rectangle \n ->"))
        b = int(input("Enter the breadth of the rectangle \n ->"))
        obj1 = Area(l, b)
        print(f"\nThe Area of the rectangle is:: {obj1.Returnarea()} ")

        print('')
        print('')
        option = input(
            "Enter 'n' to quite the program and any other to run it again \n ->")
        if option.lower() == 'n':
            break

    except ValueError as e:
        print("Enter the number only ")
        print(e)
