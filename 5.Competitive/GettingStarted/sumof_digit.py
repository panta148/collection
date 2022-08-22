"""
take the positive number from the user and print the sum of all the digit of the number
"""
number=int(input("Enter the number to calculate the sum of the digit\n:-->"))
num=number
sum=0
while number!=0:
    digit=number%10
    sum=(sum+digit)
    number=number//10

print(f"The sum of all the digit of the number {num} is {sum} ")


