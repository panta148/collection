# find the total surface of the cylinder
import math
radius=float(input("Enter the radius of the cylinder ->"))
height=float(input("Enyer the height of the cylinder ->"))
tsa=2*math.pi*radius*(radius+height)
print("Total surrface of the cylinder is:",round(tsa,2))