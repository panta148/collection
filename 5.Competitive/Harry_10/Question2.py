"""
title:divide the apple
you have got a n number of apple and you have some friend among whom you want to distribute the apple
if not evenly distributed you can request more or  few
you need to print whether a numbe in  range min and max is divisor or not
input:
take input n mn,mx from user
output:
print whether the number between mn and mx isa divisor by n or not

example:
if n=20,mn=2 abd mx=5
2 is divisor by 20
3 is not divisor by 20
.
.
.
.
"""


def not_clear():
    n = int(input("Enter n->"))
    mn = int(input("Enter the minimum number ->"))
    mx = int(input("Enter the maximum number ->"))
    for i in range(mn, mx+1):
        # print(i)
        if n % i == 0:
            print(f'{i} is divisor by {n}')
        else:
            print(f'{i} is not  divisor by {n}')
print("Thanks ")



if __name__ == '__main__':
    # not_clear()
    n=int(input("How man apple do you have ->"))
    number=int(input("How many friends do you have->"))
    if n%number==0:
        print(f'Congras you can evenly distribute the available apple amongs the friends with {n//number} each')
    else:
        print("sorry you have to do somethings :::)")
             
    

 




