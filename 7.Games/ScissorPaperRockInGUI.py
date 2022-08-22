from tkinter import *
import random
import time
def ask(event):
    btn_text=event.widget.cget("text")
    computer=Computer()
    global cpoint
    global ppoint
    if btn_text=="Scissor":
        b1['bg']='Yellow'
        b1['fg']="Black"
        if computer=="Scissor":
            result['text']="Game Draw"
            b4['bg']='Yellow'
            b4['fg']="Black"

        elif computer=="Paper":
            result['text']="You won "
            b5['bg']='Yellow'
            b5['fg']="Black"
            ppoint=ppoint+1
            result11['text']=ppoint

        elif computer=="Rock":
            result['text']="Computer Won"
            b6['bg']='Yellow'
            b6['fg']="Black"
            cpoint=cpoint+1
            result22['text']=cpoint  
        
              


    elif btn_text=="Paper":
        b2['bg']='Yellow'
        b2['fg']="Black"
        if computer=="Scissor":
            result['text']="Computer won"
            b4['bg']='Yellow'
            b4['fg']="Black"
            cpoint=cpoint+1
            result22['text']=cpoint

        elif computer=="Paper":
            result['text']="Game Draw "
            b5['bg']='Yellow'
            b5['fg']="Black"
        elif computer=="Rock":
            result['text']="You Won"
            b6['bg']='Yellow'
            b6['fg']="Black"  
            ppoint=ppoint+1
            result11['text']=ppoint 
    elif btn_text=="Rock":
        b3['bg']='Yellow'
        b3['fg']="Black"
        if computer=="Scissor":
            result['text']="You won"
            b4['bg']='Yellow'
            b4['fg']="Black"
            ppoint=ppoint+1
            result11['text']=ppoint

        elif computer=="Paper":
            result['text']="Computer Won "
            b5['bg']='Yellow'
            b5['fg']="Black"
            cpoint=cpoint+1
            result22['text']=cpoint
        elif computer=="Rock":
            result['text']=" Game Draw "
            b6['bg']='Yellow'
            b6['fg']="Black"   





 
def again(event):
    result['text']=" "
    b1['bg']='black'
    b1['fg']="white"
    b2['bg']='black'
    b2['fg']="white"
    b3['bg']='black'
    b3['fg']="white"
    b4['bg']='black'
    b4['fg']="white"
    b5['bg']='black'
    b5['fg']="white"
    b6['bg']='black'
    b6['fg']="white"

def disable(event):
    pass

def Computer():
    computer_list=["Scissor","Paper","Rock"]
    computer=random.choice(computer_list)
    return computer

def new(event):
    result['text']=" New Game "
    global cpoint
    global ppoint
    cpoint=0
    ppoint=0 
    result22['text']=cpoint
    result11['text']=ppoint
    b1['bg']='black'
    b1['fg']="white"
    b2['bg']='black'
    b2['fg']="white"
    b3['bg']='black'
    b3['fg']="white"
    b4['bg']='black'
    b4['fg']="white"
    b5['bg']='black'
    b5['fg']="white"
    b6['bg']='black'
    b6['fg']="white"  
 
    

root=Tk()
root.title("ScissorPaperRock")
root.resizable(0,0)
root.configure(bg="White")
root.geometry('500x550+100+10')
value=StringVar()
cpoint=IntVar()
ppoint=IntVar()
cpoint=0
ppoint=0
l1=Label(root,text="ScissorPaperRock",font="lucida 15 bold",bg="black",fg="white")
l1.pack(fill=X)
l2=Label(root,text="Your Choice",font="lucida 20 bold",bg="white",fg="black")
l2.pack(fill=X,pady=10)
f1=Frame(root,bg="gray")
f1.place(x=20,y=90,width=460,height=140)
b1=Button(f1,text="Scissor",font="lucida 20 bold",bg="black",fg="white",activebackground="yellow")
b1.place(x=30,y=10,width=120,height=120)
b1.bind("<Button-1>",ask)
b2=Button(f1,text="Paper",font="lucida 20 bold",bg="black",fg="white",activebackground="yellow")
b2.place(x=190,y=10,width=120,height=120)
b2.bind("<Button-1>",ask)
b3=Button(f1,text="Rock",font="lucida 20 bold",bg="black",fg="white",activebackground="yellow")
b3.place(x=350,y=10,width=120,height=120)
b3.bind("<Button-1>",ask)
l3=Label(root,text="Computer Choice",font="lucida 20 bold",bg="white",fg="black")
l3.place(x=0,y=240,width=500)
f2=Frame(root,bg="gray")
f2.place(x=20,y=290,width=460,height=140)
b4=Button(f2,text="Scissor",font="lucida 20 bold",bg="black",fg="white",state="disable")
b4.place(x=30,y=10,width=120,height=120)
b4.bind("<Button-1>",disable)
b5=Button(f2,text="Paper",font="lucida 20 bold",bg="black",fg="white",state="disable")
b5.place(x=190,y=10,width=120,height=120)
b5.bind("<Button-1>",disable)
b6=Button(f2,text="Rock",font="lucida 20 bold",bg="black",fg="white",state="disable")
b6.place(x=350,y=10,width=120,height=120)
b6.bind("<Button-1>",disable)
result=Label(root,text="  ",font="lucida 20 bold",bg="white",fg="red")
result.place(x=0,y=450,width=500)
b7=Button(root,text="OK",font="lucida 20 bold",bg="gray",fg="black")
b7.place(x=430,y=440,width=50,height=50)
b7.bind("<Button-1>",again)
b8=Button(root,text="New",font="lucida 20 bold",bg="gray",fg="black")
b8.place(x=20,y=440,width=60,height=50)
b8.bind("<Button-1>",new)
result1=Label(root,text="Your-point::",font="lucida 15 bold",bg="white",fg="black")
result1.place(x=20,y=510)
result11=Label(root,text="0",font="lucida 20 bold",bg="white",fg="black")
result11.place(x=140,y=508)
result2=Label(root,text="Computer-point::",font="lucida 15 bold",bg="white",fg="black")
result2.place(x=300,y=510)
result22=Label(root,text="0",font="lucida 20 bold",bg="white",fg="black")
result22.place(x=470,y=508)

root.mainloop()