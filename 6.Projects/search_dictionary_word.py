# pip install PyDictionary
from PyDictionary import PyDictionary
dict=PyDictionary() #making the object oof PyDictionary class
meaning=dict.meaning(input("Enter the word :: ->")) #extracting the meaning off the given word
print(f'\n\n\n{meaning}')