# in this program we transverse through the list 
number=[22,56,78,9,234,678,123,456,789]
small=number[0]
large=number[0]
for i in number:
    if i >large:
        large=i
    if i<small:
        small=i    
print("the largest number  in the list is ",large)  
print("the small number  in the list is ",small)  
