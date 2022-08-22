import re
student = {1: "Insert", 2: "Delete", 3: "Update", 4: "Search",5:"Show all data"}
def get_student():
    for index, value in student.items():
        print(f'Enter {index} for {value}')
    option=int(input("Enter the choice of above ->"))
    if option==1:
        k='y'
        while (k is not'n'):
            name=input("Enter the student name ->").capitalize()
            roll=input("Enter the roll number ->")
            with open ("student.txt","a") as f:
                f.write(f"\n\nName:{name}\n Roll:{roll}")
                print("Data is inserted in file successfully")
            k=input("Add more y/n?")
            continue
    elif option ==2:
       pass
    elif option ==3:
        word=input("Which word do you want to updat->")
        new=input(f"enter the new word to change {word} in data ->")
        with open("student.txt", 'r+') as f:
            text = f.read()
            text = re.sub(word,new, text)
            f.seek(0)
            f.write(text)
            f.truncate()
        print("Successfully updated")    
        
    elif option==4:
        name=input("\n\nEnter the name of student the search ->").capitalize()
        with open("student.txt") as f:
            for line in f:
                for part in line.split():
                    if name in part:
                        print(part,end="")
                        
        
    elif option==5:
        print("\n\nData on the Student file are as follow::::")
        with open("student.txt","r+") as f:
            content=f.readlines()
            for item in content:
                print(item,end="")
        print('\n')        
get_student()