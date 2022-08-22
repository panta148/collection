# program to check whether the number is palindrome or not\
"""
number=int(input("Enter the number to check ->"))
print(number)
count=0
nnum=number
while number!=0:
    num=number%10
    number=number//10
    count=count*10+num
print(count)
if count==nnum:
    print(f'{nnum} is palindrone number')
else:
    print(f'{nnum} is not  palindrone number')
"""
print("check the palindrome string or not\n\n\n")
word=input("Enter the word to check the palindrome :->")
# first method as in thsi method we directly reverse the string 
"""
nword=word
cword=word[::-1]
if cword==nword:
    print(cword==nword)
    print('palindrome')
else:
    print('not palindrome')  
    """
# second method    
nword=word 

            

