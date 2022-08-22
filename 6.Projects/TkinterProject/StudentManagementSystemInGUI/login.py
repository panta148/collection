from tkinter import*
from DataBaseConnection import connect
import sys
import tkinter.messagebox as mb
from PIL import Image,ImageTk
import mysql.connector
from mysql.connector import Error
def stop():
    sys.exit()

def login():
    conn=mysql.connector.connect(host="localhost",user="root",database="School")
    try:
        print("Successfully connect to the database")
        mc=conn.cursor()
        query="select * from Login"
        mc.execute(query)
        result=mc.fetchall()
        for row in result:
            Username=row[0]
            Password=row[1]
        if username.get()==Username and password.get()==Password:
            root.destroy()
            import Home
        else:
            mb.showerror("ERROR","Insert correct username and password")    
    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if (conn.is_connected()):
            conn.close()
            mc.close()
            print("MySQL connection is closed")        
    

    


  
    

if __name__ == '__main__':
    root=Tk()
    root.title("Login")
    root.resizable(0,0)
    root.geometry('600x400+300+100')
    root.config(bg="#808080")
    username=StringVar()
    password=StringVar()
    image=Image.open("photo/key.jpg")
    photo=ImageTk.PhotoImage(image)
    l1=Label(root,text="LOGIN",font="lucida 15 bold",fg="white",bg="black").pack(fill=X)
    f=Frame(root,bg="white").place(x=10,y=50,width=580,height=340)
    l1=Label(f,image=photo).pack()
    l2=Label(f,text="User_Name:",font="lucida 15 bold",fg="black").place(x=90,y=150)
    l3=Label(f,text="PassWord:",font="lucida 15 bold",fg="black").place(x=90,y=200)
    userentry=Entry(f,font="lucida 15 bold",textvariable=username).place(x=250,y=150)
    passentry=Entry(f,font='lucida 15 bold',textvariable=password).place(x=250,y=200)
    b1=Button(f,text="Login",font="lucida 15 bold",bg="red",fg="white",command=login).place(x=200,y=300)
    b2=Button(f,text="Cancel",font="lucida 15 bold",bg="red",fg="white",command=stop).place(x=350,y=300)
    root.mainloop()
        