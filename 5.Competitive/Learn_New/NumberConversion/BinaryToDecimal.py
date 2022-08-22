import math
b_num = list(input("Input a binary number: "))
value = 0

for i in range(len(b_num)):
	digit = b_num.pop()
	if digit == '1':
		value = value + pow(2, i)
print("The decimal value of the number is", value)





exit()



number=int(input("Enter the binary number to convert to the decimal ->"))
number1=number
sum=0
power=0

while(number!=0):
    digit=number%10
    sum=sum+digit*math.pow(2,power)
    power+=1
    number=number//10
print("The Decimal of %d is %d "%(number1,sum))    
