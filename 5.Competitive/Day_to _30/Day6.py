"""
exchhange character in string
due to the mistake few cjaractere are excahnnge so we need to fix it with the help of the progeam

wwrite a program  which the two user input string and yyou have 
to exchange the first two character of the first string with the last 2 character 
of the second string. same things must have to be done to the both string
note; use of the loop is not allowed

lenght of the both string altest 4 and output string should be store in variable before printing it

input:
string1:abcdefqwa
string2:gfdkghye
output
string1:yecdefqgf
string2:wadkghab

here ab is exchange with ye and wa is exchange with gf


string1:abcd
string2:efgh
output
string1:ghef
string2:cdab
"""
string1=input("String 1 :")
string2=input("String 2 :")
a=string1.replace(string1[:2],string2[-2:])
b=a.replace(a[-2:],string2[:2])
print("New string..after the exchange of the string")
print("string1 :",b)
a=string2.replace(string2[:2],string1[-2:])
b=a.replace(a[-2:],string1[:2])
print("string2 :",b)
print('Thanks you man,,')


