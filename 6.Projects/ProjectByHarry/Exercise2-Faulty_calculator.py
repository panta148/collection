"""
Remember that:::
in this calculator you will find the following fault:
5+3=15
5-1=10
7*4=4
so check the result more precisely..

"""

def calculate_result(num1,num2,c):
    if c=='+':
        if num1==5 and num2==3:
            print(f'{num1}+{num2}::15')
        else:
            print(f'{num1}+{num2}::{num1+num2}')

    elif c=='-':
        if num1 == 5 and num2 == 1:
            print(f'{num1}-{num2}::10')
        else:
            print(f'{num1}-{num2}::{num1-num2}')
    elif c == '*':
        if num1 == 7 and num2 == 4:
            print(f'{num1}*{num2}::4')
        else:
            print(f'{num1}*{num2}::{num1*num2}')
    elif c == '/':
        print(f'{num1}/{num2}::{num1/num2}')
    elif c == '%':
        print(f'{num1}%{num2}::{num1%num2}')
    elif c == '**':
        print(f'{num1}**{num2}::{num1**num2}')
    else:
        print("Invalid operator ..choice the correct one to perform")




choice=True
while choice:
    try:
        num1=int(input("Enter the first number:->"))
        operator=input("Enter the operator you want to do\n'+'\t'-'\t'*'\t'/'\t'%'\t'**'\n:->")
        num2 = int(input("Enter the second number:->"))
        calculate_result(num1,num2,operator)
        print("\n\t\t\t:Thanks for using our calculator")


    except Exception as e:
        print(e)

    print("Enter the 'y' to continue and press any key to exit from the program")
    unit=input()
    if unit=="y":
        choice=True
    else:
        choice=False