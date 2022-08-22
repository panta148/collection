"""
swapping the two number
"""
import time
print("method 1 ")
number1=int(input("Enter the first number: "))
number2=int(input("Enter the second number: "))
print(f'Number before swapping\nNumber1={number1}\nNumber2={number2}')
temp=number1
number1=number2
number2=temp
print(f'Number after swapping\nNumber1={number1}\nNumber2={number2}')



print("\n\nwait 3 second to see the method 2(python method) \n\n")
time.sleep(3)


print("method 2 ")
number1=int(input("Enter the first number: "))
number2=int(input("Enter the second number: "))
print(f'Number before swapping\nNumber1={number1}\nNumber2={number2}')
# temp=number1
# number1=number2
# number2=temp
number1,number2=number2,number1
print(f'Number after swapping\nNumber1={number1}\nNumber2={number2}')

