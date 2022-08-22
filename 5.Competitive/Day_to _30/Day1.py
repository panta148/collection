"""

write the program to take the price of the 3 product for the restaurant bill and the tax percentage from 
the user and calculate the final amount
tax amount=(tax percent/100)*poduvt price
sample input:
enter the price1:70
enter the price3:20
enter the price3:10
enter he tax %:18
output:
Finam amount:118

"""
price1=int(input("Enter the price1 ->"))
price2=int(input("Enter the price2 ->"))
price3=int(input("Enter the price3 ->"))
total=price1+price2+price3
tax_percent=int(input("Enter the tax percent of the restaurant ->"))
300
tax_amount=(tax_percent//100)*total
print(f'Final amount->:{total+tax_amount}\n\n')