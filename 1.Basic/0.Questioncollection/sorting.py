# sorting in python
a = [100, 6, 555, 9, 334, 30]
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            temp = a[j]
            a[j] = a[i]
            a[i] = temp


print("Final list after assending ")
print(a)
