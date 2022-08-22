'''
pattern printed task 
if you enter 1 then increasing pattern will be shown or if you enter 0 then decending order start pattern will
be shown according to the height of the pattern you have enter.

*                    *****
**                   ****
***                  ***
****                 **
*****                *
N=5                 N=5
'''
print("\n\n\n*********************************************\n")
count = int(input("Enter the height of the pattern -> "))
pattern = int(input("enter 1 for or 0 ->"))
print()
if pattern == 1:
    for i in range(1, count+1):
        for j in range(1, i+1):
            print("*", end=" ")
        print()
else:
    for i in range(1, count+1):
        for j in range(1, count+1):
            print("*", end='')
        count -= 1
        print()
