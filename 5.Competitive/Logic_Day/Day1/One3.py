# calculate the area and the perimeter of the right angle triangle




####################################################################
# method1
# p=float(input("\n\n\nEnter the p of the right Angle Triangle ->"))
# b=float(input("Enter the b of the right Angle Triangle ->"))
# h=float(input("Enter the h of the right Angle Triangle ->"))
# area=0.5*p*b/1
# perimeter=p+b+h
# print(f'The Area={area}\nPerimeter={perimeter}')




# method2
# A
# |\
# | \
# |  \
# |   \
# |    \
# B|_____\C    
import math
AB=float(input("Enter the first side ->"))
BC=float(input("Enter the second side ->"))
AC=math.sqrt(AB**2+BC**2)
area=0.5*AB*BC
perimeter=AB+BC+AC
print("The area is %.2f\nThe perimeter is %.2f"%(area,perimeter))
