"""
this is a simple calculator which is made my me sololely:::)))))

"""
from tkinter import *
root=Tk()
root.title("Simple Claculator")
root.resizable(0,0)
root.geometry("400x400+0+0")
l=Label(root,text="Calculator",fg="white",bg="black",font="arial 20 bold").grid()
l2=Label(root,text="First Number ").grid(row=1,column=1)
l3=Label(root,text="Second Number ").grid(row=2,column=1)



root.mainloop()
