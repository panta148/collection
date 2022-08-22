"""
Deletion
Deletion refers to removing an existing element from the array. 
"""


import array
my_array = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10])
print(f"Your array list \n {my_array}  ")
num = int(input("Enter the number you want to delete \n ->"))
if num in my_array:
    my_array.remove(num)
    print(f"Array after the remove of {num}")
    print(my_array)
else:
    print(f'{num} is not found in an array . Try with new number ')
