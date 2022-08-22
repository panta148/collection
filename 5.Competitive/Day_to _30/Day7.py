# Generate the HTML tags
"""
write the program which take the four string from the user
first string as the tag name second onward string will be values/text inside the tag,
 you have to generate the html tag for the same
 lets us suppose the tag inpyt is "i"
 you have to make the tag as <i>value</i>
 note: using loop is not allowed
 tag name must not be empty but the values can be empty
 output string must be pace in varioable before printing it

 input:
 tag name:b
 string1:amrit
 string2:panta
 string3:name
 output:
 <b>amrit</b>
 <b>panta</b>
 <b>name</b>



"""
tag=input("Tag name :")
string1=input("String 1 :")
string2=input("String 2 :")
string3=input("String 3 :")
print(f'<{tag}>{string1}</{tag}>\n<{tag}>{string2}</{tag}>\n<{tag}>{string3}</{tag}>')