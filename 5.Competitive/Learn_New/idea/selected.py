# Given list is  [10, 20, 33, 46, 55]
# Divisible of 5 in a list
# 10
# 20
# 55
def Divisible_by_5(llist):
    print("Given list is ",llist)
    print("Divisible of 5 in a list")
    for x in llist:
        if x%5==0:
            print(x)

new_list=[10, 20, 33, 46, 55]
Divisible_by_5(new_list)

exit()
def printEveIndexChar(str):
  for i in range(0, len(str)-1, 2):
    print("index[",i,"]", str[i] )

inputStr = "pynative" 
print("Orginal String is ", inputStr)

print("Printing only even index chars")
printEveIndexChar(inputStr)