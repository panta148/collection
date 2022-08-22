"""
A school has the following rules of grading system
below 25--F
25-45--E
45-50--D
50-60--C
60-80--B
Above 80--A
ask the user to enter the marks and the corresponding grade
"""
def calculate_grade(mark):
    if mark < 25:
        print("Grade=F")
    elif (mark >= 25) and (mark < 45):
        print("Grade=E")
    elif (mark >= 45) and (mark < 50):
        print("Grade=D")
    elif (mark >= 50) and (mark < 60):
        print("Grade=C")
    elif (mark >= 60) and (mark < 70):
        print("Grade=B")
    elif (mark >= 80) and (mark <= 100):
        print("Grade=A")
    else:
        print("Enter the valid percentage ..")


def calculate_percentage():
    english=int(input("Enter the mark in English :"))
    nepali = int(input("Enter the mark in Nepali :"))
    math = int(input("Enter the mark in Math :"))
    science= int(input("Enter the mark in Science :"))
    social = int(input("Enter the mark in Social :"))
    environment = int(input("Enter the mark in Environment :"))
    option_math = int(input("Enter the mark in optional_math :"))
    computer = int(input("Enter the mark in Computer :"))
    total=english+nepali+math+science+social+environment+option_math+computer
    percentage=(total/800)*100
    return percentage





if __name__ == '__main__':
            print("\n\t\t\twel come to student grade management system")
            name=input("Enter the name of the student to see the result :->")
            roll=int(input("Enter the roll number of the student: ->"))
            print("\n\nNow Enter the mark of the student")
            percent=calculate_percentage()
            # mark = int(input("Enter the percentage  of the student :->"))
            print("\n\n\t\t\t .........MarkSheet...")
            print(f'Name:{name}\nRoll:{roll}')
            calculate_grade(percent)


