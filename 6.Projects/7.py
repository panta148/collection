'''
8. Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
'''
color=input("Enter color name separate by comma->\n")
color_list=color.split(",")
print("First and Last color fromm the list is as below:\n")
print("%s %s"%(color_list[0],color_list[-1]))