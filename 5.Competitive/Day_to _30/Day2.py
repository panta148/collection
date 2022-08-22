"""
Height and weight converter
#########################################################
input-1 
Enter the height feet part:5
Enter the height inch part:11
Enter the weight in kg:60
output
Height in cm:34
weight in pound:132.0

input-2
Enter the height feet part:5
Enter the height inch part:0
Enter the weight in kg:101
output
Height in cm:152.4
weight in pound:222.2


hints:
1 inch is equal to 2.54cm. 
1 Foot = 12 Inches(1 ft = 12)

1 meter = 100 cm = 1,000 mm
1 foot = 12 inches, 1 inch = 2.54 cm
12 x 2.54 = 30.48
1 foot is equal to 30.48 cm, 1 cm is equal to 0.032808399 feet


one kilo of mass is equal to 2.26lbs
"""
foot=int(input("Enter the height foot part ->"))
inch=int(input("Enter the height in inch part->"))
weight=int(input("Enter the weight in kg ->"))
# inch=foot*12
# cm=inch*2.54
cm1=foot*30.48
cm2=inch*2.54
cm=cm1+cm2
pound=weight*2.26
print(f'Height in cm={cm}\n Weight in pound={pound}')