import mysql.connector
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="amritdon")

# preparing a cursor object
cursorObject = dataBase.cursor()

# creating table
login = """CREATE TABLE LOGIN (  
                   USERNAME  VARCHAR(20) NOT NULL,  
                   PASSWORD VARCHAR(20),  
                   )"""

# table created
cursorObject.execute(login)
print("create the table successfully")
# disconnecting from server
dataBase.close()
