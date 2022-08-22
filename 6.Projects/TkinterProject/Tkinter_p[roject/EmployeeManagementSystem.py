from tkinter import*
from tkinter import ttk
from tkinter import messagebox as mb
import pymysql

def update():
    print("update")
def delete():
    print("delete")
def show():
    pass
def showall():
    pass




def search():
    print("search")


class Employee:
    def __init__(self,root):
        self.root=root
        self.root.resizable(0,0)
        self.root.title("Employee Managemenyt System")
        self.root.geometry("1270x700+0+0")
        header=Label(self.root,text="Employee Management System",font="lucida 20 bold",fg="white",bg="black",bd=5)
        header.pack(side=TOP,fill=X)
        """
        all the required variable for the project
        """
        self.roll=StringVar()
        self.name=StringVar()
        self.email=StringVar()
        self.gender=StringVar()
        self.contact=StringVar()
        self.dob=StringVar()
        # self.address=StringVar()
        self.entry=StringVar()

        """
        all the efuunction defination
        """
        


        ff=Frame(self.root,bd=4,bg="crimson")
        ff.place(x=15,y=70,width=430,height=600)
        m_title=Label(ff,text="Manage Employee::",font="lucida 20 bold",fg="white",bg="crimson")
        m_title.grid(row=0,columnspan=2,pady=5)
        Roll=Label(ff,text="Roll",font="lucida 20 bold",fg="white",bg="crimson")
        Roll.grid(row=1,column=0,pady=5)
        entry_Roll=Entry(ff,font="lucida 20 bold",width=18,textvariable=self.roll)
        entry_Roll.grid(row=1,column=1,pady=5)
        Name=Label(ff,text="Name",font="lucida 20 bold",fg="white",bg="crimson")
        Name.grid(row=2,column=0,pady=5)
        entry_name=Entry(ff,font="lucida 20 bold",width=18,textvariable=self.name)
        entry_name.grid(row=2,column=1,pady=5)
        Email=Label(ff,text="Email",font="lucida 20 bold",fg="white",bg="crimson")
        Email.grid(row=3,column=0,pady=5)
        entry_email=Entry(ff,font="lucida 20 bold",width=18,textvariable=self.email)
        entry_email.grid(row=3,column=1,pady=5)
        Gender=Label(ff,text="Gender",font="lucida 20 bold",fg="white",bg="crimson")
        Gender.grid(row=4,column=0,pady=5)
        entry_gender=ttk.Combobox(ff,font="lucida 20 bold",width=17,state="readonly",textvariable=self.gender)
        entry_gender['values']=('Male',"Female","Other")
        entry_gender.grid(row=4,column=1)
        Contact=Label(ff,text="Contact",font="lucida 20 bold",fg="white",bg="crimson")
        Contact.grid(row=5,column=0,pady=5)
        entry_contact=Entry(ff,font="lucida 20 bold",width=18,textvariable=self.contact)
        entry_contact.grid(row=5,column=1,pady=5)
        DOB=Label(ff,text="DOB",font="lucida 20 bold",fg="white",bg="crimson")
        DOB.grid(row=6,column=0,pady=5)
        entry_dob=Entry(ff,font="lucida 20 bold",width=18,textvariable=self.dob)
        entry_dob.grid(row=6,column=1,pady=5)
        Address=Label(ff,text="Address",font="lucida 20 bold",fg="white",bg="crimson")
        Address.grid(row=7,column=0,pady=5)
        self.entry_address=Text(ff,width=18,height=3,font="lucida 20 bold")
        self.entry_address.grid(row=7,column=1,pady=5)
        btn_frame=Frame(ff,bd=2,bg="red")
        btn_frame.place(x=0,y=470,width=440,height=100)
        btn_insert=Button(btn_frame,text="Insert",font="lucida 20 bold",fg="white",bg="green",command=self.insert)
        btn_insert.grid(row=0,column=0,pady=20)
        btn_delete=Button(btn_frame,text="Delete",font="lucida 20 bold",fg="white",bg="green",command=self.delete)
        btn_delete.grid(row=0,column=1)
        btn_update=Button(btn_frame,text="update",font="lucida 20 bold",fg="white",bg="green",command=self.update)
        btn_update.grid(row=0,column=2)
        btn_clear=Button(btn_frame,text="Clear",font="lucida 20 bold",fg="white",bg="green",command=self.clear)
        btn_clear.grid(row=0,column=3)
        
      
        sf=Frame(self.root,bd=4,bg="crimson")
        sf.place(x=460,y=70,width=800,height=600)
        f_title=Label(sf,width=10,text="Search By",font="lucida 20 bold",fg="white",bg="crimson")
        f_title.grid(row=0,column=0,pady=10)
        entry_search=ttk.Combobox(sf,width=10,font="lucida 20 bold",state="readonly")
        entry_search['values']=('Roll',"Name","Contact")
        entry_search.grid(row=0,column=1,padx=20,pady=10)
        entry=Entry(sf,width=10,font="lucida 20 bold",textvariable=self.entry)
        entry.grid(row=0,column=2,pady=5)
        btn_show=Button(sf,text="Show",font="lucida 15 bold",fg="white",bg="green",command=show)
        btn_show.grid(row=0,column=3,padx=20)
        btn_showall=Button(sf,text="ShowAll",font="lucida 15 bold",fg="white",bg="green",command=showall)
        btn_showall.grid(row=0,column=4,padx=10)
        """
        table frame to show the table
        """
        table_frame=Frame(sf,bd=3,relief=RIDGE)
        table_frame.place(x=10,y=70,width=780,height=520)


        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("Roll","Name","Email","Gender","Contact",'DOB',"Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("Roll",text="Roll_No")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Contact",text="Contact")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Address",text="Address")
        #to remove the first space to the tree view
        self.student_table['show']='headings'
        
        self.student_table.column("Roll",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Contact",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        # self.clear()
    
    def insert(self):
        print("insert")
        conn=pymysql.connect(host="localhost",user="root",password='',database="Employee")
        cur=conn.cursor()
        cur.execute("insert into Report values(%s,%s,%s,%s,%s,%s,%s)",(self.roll.get(),
                                                                    self.name.get(),
                                                                    self.email.get(),
                                                                    self.gender.get(),
                                                                    self.contact.get(),
                                                                    self.dob.get(),
                                                                    self.address.get("1.0",END)
                                                                    ))
        conn.commit()
        self.fetch_data()
        conn.close()
        mb.showinfo("Message","Data Are Successfully Inserted")      

    def fetch_data(self):
        conn=pymysql.connect(host="localhost",user="root",password='',database="Employee")
        cur=conn.cursor()
        cur.execute("select * from Report")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
                conn.commit()
            
        conn.close()  
    def clear(self):
            print("clear")  
            self.roll.set("")  
            self.name.set("")
            self.email.set("")
            self.dob.set("")
            self.gender.set("")
            self.contact.set("")
            self.address.delete("1.0",END)


    def get_cursor(self,ev):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        row=content['values']
        # print(row)
        self.roll.set(row[0])
        self.name.set(row[1])
        self.email.set(row[2])
        self.gender.set(row[3])
        self.contact.set(row[4])
        self.dob.set(row[5])
        self.address.delete("1.0",END)
        self.address.set(END,row[6])


    def update(self):
        conn=pymysql.connect(host="localhost",user="root",password='',database="Employee")
        cur=conn.cursor()
        cur.execute("update Record set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll=%s",(self.name.get(),
                                                                                                                self.email.get(),
                                                                                                                self.gender.get(),
                                                                                                                self.contact.get(),
                                                                                                                self.dob.get(),
                                                                                                                self.address.get("1.0",END),
                                                                                                                self.roll.get()
                                                                                                                ))
        conn.commit()
        self.fetch_data()
        self.clear()
        conn.close()
        mb.showinfo("Message","Data Are Successfully Updated")

    # def delete(self):
    #     conn=pymysql.connect(host="localhost",user="root",password='',database="Employee")
    #     cur=conn.cursor()
    #     cur.execute("delete from Report where roll=%s"self.roll.get())
    #     conn.commit()
    #     conn.close()
    #     mb.showinfo("Message","Data Are Successfully Deleted")


    def delete(self):
        pass

    def update(self):
        pass                                                       










root=Tk()
obj=Employee(root)
root.mainloop()