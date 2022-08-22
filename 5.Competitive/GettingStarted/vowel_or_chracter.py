"""
 take the character form the user and display vowel or consonant if the user input is not from [a-z] and
 [A-Z] or the length of the string >1 display error message
"""
while 1:
    character = input("Enter the character you want ot check for the vowel or consonant\n ->")
    character = character.lower()
    if character in ['a', 'e', 'i', 'o', 'u']:
        print(f'{character} is vowel ..')
    elif character.isnumeric():
        print(f'{character} is number..\n please enter the english alphabets')
    elif len(character) > 1:
        print("you have enter the string\n so enter the character only")
    else:
        print(f'{character} os consonants')
    print("Enter 'c' to continue and 'q' to quit'")
    char = input()
    if char == 'c':
        continue
    elif char == 'q':
        exit()
    else:
        print("enter teh correct option")


