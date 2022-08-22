# 1. Write a Python program to print the following string in a specific format (see the output). 
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" 
# Output :

# Twinkle, twinkle, little star,
# 	How I wonder what you are! 
# 		Up above the world so high,   		
# 		Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
# 	How I wonder what you are
p1 = "Twinkle, twinkle, little star,\n\tHow I wonder what you are! "
p2 = "\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky."
p3 = "\nTwinkle, twinkle, little star,"
p4 = "\n\tHow I wonder what you are,"
print(p1+p2+p3+p4)
