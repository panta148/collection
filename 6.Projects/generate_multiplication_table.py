print('\n\t\t\tWel come to the multiplication generation software\n')
num=int(input('Enter the number you want to generation multiplacation table \n->'))
end=int(input('Enter the number upto which you want to generate the table \n->'))
print("Table is gioven below::")
for i in range(1,end+1):
    print(f'{num}*{i}={num*i}')