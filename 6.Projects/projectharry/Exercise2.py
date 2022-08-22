"""
this is the feaulty calculator , following are the fault that the calculator will make 
45*3=555
56+9=77
66/6=4

so lets start....
"""


def menu():
    print("\n\n\t\t\tEnter 1 for addition")
    print("\t\t\tEnter 2 for subtraction")
    print("\t\t\tEnter 3 for multiplication")
    print("\t\t\tEnter 4 for division")
    print("\t\t\tEnter 0 for exit")
    option = int(input("Enter the option ->  "))
    return option


print("\n\n\n\t\t\tSimple Calculator......")

while 1:
    try:
        choice = menu()
        if choice == 0:
            break
        num1 = int(input("\n\nEnter first number -> "))
        num2 = int(input("Enter second number -> "))
        result = 0
        if choice == 1:
            if (num1 == 56 and num2 == 9) or (num1 == 9 and num2 == 56):
                result = 77
            else:
                result = num1+num2
        elif choice == 2:
            result = num1-num2
        elif choice == 3:
            if (num1 == 43 and num2 == 3) or (num1 == 3 and num2 == 43):
                result = 555
            else:
                result = num1*num2
        elif choice == 4:
            if (num1 == 66 and num2 == 6):
                result = 4
            else:
                result = num1/num2
        else:
            print("Enter the correct option menntion as above")
        print(f"\n\n\t\tResult: {result}")

    except Exception as e:
        print("\n Enter the number only as the input , you have enter other character ...")


print("\n\nthank you have a good day !!!!!")
