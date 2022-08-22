"""
this is the sanke ,water and gun game so play well to be the winner
"""
import random
listt=['s','w','g']
def Computer():
    return random.choice(listt)

def logic():
    global total
    global computer
    global human
    c=Computer()
    h=input("Enter the choice \n 1 for snake\n2 for water\n3 for gun \n->")
    # if computer have choice snake
    if c=='s':
        total-=1
        if h==1:
            print("Draw the game ")
        elif h==2:
            computer+=1
            print(f"Computer won the game\n your point={human}\n computer point={computer}\n")  
        elif h==3:
            human+=1
            print(f"You  won the game\n your point={human}\n computer point={computer}\n") 
    elif c=='w':
        total-=1
        if h==1:
            human+=1
            print(f"You  won the game\n your point={human}\n computer point={computer}\n")
            
        elif h==2:
             print("Draw the game ")
              
        elif h==3:
            computer+=1
            print(f"Computer won the game\n your point={human}\n computer point={computer}\n")
           
    elif c=='g':
        total-=1
        if h==1:
            computer+=1
            print(f"Computer won the game\n your point={human}\n computer point={computer}\n")
            
        elif h==2:
            human+=1
            print(f"You  won the game\n your point={human}\n computer point={computer}\n")
              
        elif h==3:
            print("Draw the game")
    else:
        print("Invalid option")        
                    

if __name__ == '__main__':
    print('\n\n\n\n\t\t\t\t\twelcome to our game ')
    total=10
    human=0
    computer=0
    while total!=0:
        logic()
