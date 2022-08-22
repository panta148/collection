"""
count the cheese cubes

there is a tray having the cheese cube , we need to count the number of the cheese in the tray
one cube can not be palce into the another
you can ask the user for the dimensional of the box(length X width) and the also the size of the cube
for the box lenght nad the width can be different but for the cube the length and the width should 
be same
assumption: there is not any gaps or the space in between the tray or in side



input:
Enter the tray length:12 
Enter the tray width=12
Enter the side of cube=4

 output:
 Number of cube:9


 
input:
Enter the tray length:20
Enter the tray width=20
Enter the side of cube=5

 output:
 Number of cube:16

 
input:
Enter the tray length:12
Enter the tray width=12
Enter the side of cube=12

 output:
 Number of cube:1
"""
length=int(input("Enter the tray length ->"))
width=int(input("Enter the width of tray->"))
side=int(input("Enter the side of the cube->"))
number_of_cube=(length*width)//(side*side)
print('Number of cube :',number_of_cube)