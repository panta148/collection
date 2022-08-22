"""
switch case us not  available in the python we should used if else ladder instead of switch case
"""
#it will print only the odd number
for i in range(1,101):
    if i%2==0:
        continue
    print(i)

print("\n\nWe used break statement to break the loop when i is equal to 6")
i=0
while i<10:
    i+=1
    if i==6:
        break
    print(i)


