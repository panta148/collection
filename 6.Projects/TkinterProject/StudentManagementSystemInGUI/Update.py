from tkinter import *
def go():
    root.destroy()
    import Home

    
root=Tk()
root.title("Update")
root.resizable(0,0)
root.geometry('1000x600+100+10')
root.config(bg="#808080")
b=Button(root,text="<-",bg="red",fg="black",command=go).place(x=960,y=0,width=40,height=40)
root.mainloop()