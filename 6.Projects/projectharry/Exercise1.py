"""
this is simple dictionay in which you search the meaning of of the word by enter the user input
"""
print("\n\n\n\n\t\t\t\tWelcome to our dictionary")
my_dict = {
    "happy": "joyful",
    "sad": "upset",
    "important": "significant",
    "feature": "characteristic",
    "top": "submit"
}
while 1:
    word = input(" \n\t\t\t\tEnter the word for finding the meaning \n :->  ")
    if word in my_dict:
        print(f'The meaning of {word} is {my_dict[word]}')
    else:
        print(
            f" sorry ! {word} is not found in our dictionary \n Try with other words.")
    q = int(input("Enter 1 for Stop the program and 0 for continue \t:  "))
    if q == 1:
        break
