# this is the tictactoe game develop in the python 
import tkinter as tk
player="x"
stopGame=False
bgcolor="yellow"
fgcolor="white"
wcolor="black"
def RunProgram():
    root=tk.Tk()
    root.title("Tic_Tac_Toe_Game")
    root.resizable(0,0)
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
                box[1][1].config(bg=wcolor)
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
    

    def restart():
        '''
        this method will destroy the all the frame that 
        you have seen in the window and start the new window as rhe function call again
        '''
        root.destroy()
        RunProgram()

    
    '''
    initialization for the box,frames,states
    '''
    box=[[0,0,0],[0,0,0],[0,0,0]]
    frames=[[0,0,0],[0,0,0],[0,0,0]]
    states=[[0,0,0],[0,0,0],[0,0,0]]
    '''
    making the 6 button using the for loop
    '''
    for i in range(3):
        for j in range(3):
            frames[i][j]=tk.Label(root,bg="gray",bd=3)
            frames[i][j].grid(row=i,column=j)
            box[i][j]=tk.Button(frames[i][j],font=('Arial',65),width=3,bg=fgcolor,border=0,command=lambda x=i,y=j:activate(x,y))
            box[i][j].pack()
    '''
    for making the restart button
    '''        
    button_reset=tk.Button(root,text="Restart",font=('Arial',15,"bold"),border=0,fg="black",command=restart,activebackground='yellow',activeforeground="red")
    button_reset.grid(row=5,column=1,ipady=2)
    '''
    for making the label for showing the "x" and the "o"
    '''
    label1=tk.Label(root,text="0",fg="#0a44a1",border=3,font=('arial',23,"bold"))
    label1.grid(row=5,column=0)
    label2=tk.Label(root,text="X",fg="#B80028",border=3,font=('arial',23,"bold"))
    label2.grid(row=5,column=2)




    root.mainloop()

RunProgram()