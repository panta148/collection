"""
Insertion
Insertion operation means to insert one or more data elements into an array.
"""


from array import array
# creating an empty array , in which elements will be enter by user
my_array = array('i', [])
n = int(input("Enter the number of elements you want to enter:: "))
# taking input from the user and inserting into the array
for i in range(n):
    element = int(input(f"Enter {i+1} Element -> "))
    my_array.append(element)
# showing all the element of an array after inserting
print("Element's in an array after insertion:")
print(my_array)
