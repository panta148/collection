from chapter1 import lession1
def showmenu():
    print("*************************************************")
    for i in range(1,6):
       print(f"Enter {i} to chapter {i}")
    print("\nEnter the correct option you want-> ")
    option = int(input())
    return option
def show1():
    print("wel come to the new world")
def chapter1():
    print('''welcome to chapter 1:::\n we will learn the following topices in this chapter\n
    1.introduction
    2.variiable
    3.datatype
    4.input/output
    5.operator
    6.conditional statement
    7.loop
    8.function
    9.project1
    10.project2
    ''')
    hah=input("Enter any key to sttart the lession ->")
    lession1()
def chapter2():
    print('''welcome to chapter 2:::\n we will learn the following topices in this chapter\n
    1.list
    2.tuples
    3.sets
    4.dictionary
    5.project on list
    6.project on tuples
    7.project on sets
    8.project on dictionary
    9.project1
    10.project2
  ''')    
def chapter3():
    print('''welcome to chapter 3:::\n we will learn the following topices in this chapter\n
    1.class/object
    2.Encapsulation
    3.Data Hinding
    4.inheritance
    5.polymerphism
    6.project1
    7.project2

  ''')    
def choice():
    option = showmenu()
    if option == 1:
        chapter1()
    elif option == 2:
        chapter2()
    
    elif option == 3:
        chapter3()
        
    elif option == 4:
        show1()
        
    elif option==5:
        show1()
          

if __name__ == '__main__':
    while 1:
        choice()
        op=input("do you want to continue or not(Y/n)")
        if op=='y':
            continue
        else:
            break
  
        
