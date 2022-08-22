import random
import string
import os
from platform import system
s1=string.ascii_lowercase
s2=string.ascii_uppercase
s3=string.digits
s4=string.punctuation
plen=int(input("Enter the password length you want to generate \n->"))
s=[]
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))

# you can also write like this also too
# s.extend(s1)
# s.extend(s2)
# s.extend(s3)
# s.extend(s4)
# print(s)
random.shuffle(s)
print(s)
print("Your password is \n")
print("".join(s[0:plen])) # it lake th efirst plen sample from the dhuffle list

# you can also write like this also too
# print(" ".join(random.sample(s,plen))) # it work quite differently
if system()=='Windows':
    os.system('cls')
elif system()=="Linux":
    os.system('clear')    
# os.system('cls')    
print(system())

print("\n\n Thanks for generating the password")