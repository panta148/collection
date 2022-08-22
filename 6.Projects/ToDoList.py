import tkinter as tk 
from datetime import datetime
from tkinter import ttk
def getdate():
    now= datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string

def add():
    text=my_list.get()
    print(text)


root=tk.Tk()
root.title('ToDo List')
root.resizable(0,0)
root.geometry('600x600+0+0')
l1=tk.Label(root,text="My ToDo LIst",bg="black",fg="white",font='lucida 20 bold')
l1.pack(fill="x")
my_list=tk.StringVar()
entry=tk.Entry(root,font="lucida 15 bold",bg="white",fg="black",textvar=my_list)
entry.place(x=40,y=60,width=500,height=40)
bt=tk.Button(root,text="ADD",bg="black",fg="white",font='lucida 20 bold',command=add)
bt.place(x=250,y=110,width=80,height=50)
f1=tk.Frame(root,bg="gray",bd=3,)
f1.place(x=10,y=170,width=570,height=420)
tree=ttk.Treeview(f1)
#defining the column of the treeview
tree["columns"]=("one","two","three")
tree.column("#0", width=70, minwidth=70, stretch=tk.NO)
tree.column("one", width=180, minwidth=180, stretch=tk.NO)
tree.column("two", width=300, minwidth=200)
#defining the heading 
tree.heading("#0",text="SN",anchor=tk.W)
tree.heading("one", text="Date modified",anchor=tk.W)
tree.heading("two", text="ToDo List",anchor=tk.W)

#inserting the element to the treeview
# folder1=tree.insert("", 1, "", text="Folder 1", values=("23-Jun-17 11:05","File folder",""))
# tree.insert("", 2, "", text="text_file.txt", values=("23-Jun-17 11:25","TXT file","1 KB"))
# tree.insert(folder1, "end", "", text="photo1.png", values=("23-Jun-17 11:28","PNG file","2.6 KB"))
# tree.insert(folder1, "end", "", text="photo2.png", values=("23-Jun-17 11:29","PNG file","3.2 KB"))
# tree.insert(folder1, "end", "", text="photo3.png", values=("23-Jun-17 11:30","PNG file","3.1 KB"))
tree.insert(text="1",values=("","","2/2","reading"))


tree.pack()
# tree.pack(side=tk.TOP,fill=tk.X)




    

        

root.mainloop()