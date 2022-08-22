import time
def String_capatailze():
    sentence = input("\n\nEnter the sentence you want ->")
    sentence = (sentence.split(" "))

    for item in sentence:
          print(item.capitalize(), end=" ")
    time.sleep(5)        

def swapcase():
    sentence = input("\n\nEnter the sentence you want ->")
    for item in sentence:
        if item.islower():
            print(item.upper(),end='' )
        elif item.isupper():
            print(item.lower(),end="" )
        elif item.isspace:
            print(' ',end="")
        elif item is '.':
            print(".")    
    time.sleep(5)          


                     
def textWrap():
    text=input("Enter the text ->")
    wrap=int(input('Enter the number to divide the text in the certain number paragraph ->'))
    count=0
    for item in text:
        
        if count==wrap:
            count=0
            print("")
        print(item,end="")  
        count+=1
        
    time.sleep(5)    
        

    


if __name__ == '__main__':
   while True:
        print("\n\n\t\t\tWel come to string solution ")
        print("Enter 1 for capatalize function")
        print("Enter 2 for change the case of the sentence")
        print('Enter 3 for Text Wrap ')
        print("Enter 0 for exit")
        option=int(input("\nEnter the option mention above-> "))
        if option==1:
           String_capatailze()
        elif option==2:
            swapcase()
        elif option==3:
            textWrap()       
        elif option==0:
           exit()
        else:
            print("Enter the valid option ..")        

    
 

 

