"""
convert ssecond to the time

user will enter the timin seconds and you have to show thw second in the form of day,hour,minute and second

input
Enter the second:
360000
output
4 days 4 hour 0 minute 0 second


input
Enter the second:
36123
output
0 days 10 hour 2 minute 3 second


input
Enter the second:
2500
output
0 days 0 hour 41minute  40second
"""
second=int(input("Enter the second :"))
days=second//(24*60)
hour=days//24
minute=hour//60
second=minute//60
print(f'{days} days {hour} hour {minute} minute  {second} seccond')