
import mysql.connector  
print("This is the new connection of the mysql data type")   
# connecting to the database  
dataBase = mysql.connector.connect( 
                     host = "localhost", 
                     user = "root", 
                     passwd = "", 
                     database = "School" )   
    
# preparing a cursor object  
cursorObject = dataBase.cursor() 
    
print("Displaying NAME and ROLL columns from the STUDENT table:") 
  
# selecting query 
query = "SELECT * FROM Login"
cursorObject.execute(query) 
  
myresult = cursorObject.fetchall() 
  
for x in myresult: 
    print(x) 
  
# disconnecting from server 
dataBase.close() 