yearAge=int(input("enter your age: "))
isAge=False
isYear=False
if yearAge<125:
    isAge=True

elif yearAge>1990:
    isYear=True
elif yearAge<1900:
    print("you seem to be oldest person alive")
elif yearAge>2020:
    print("you are not born yet all")
else:
    print("your age have the problems please enter the correct format ")
    exit()

if isAge:
    yearAge=2020-yearAge
print(f"you will be 100 year after {yearAge+100} year")


