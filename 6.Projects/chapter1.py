import time
def lession1():
    print('''1.Introduction
    python is one of the maost growing language in the market now a days because of the following application
    1.Desktop Application
    2.Web Application
    3.Machine Learning
    4.Artifiical Intelligent
    5.many more on programming \n\n''')
    time.sleep(5)
    print('''2.variable
    ->it is the bucket or the place which is used to keep the data for the temporary because once we close the 
    program it will automatically clean the mmemory it occupied\n\n
    In python there are manily four type of the variable
    1.Integer
    2.Fraction
    3.String
    4.Boolean\n\n
    lets us amke the project on variable which take the two number and do the basic mathematical operation\n\n
    ''')
    time.sleep(5)
    num1=int(input('Enter the first number ->'))
    num2=int(input('Enter the second number ->'))
    d=input("Choose +,-,*,?,%")
    if d=='+':
        print(f'{num1}{d}{num1}=',num1+num2)
    elif d=='-':
        print(f'{num1}{d}{num1}={num1}-{num2}')  
    elif d=='*':
        print(f'{num1}{d}{num1}={num1}*{num2}')
    elif d=='/':
        print(f'{num1}{d}{num1}={num1}/{num2}')
    elif d=='%':
        print(f'{num1}{d}{num1}={num1}%{num2}')   

    print("Thank you for the operation") 
    time.sleep(5)              

    
    
