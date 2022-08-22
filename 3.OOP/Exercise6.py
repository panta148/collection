"""
write the program to print the area of the two rectangle having side (4,5) and (5,8) by creating
the class name Rectangle with the method Area which return the Area and the length and breadth are
passed through the constructor
"""


class Rectangle:
    def __init__(self, l1, b1, l2, b2):
        self.l1 = l1
        self.b1 = b1
        self.l2 = l2
        self.b2 = b2

    def Area(self):
        return (self.l1*self.b1), (self.l2*self.b2)


obj1 = Rectangle(4, 5, 5, 8)
a1, a2 = obj1.Area()
print(a1)
print(a2)
print(
    f"The area of Recatngle having  side {obj1.l1} and {obj1.l1} is {a1} \n similary ,,\nThe area of Recatngle having  side {obj1.l2} and {obj1.b2} is {a2} ")
