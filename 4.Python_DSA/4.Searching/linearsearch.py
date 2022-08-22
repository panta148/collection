"""

Searching Algorithms are designed to check for an element or retrieve an element from any data structure where it is stored. Based on the type of search operation, these algorithms are generally classified into two categories:

Sequential Search: In this, the list or array is traversed sequentially and every element is checked. For example: Linear Search.
Interval Search: These algorithms are specifically designed for searching in sorted data-structures. These type of searching algorithms are much more efficient than Linear Search as they repeatedly target the center of the search structure and divide the search space in half. For Example: Binary Search.

https://www.geeksforgeeks.org/linear-search/

"""
print("linear searching....")


def linearSearch(list, element):
    count = 0
    for i in range(len(list)):
        if list[i] == element:
            print(f"{element} is found in {i+1} position")
            count += 1

    if count == 0:
        print(f'{element} is not found ...')


list = []
n = int(input("\n\nHow many element do you want to enter in list ?"))
print(f"Enter {n} element:")
for i in range(n):
    num = int(input(f"Enter {i+1} element :=> "))
    list.append(num)
print()
print()
element = int(input("Enter the element you want to search \n-> "))
linearSearch(list, element)


