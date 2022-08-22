# import mysql.connector
# dataBase = mysql.connector.connect(
#   host ="localhost",
#   user ="root",
#   passwd =""
# )

# # preparing a cursor object
# cursorObject = dataBase.cursor()

# # creating database
# cursorObject.execute("CREATE DATABASE School")
import mysql.connector

# connecting to the database
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

# studentRecord = """CREATE TABLE STUDENT (
#                    NAME  VARCHAR(20) NOT NULL,
#                    BRANCH VARCHAR(50),
#                    ROLL INT NOT NULL,
#                    SECTION VARCHAR(5),
#                    AGE INT,
#                    )"""
