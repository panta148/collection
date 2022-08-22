# calculate the sum of the digit of the three random number
from random import random
n=random()*900
n=int(n)
print(n)
a=n//100 #taking the first digit
print(a)
print(n//10)
b=(n//10)%10
print(b)

c=n%10
print(c)
print(a+b+c)
