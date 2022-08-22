# the digit are represent as the symbol and then find the sum and the differencen1he first
n1=input("Enter the first number(0--9) ->")
n2=input("Enter the second number(0--9)-> ")
# n1="5"
# n2="6"
a=ord(n1)
b=ord(n2)
# print(a,b)
actual_n1=a-ord('0')

actual_n2=b-ord('0')
# print(actual_n1,actual_n2)
sum=actual_n1+actual_n2
diff=actual_n1-actual_n2
print("%s+%s=%d"%(n1,n2,sum))
print("%s-%s=%d"%(n1,n2,diff))
