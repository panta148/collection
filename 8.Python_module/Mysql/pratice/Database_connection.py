# method1
import mysql.connector 
# we use  connect() function
  
# Connecting from the server 
conn = mysql.connector.connect(user = 'root', 
                               host = 'localhost', 
                              database = 'Amrit') 
  
print(conn) 
print("Thois is the connection of the data base ")
  
# Disconnecting from the server 
conn.close() 


##################################################################################################
# method-2
# Also for the same, we can use connection.MySQLConnection() class instead of connect():
# from mysql.connector import connection 
  
# # Connecting to the server 
# conn = connection.MySQLConnection(user = 'root',  
#                               host = 'localhost', 
#                               database = 'Amrit') 
  
# print(conn) 
  
# # Disconnecting from the server 
# conn.close() 







#####################################################################################################
#method 3
# from mysql.connector import connection 
# Another way is to pass the dictionary in the connect() function using ‘**’ operator:
  
  
# dict = { 
#   'user': 'root', 
#   'host': 'localhost', 
#   'database': 'Amrit'
# } 
  
# # Connecting to the server 
# conn = connection.MySQLConnection(**dict) 
  
# print(conn) 
  
# # Disconnecting from the server 
# conn.close() 