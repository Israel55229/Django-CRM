import mysql.connector


dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Kobby#55229'
)

# prepare a cursor object
CursorObject = dataBase.cursor()

CursorObject.execute("CREATE DATABASE elderco")

print('All Done!')

