"""
Traverse:
Traverse means printing all the elements of an array.

"""

# import array class from array module
from array import array
# creating array of integer value
my_array = array('i', [2, 4, 6, 8, 10])
# for traverse we used loop to show all the elments of an array
print("Element of an array are listed here after::")
for i in range(len(my_array)):
    print(f"my_array[{i}]={my_array[i]}")
