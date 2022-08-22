"""
take the integer input from the user and then convert to the boolean and if boolean is True then print
*
**
***
****
*****
if boolean condition is False, print
*****
****
***
**
*
"""
choice=True
while choice:
    number = int(input("Enter the 0 or 1 to see the different pattern :->"))
    In_boolean_form = bool(number)

    while In_boolean_form:
        lit = [1, 2, 3, 4, 5]
        for i in lit:
            output = ''
            for count in range(i):
                output += '*'
            print(output)
        break

    else:
        name = [5, 4, 3, 2, 1]
        for i in name:
            output = ''
            for count in range(i):
                output += '*'
            print(output)

    print("\n\n\t\tThanks ")
    print("if you want to use  further enter 'y' otherwise enter 'n'")
    choice = input()
    if choice=="y":
        choice=True
    else:
        choice=False
