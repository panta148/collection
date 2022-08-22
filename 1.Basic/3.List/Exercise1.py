print("Exercise-10")
"""
Exercise Question 10: Given a Python list, remove all occurrence of 20 from the list
list1 = [5, 20, 15, 20, 25, 50, 20]
Expected output:

[5, 15, 25, 50]
"""
print("Exercise-9")
"""
Exercise Question 9: Given a Python list, find value 20 in the list,
 and if it is present, replace it with 200. Only update the first occurrence of a value
list1 = [5, 10, 15, 20, 25, 50, 20]
Expected output:

list1 = [5, 10, 15, 200, 25, 50, 20]
"""
print("Exercise-8")
"""
Exercise Question 8: Given a nested list extend it with adding sub list
 ["h", "i", "j"] in a such a way that it will look like the following list
Given List:

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
Sub List to be added = ["h", "i", "j"]

Expected output:

['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
"""
print("Exercise-7")
"""
Exercise Question 7: Add item 7000 after 6000 in the following Python List
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
Expected output:

[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
"""
print("Exercise-6")
"""
Exercise Question 6: Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
Expected output:

["Mike", "Emma", "Kelly", "Brad"]
"""
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
resList = list(filter(None, list1))
print(resList)
exit()
print("Exercise-5")
"""
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
Expected output:

10 400
20 300
30 200
40 100
"""
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
# list2=list2[::-1]
# count=0
# for x in list1:
#     print(str(x)+" "+str(list2[count]))
#     count+=1
print("New and the most efrective way")    
for x, y in zip(list1, list2[::-1]):
    print(x, y)


print("Exercise-4")
"""
Exercise Question 4: Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
Expected output:

['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
"""
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
# list3=[i+j for i,j in zip(list1,list2)]
# print(list3)
resList = [x+y for x in list1 for y in list2]
print(resList)
print("\nnew way\n")
ll=[]
for x in list1:
    for y in list2:
        ll.append(x+""+y)
print(ll)        






print("Exercise-3")
"""
aList = [1, 2, 3, 4, 5, 6, 7]
Expected output:
[1, 4, 9, 16, 25, 36, 49]
"""
aList = [1, 2, 3, 4, 5, 6, 7]
aList =  [x * x for x in aList]
print(aList)


print("Exercise -2")
"""
Exercise Question 2: Concatenate two lists index-wise


list1 = ["M", "na", "i", "Ke"] 
list2 = ["y", "me", "s", "lly"]
Expected output:

['My', 'name', 'is', 'Kelly']
"""
list1 = ["M", "na", "i", "Ke"] 
list2 = ["y", "me", "s", "lly"]
ll=list( zip(list1, list2))
print(ll)
list3 = [i + j for i, j in zip(list1, list2)]
print(list3)

print("Exercise1")
"""
Exercise Question 1: Given a Python list you should be able to display Python list in 
the following order

aLsit = [100, 200, 300, 400, 500]
Expected output:

[500, 400, 300, 200, 100]

"""
aLsit = [100, 200, 300, 400, 500]
print(aLsit[::-1])
