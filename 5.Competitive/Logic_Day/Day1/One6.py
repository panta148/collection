# find the equation of the line (y=mx+b) passing through the two point
x1=int(input("Enter teh X1 of co-ordinate ->"))
x2=int(input("Enter teh x2 of co-ordinate ->"))
y1=int(input("Enter teh y1 of co-ordinate ->"))
y2=int(input("Enter teh y2 of co-ordinate ->"))
m=(y2-y1)/(x2-x1)

# y=mx+b
# b=y-mx
c=y2-(m*x2)
# c=int(input("Enter the y inter-cept ->"))
print(f"The equation of the line is\n y=%.2fX+%.2f"%(m,c))
