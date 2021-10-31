#Conexion a la base de datos 

import mysql.connector

db = mysql.connector.connect(
    
    host = 'localhost',
    user = 'root',
    passwd = '', 
    database = 'voto_electronico',
    port = 3306    
)

cursor = db.cursor(buffered= True)