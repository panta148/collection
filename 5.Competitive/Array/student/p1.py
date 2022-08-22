arr = [1, 3, 2, 4, 6, 7, 6]
# for item in range(0, len(arr), 2):
#     print(arr[item], end=' ')

# print(len(arr))
# for i in range(0, len(arr), 2):
#     print(arr[i], end=" ")




def valueEqualToIndex(arr):
    for i in range(1,len(arr)):
        if i == arr[i]:
            print(arr[i])

valueEqualToIndex(arr)

