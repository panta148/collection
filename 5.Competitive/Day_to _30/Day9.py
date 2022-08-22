# Count the diggit in power
"""
WAP which take tthe two inter input lets say a and b and calculate a**b
now it is the time to count the diggit in the power
lets try top solve the problems without using the loop

input;
Enter 1st number:5
Enter 2nd number:2
output;
Digit Count:2


Enter 1st number:999
Enter 2nd number:0
output;
Digit Count:1
Explanation:5^2=25
Number of digit in 25:2

Enter 1st number;999
Enter 2nd number:99
output;
Digit Count:297
"""
a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
c=a**b
count=len(str(c))
print("Digit Count:",count)
