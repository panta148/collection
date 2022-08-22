'''
4. Write a Python program which accepts the radius of a circle from the user and compute the area.
Sample Output :
r = 1.1
Area = 3.8013271108436504
'''
from math import pi,pow
print("\t\t\tProgram to calculate the area of circle")
r=float(input("r="))
# area=pi*r*r
area=pi*pow(r,2)
print(f'Area ={area}')


