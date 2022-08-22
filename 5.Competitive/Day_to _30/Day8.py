# insert in middle of string
"""
writ the program to take the string of even length and second string of any numbe of character
generate the output with the secoond string inserted in the middle os the firststring

use of loop is  not allowed 
store the output in the variable before printing it
input;
first string:[[]]
second;amrit
output:[[amrit]]

input;
first string:{{{}}}
second;panta
output:{{{panta}}}
"""
string1=input("'First String :")
string2=input("Second string :")
c=len(string1)
print(string1[:c//2]+f"{string2}"+string1[c//2:])
