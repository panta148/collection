import math
b_num = list(input("Input a octal number: "))
value = 0
number = [0, 1, 2, 3, 4, 5, 6, 7]
for i in range(len(b_num)):
    digit = b_num.pop()
    if digit in number:
        print(digit)
        value = value + digit*pow(8, i)
print("The decimal value of the number is", value)
exit()


number = int(input("Enter the octal number to convert to the decimal ->"))
number1 = number
sum = 0
power = 0

while(number != 0):
    digit = number % 10
    sum = sum+digit*math.pow(8, power)
    power += 1
    number = number//10
print("The Decimal of %d is %d " % (number1, sum))
