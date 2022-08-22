"""
write the program to print the area and the perimeter of the
triangle having side 3,4 and 5 by creating the class
name Triangle without any parameter in the constructor

"""


class Triangle(object):
    def getd(self):
        self.l1 = int(input("Enter the 1st side of Traingle :: "))
        self.l2 = int(input("Enter the 2st side of Traingle ::  "))
        self.l3 = int(input("Enter the 3st side of Traingle ::  "))

    def claculate(self):
        self.p = self.l1+self.l2+self.l3
        print(self.p)
        self.s = (self.l1+self.l2+self.l3)//3
        print(self.s)
        self.a = (self.s*(self.s-self.l1)*(self.s-self.l2)*(self.s-self.l3))
        print(self.a)
        print(
            f"The perimeter of trangle having side {self.l1}, {self.l2},{self.l3 } is {self.p}\n\n")
        print(
            f"The Area of trangle having side {self.l1}, {self.l2},{self.l3 } is {self.a}")


obj1 = Triangle()
obj1.getd()
obj1.claculate()
