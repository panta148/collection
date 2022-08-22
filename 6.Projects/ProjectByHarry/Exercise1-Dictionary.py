""""
this is the program to create the dictionary and give the user to choice the word and
 the program should be able to give the meaning
"""
dic={"happy":"glad","massive":"huge",
     "stuff":"time waste talk"

     }
choice=True
while choice:
    word = input("\n\nEnter the word to search the meaning ..\n-> ")
    for key, value in dic.items():
        if key == word:
            print(dic[word])
            break
        else:
            print(f"Sorry!!currently we did not have the meaning of {word} in our database")
            break

    print("\n\n\t\tThanks for using our dictionary")
    print("if you want to use the dictionary further enter 'y'herwise enter 'n'")
    unit = input()
    if unit=="y":
        choice=True
    else:
        choice=False

