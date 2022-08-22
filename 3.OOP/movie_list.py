# object and class 
class Movie:
    def __init__(self,moviename,hero,heroine):
        self.moviename=moviename
        self.hero=hero
        self.heroine=heroine
    def info(self):
        print('')
        print("Movie Name:",self.moviename)    
        print("Hero:",self.hero)    
        print("Heroine:",self.heroine)
        print('')

movie_list=[]
while True:
    print("Wel come to the movie management system\n")
    movie=input("Enter the movie name:")        
    hero=input("Enter the Hero name:")        
    heroine=input("Enter the Heroine name:") 
    w=Movie(movie,hero,heroine)
    movie_list.append(w)
    option=input("\nDo you want to enter more . [y/n]")
    if option.lower()=='n':
        break
print("################# Your list of movie #######################")
for i in movie_list:
    i.info()


    




