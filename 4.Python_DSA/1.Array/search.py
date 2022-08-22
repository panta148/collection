"""

 Searching
Searching is the process of finding the element in the existing array with the help of index. 


"""


import array
my_array = array.array('i', [1, 3, 5, 7, 9, 1, 2, 4, 6, 8, 10])
search = int(input("Enter the number to be search :: "))
l = len(my_array)
found = False
# searching number in an array
for i in range(l):
    if my_array[i] == search:
        print(f"{search}  is found in {i+1} position  !!")
        found = True
# if number is not found then display the message
if found == False:
    print(f"{search } is not found in array")
