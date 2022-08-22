# create the main sections of the layout, 
# and lay them out
def click(event):
    print("hello man")
from tkinter import *
root=Tk()
root.geometry('100x100+100+100')
b=Button(text="click")
b.pack()
b.bind("<Button-1>",click)


root.mainloop()