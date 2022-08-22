
# importing user define module
from stack2 import Stack
s = Stack()
print("enter the character one by on\n")
print("Enter 0 to Exit\n")

while True:
    c = input()
    if c == 0 or c == '0':
        break
    s.push(c)


print(" After Reversing")
reverse = ''
while s.size() != 0:
    reverse = reverse+str(s.pop())
print()
print(reverse)
