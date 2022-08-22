import sys
from login import get_data
from Student import get_student
from Teacher import get_teacher
dic1={1:"Student",2:"Teacher",3:"Other staff",0:"EXIT"}
if __name__ == '__main__':
    print("\n\n\t\tWel come to student management System\n\n")
    while 1:
        if get_data():
            while 1:
                print("\n")
                for index,value in dic1.items():
                    print(f'Enter {index} for {value}')
                option=int(input("Enter the choice of above ->"))
                if option ==1:
                    get_student()   
                elif option==2:
                    get_teacher()
                elif option==3:
                    print("for the staff our work is not finish yet") 
                elif option==0:
                    sys.exit()
        else:
            continue            
         
                  
        
           
   
    
