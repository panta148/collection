    # def update(self):
    #     conn=pymysql.connect(host="localhost",user="root",password='',database="Employee")
    #     cur=conn.cursor()
    #     cur.execute("update Record set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll=%s",(self.roll.get(),
    #                                                                 self.name.get(),
    #                                                                 self.email.get(),
    #                                                                 self.gender.get(),
    #                                                                 self.contact.get(),
    #                                                                 self.dob.get(),
    #                                                                 self.address.get()
    #                                                                 ))
    #     conn.commit()
    #     conn.close()
    #     mb.showinfo("Message","Data Are Successfully Updated")

    # def delete(self):
    #     conn=pymysql.connect(host="localhost",user="root",password='',database="Employee")
    #     cur=conn.cursor()
    #     cur.execute("delete from Report where roll=%s"self.roll.get())
    #     conn.commit()
    #     conn.close()
    #     mb.showinfo("Message","Data Are Successfully Deleted")