"""
take positive integer from the user and print the  reverse  of the number
"""
number=int(input("Enter the number to reverse the digit of number :\n->"))
num=number
sum=0
while number!=0:
    digit=number%10
    sum=sum*10+digit
    number=number//10

print(f'The Reverse of the number {num} is {sum} ')
# print(sum)