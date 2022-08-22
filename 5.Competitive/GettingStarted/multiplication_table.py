"""
take the user input and display the table
"""
num=int(input("Enter the number to find the table :->"))
step=int(input("Enter up to which term do you need the multiplication table:-> "))
print("\n\n")
for i in range(1,step+1):
    print(f'{num}*{i}={num*i}')
i=1
print("now  using the while loop")
while i<=step:
    print(f'{num}*{i}={num * i}')
    i+=1


print("\n\nThanks for using our software")
