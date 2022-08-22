"""
this is the guessing number game ..play well and win the more point
we will make more advance to this program
"""
import random
import sys
condition=True
def Guess_number_Result():
    secrete_number=random.randint(1,50)
    limit=5
    count=0
    while count<limit:

        num = int(input("\n\nEnter the secrete number from 1 to 50..->"))
        if num==secrete_number:
            print(f"you won the game in {count} step ")
            break
        else:
            if num>secrete_number:
                print(f'{num} is greater than secrete number..\nso Enter the lesser number')
            else:
                print(f'{num} is lesser than secrete number..\nso Enter the greater number')
        count += 1
    else:
        print("\n\nSorry you loss the game....Try again ")
        print(f' correct number was = {secrete_number}')



if __name__ == '__main__':
    print("..................Wel come to guess_number game.........\n you have 5 step to win the game ")

    while condition:
        try:

            Guess_number_Result()

        except Exception as e:
            print(e)

        unit = input("\n\nEnter 'y' to continue and press any key to exit from the game")
        if unit == "y":
            condition = True
        else:
            sys.exit()
