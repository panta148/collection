"""
compute the product from 1 to 11,1 to 12, 1 to 13 and 1 to 14
write down the product obtain and decide if the result are correct
hint:
factorial of 13(=6227020800) is the out of the range of  int[-2147483648,2147483647] take note that computer program may
not produce the correct result though the code is correct
"""
import time
print("Method 1 to calculate the factorial of the number")
num=int(input("Enter the number to calculate the factorial..\n:->"))
product=1
for i in range(1,num+1):
    product*=i
print(f'The factorial of {num} is {product}')

print("Wait 3 second to see the method 2")
time.sleep(3)
print("Method 2")
def calculate_factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*calculate_factorial(num-1)


num=int(input("Enter the number to calculate the factorial..\n:->"))
answer=calculate_factorial(num)
print(f'The factorial of {num} is {answer}')
