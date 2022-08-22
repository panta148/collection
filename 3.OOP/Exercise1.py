"""
create the program to number of the object created
"""


class Count:
    count = 0

    def __init__(self):
        self.count += 1

    def show(self):
        print(f'Total Number of Object created :: {self.count}')


c = Count()
c.show()

c1 = Count()
c1.show()
