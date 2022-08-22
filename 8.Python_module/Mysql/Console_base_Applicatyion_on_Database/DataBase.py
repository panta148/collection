import mysql.connector as mc
class MyConnection:
    def __init__(self):
        self.conn = mc.connect(host="localhost",
                     user="root",
                     passwd="",
                     database="school")
        try:
            mycursor=self.conn.cursor()
            query="Create table if not exists Student(userid int primary key,uusername varchar(100),roll int,Address varchar(100))"
            mycursor.execute(query)
            print("Table is created successfully")
        except Exception as a:
            print(a)

    def insert(self,userid,username,roll,address):
        try:
            query="insert into Student(userid,uusername,roll,Address)values({},'{}',{},'{}')".format(userid,username,roll,address)
            mycur=self.conn.cursor()
            mycur.execute(query)
            self.conn.commit()
            print("Data are successfully inserted")
        except Exception as e:
            print(e)    

    def fetch_all(self):
        try:
            query="select * from Student"
            mycur=self.conn.cursor()
            mycur.execute(query)
            for row in mycur:
                print(f'UserId={row[0]}')   
                print(f'UserName={row[1]}') 
                print(f'Roll={row[2]}') 
                print(f'Address={row[3]}')
                print()
                print()  
                
        except Exception as e:
            print(e)        

    def delete(self,id):
        try:
            print(id)
            query=f"delete from Student where userid={id}"
            mycur=self.conn.cursor()
            mycur.execute(query)
            self.conn.commit()
            print(f"userid={id} data have been successfully deleted")   
        except Exception as e:
            print(e)         




    def update(self,id,newname,newroll,newaddress):
        try:
            query=f"update Student set uusername='{newname}',roll={newroll},Address='{newaddress}' where userid={id}"
            mycur=self.conn.cursor()
            mycur.execute(query)
            self.conn.commit()
            print(f'userid of {id} data have been updated')
        except Exception as e:
            print(e)   


    def search(self,id):
        try:
            count=0
            query="select * from Student"
            mycur=self.conn.cursor()
            mycur.execute(query)
            for row in mycur:
                if row[0]==id:
                    count=1
                    print(f'UserId={row[0]}')   
                    print(f'UserName={row[1]}') 
                    print(f'Roll={row[2]}') 
                    print(f'Address={row[3]}')
                    print()
            if count==0:
                print("ID you have enter is not correct ..Enter the correct one to search")        
                     
        except Exception as e:
            print(e)








# obj=MyConnection()
# obj.insert(1,"Amrit",1,'Banepa')
# obj.insert(2,"amrit",2,'Banepa')
# obj.insert(3,"anupa",3,'Banepa')
# obj.insert(4,"manita",4,'Banepa')
# obj.insert(5,"pragya",5,'Banepa')
# obj.insert(6,"aarogya",6,'Banepa')

# obj.fetch_all()
# obj.delete(6)
# obj.update(1,"Dhoni",11,"Kathmandu")
# obj.search(100)
