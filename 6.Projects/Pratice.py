import tkinter as tk 
player="x"
stopGame=False
wcolor="black"
def Rungame():
    root=tk.Tk()
    root.title("TicTacToe")
    root.resizable(0,0)
    def restart():
        root.destroy()
        Rungame()
    def activate(x,y):
        global player
        if player=="x" and states[x][y]==0 and stopGame is False:
            box[x][y].config(text="x",fg="white",bg="#B80028")
            states[x][y]="x"
            player="0"
        elif player=="0" and states[x][y]==0 and stopGame is False:
            box[x][y].config(text="0",fg="white",bg="#0a44a1")
            states[x][y]="0"
            player="x"
        checkForWinner()    

    def checkForWinner():
        global stopGame
        stopGame=False
        for i in range(3):
            if states[i][0]==states[i][1]==states[i][2]!=0:
                box[i][0].config(bg=wcolor)
                box[i][1].config(bg=wcolor)
                box[i][2].config(bg=wcolor)
                stopGame=True
            elif states[0][i]==states[1][i]==states[2][i]!=0:
                box[0][i].config(bg=wcolor)
                box[1][i].config(bg=wcolor)
                box[2][i].config(bg=wcolor)
                stopGame=True
            elif states[0][0]==states[1][1]==states[2][2]!=0:
                box[0][0].config(bg=wcolor)
                box[1][1].config(bg=wcolor)
                box[2][2].config(bg=wcolor)
                stopGame=True
            elif states[2][0]==states[1][1]==states[0][2]!=0:
                box[2][0].config(bg=wcolor)
                box[1][1].config(bg=wcolor)
                box[0][2].config(bg=wcolor)
                stopGame=True  
    states=[[0,0,0],[0,0,0],[0,0,0]]
    box=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):   
        for j in range(3):
            box[i][j]=tk.Button(root,bg="gray",fg="black",width=3,border=5,font="lucida 65 bold",command=lambda x=i,y=j:activate(x,y))
            box[i][j].grid(row=i,column=j)
    reset_btn=tk.Button(root,bg="gray",text="Reset",fg="black",width=5,border=3,font="lucida 20 bold",command=restart)
    reset_btn.grid(row=3,column=1)     
    l1=tk.Label(root,bg="white",text="0",fg="red",width=3,border=3,font="lucida 30 bold") 
    l1.grid(row=3,column=0)
    l2=tk.Label(root,bg="white",text="X",fg="red",width=3,border=3,font="lucida 30 bold")
    l2.grid(row=3,column=2)
    root.mainloop()

Rungame()    