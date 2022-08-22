 
import time
def problems1():
    """
    print Hello,World!   
    """
    print("\nThis is simple print hello world  part\n")
    print("Hello , World !")
    time.sleep(5)

def problems2():
    """
    take the two input from the user and use the operator / and //
    and finnd the difference between them
    """
    print("\nthis is simple difference between the / and // operator")
    num1=int(input("\n\nEnter the first number-> "))
    num2=int(input("Enter the second number-> "))
    print(f'{num1/num2}  this will display the floating number \n{num1//num2} this will display integer number')
    time.sleep(5)


def problems3():
    """
    arithmetic operation on python
    """   
    print("\nThis is simple arithmetic calculation in python")
    num1=int(input("\n\nEnter the first number-> "))
    num2=int(input("Enter the second number-> "))
    print(num1+num2)
    print(num1-num2)
    print(num1*num2)
    time.sleep(5)

def problems4():
    """
    python if else statement
    take the integer from the user and ;
    if n is odd print weired
    if n is even and the inclusive range of 2 to 5 , print not weired
    if n is even and the inclusive range of 6 to 20 ,print weired
    if n is even and the greater than 20 print not weired"""
    print("\nThis is simple python if else statement")   
    n=int(input("Enter the number ->"))
    if n%2!=0:
        print("weired")
    else:
        if n>=2 and n<=5:
            print("not weired")
        elif n>=6 and n<=20:
            print("weired")
        else: 
            print(" not weired")  
    time.sleep(5) 


def problems5():
    """
    with out using any string methhod, try to print if user ente any interger let say n..
    you have to print 123......n
    """
    print("\nIn this part number from 1 to user enter number will be display")
    n=int(input("\nEnter any integer nummber you want to print the number from 1 to that number ->"))
    for i in range(1,n+1):
        print(i,end=" ")
    time.sleep(5)    

def problems6():
    """
    take the any integer from the user
    lets n=5
    output:
    0
    1
    4
    9
    16
    i.e square of the number
    """
    print("\nThis will dispaly simply the square of the number from 0 to num-1")
    num=int(input("Enter the number you want -> "))
    for i in range(num):
        print(i*i)
    time.sleep(5)    

def problems7():
    print("\nhello every this is leap year calculation part ")
    year=int(input("Enter the year you want to check for the leap year->"))
    if year%4==0:
        if year%100==0 and year%400==0:
            print("Hello nepal")
            print(f'{year} is a leap year')
        else:
            print(f"{year} is not leap year")    
    else:
        print(f'{year} is not a leap year')  
          
    time.sleep(5) 



if __name__ == '__main__':

       while True:
        print("\n\n\t\t\tWel come to string solution ")
        print("Enter 1 for problems1")
        print("Enter 2 for problems2")
        print("Enter 3 for problems3")
        print("Enter 4 for problems4")
        print("Enter 5 for problems5")
        print("Enter 6 for problems6")
        print("Enter 7 for problems7")
        
        print("Enter 0 for exit")
        option=int(input("\nEnter the option mention above-> "))
        if option==1:
           problems1()
        elif option==2:
            problems2()  
        elif option==3:
            problems3()  
        elif option==4:
            problems4()  
        elif option==5:
            problems5()
        elif option==6:
            problems6()  
        elif option==7:
            problems7()                        
        elif option==0:
           exit()
        else:
            print("Enter the valid option ..")  

        print("Thanks for using ....\nhope to see you later...")              
