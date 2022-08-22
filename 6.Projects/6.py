'''
7. Write a Python program to accept a filename from the user and print the extension of that. 
Sample filename : abc.java
Output : java
'''
file=input("Sample filename : ->")
extension=file.split(".")
print(extension)
print(repr(extension[-1]))


pass
'''
6. Write a Python program which accepts a sequence of comma-separated numbers from user and
 generate a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
'''
values = input("Input some comma seprated numbers : ")
lists = values.split(",")
# print(lists)
tuples = tuple(lists)
print('List : ',lists)
print('Tuple : ',tuples)


