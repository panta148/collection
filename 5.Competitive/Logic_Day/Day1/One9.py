# get the random integer and the float number in given range

from random import random,randint
print("range of the integer :")
imin=int(input("->"))
imax=int(input("->"))
n=randint(imin,imax)
print("%d"%n)

print("range of the float :")
fmin=float(input("->"))
fmax=float(input("->"))
n=random()*(fmax-fmin)+fmin
print("%.3f"%n)