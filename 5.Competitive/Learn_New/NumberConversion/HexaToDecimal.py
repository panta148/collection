import math
number=int(input("Enter the Hexa_number to convert to the decimal ->"))
number1=number
sum=0
power=0

while(number!=0):
    digit=number%10
    sum=sum+digit*math.pow(16,power)
    power+=1
    number=number//10
print("The Decimal of %d is %d "%(number1,sum))




exit()
number=[0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']
user_number=list(input("Enter the number "))
if user_number in number:
    print("good")
    print(user_number)
else:
    print("bad")    



