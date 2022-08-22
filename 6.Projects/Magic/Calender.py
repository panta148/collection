import calendar
yy=int(input("Enter the year :"))
mm=int(input("Enter the month  :"))
print(f'Year:{yy}\nMonth:',end=' ')
print(calendar.month(yy,mm))