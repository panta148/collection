from tkinter import*
import tkinter
import sys
import tkinter.messagebox as mb
from PIL import Image,ImageTk
def insert():
    root.destroy()
    import Insert


def delete():
    root.destroy()
    import Delete


def update(): 
    root.destroy()
    import Update

def search():
    root.destroy()
    import Search





root=Tk()
root.title("Home")
root.resizable(0,0)
root.geometry('1000x600+100+10')
root.config(bg="#808080")
image=Image.open("photo/SCHOOL.jpg")
photo=ImageTk.PhotoImage(image)
f1=Frame(root,bg="red").place(x=0,y=0,height=550,width=950)
l=Label(f1,image=photo).pack()
l1=Label(f1,text="SCHOOL MANAGEMENT SYSTEM",bg="skyblue",fg="black",font="lucida 20 bold",width=60).place(x=0,y=0)
b1=Button(f1,text="Insert",bg="green",font="lucida 15 bold",fg="white",padx=10,pady=10,command=insert).place(x=200,y=500)
b2=Button(f1,text="Delete",bg="green",font="lucida 15 bold",fg="white",padx=10,pady=10,command=delete).place(x=400,y=500)
b3=Button(f1,text="Update",bg="green",font="lucida 15 bold",fg="white",padx=10,pady=10,command=update).place(x=600,y=500)
b4=Button(f1,text="Search",bg="green",font="lucida 15 bold",fg="white",padx=10,pady=10,command=search).place(x=800,y=500)

root.mainloop()