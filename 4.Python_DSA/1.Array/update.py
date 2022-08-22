"""
 Update
Updating refers to updating an existing element from the array at a given index.
"""


from array import array
my_array = array('i', [1, 2, 3, 5, 6, 7, 9])
print(f"Your array List\n {my_array}")
position = int(
    input("\nEnter the position on which you want to update :: \n -> "))
new_element = int(input("Enter the new element you want to enter \n -> "))
# updating the new eelement at the given position
my_array[position-1] = new_element
print("\nArray list after updating")
print(my_array)
