

from stack2 import Stack
s = Stack()

decimal_number = int(input("Enter the deciaml number ->"))
while decimal_number > 0:
    num = decimal_number % 2
    s.push(num)
    decimal_number = decimal_number//2


binary_number = ''
print(binary_number)
while not s.isEmpty():
    binary_number = binary_number+str(s.pop())

print(binary_number)
