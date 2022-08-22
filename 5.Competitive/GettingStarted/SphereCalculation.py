"""
write program called sphere computation that prompts user for the radius of the sphere in floating number.
the program shall read the input as double:compute the volume and the surface area of the sphere in double and print the value
around 2 decimal place
"""
import math
radius=float(input("Enter the radius of the sphere \n:->"))
volume=4/3*math.pi*radius*radius*radius
surface_area=4*math.pi*radius*radius
print(f'The volume of the sphere is {volume}\n The surface of the sphere is {surface_area}')