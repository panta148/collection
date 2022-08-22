from array import array
a = array('i', [])
n = int(input("Enter the number of item to be enter   "))
for j in range(n):
    num = int(input(f"Enter the {j+1} Number "))
    a.append(num)


print("       ")
print("New array.......")
for i in a:
    print(i)

print("Ending")
