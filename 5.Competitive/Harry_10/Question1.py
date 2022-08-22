"""
title:you will become 100 year 
take the age or the date of the birth from the user and tell them when they will turn 100 year 

then can optionally provide the yearr and 
then program will be able to tell the user their age in the particular year


handle the error like
1.you are not born yet
2.you seem to be the oldest person
3.other erroe if possible

"""
def age_at_particuler_year(age):
    newyear=int(input("Enter the  year to calculate the age ->"))
    newage=newyear-2020+age
    print(f'{name} your age at {newyear} will be {newage}')

yes=True
while yes:
    name=input("Enter you your name ->")
    age=int(input("Enter youe age or the date of birth ->"))
    if len(str(age))>3:
        if age>2020:
            print("sorry vai you are not born yet :::))))")
            exit()
        age=2020-age
        print(age)
    if age>=1 and age<100:
        birth_year=2020-age
        
        print(birth_year)
        print(f'{name} you will become 100 year in {birth_year+100} year')
        print("\n\nIf you want to know the age in particular year press 1 ->")
        ch=int(input())
        if ch==1:
            age_at_particuler_year(age)

    else:
        print("Enter the valid  age ")    
    print("you want to run the game again y/n ")
    choice=input()
    if choice=='n':
        yes=False
    continue        