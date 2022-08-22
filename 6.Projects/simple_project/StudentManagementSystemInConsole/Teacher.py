Teacher={1:"Insert",2:"Delete",3:"Update",4:"Search"}
def get_teacher():
    for index, value in Teacher.items():
        print(f'Enter {index} for {value}')
    option=int(input("Enter the choice of above ->"))
    if option==1:
        k='y'
        while (k!='n'):
            name=input("Enter the Teacher name ->")
            Id=input("Enter the ID number ->")
            with open ("teacher.txt","a") as f:
                f.write(f"\n\nName:{name}\n Roll:{Id}")
                print("Data is inserted in file successfully")
            k=input("Add more y/n?")
            continue
    elif option ==2:
        pass
    elif option ==3:
        pass
    elif option==4:
        print("\n\nData on the Teacher file are as follow::::")
        with open("teacher.txt","r+") as f:
            content=f.readlines()
            for item in content:
                print(item,end="")
        print('\n')  
        


    
