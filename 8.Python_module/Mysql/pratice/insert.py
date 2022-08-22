import mysql.connector 
  
  
mydb = mysql.connector.connect( 
  host = "localhost", 
  user = "root", 
  password = "", 
  database = "School"
)  
  
mycursor = mydb.cursor()
sql = "INSERT INTO Login (Username, Password) VALUES (%s, %s)"
val = ("4", "4") 
  
mycursor.execute(sql, val) 
mydb.commit() 
  
print(mycursor.rowcount, "details inserted") 
  
# disconnecting from server 
mydb.close() 

# sql = "INSERT INTO Student (Name, Roll_no) VALUES (%s, %s)"
# val = [("Akash", "98"), 
#        ("Neel", "23"), 
#        ("Rohan", "43"), 
#        ("Amit", "87"), 
#        ("Anil", "45"),  
#        ("Megha", "55"),  
#        ("Sita", "95")] 
  
# mycursor.executemany(sql, val) 
# mydb.commit() 
  
# print(mycursor.rowcount, "details inserted") 
  
# # disconnecting from server 
# mydb.close() 