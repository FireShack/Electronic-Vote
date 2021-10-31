import conexion
from conexion import cursor
from conexion import db

class resultado:
    
    sql = ('SELECT voto FROM jxc ORDER BY voto DESC')
    cursor.execute(sql)
    A = cursor.fetchone()
    
    for x in A:
        print('Votos de Juntos por el Cambio: ', x)
        
    sql = ('SELECT id FROM ft ORDER BY id DESC')
    cursor.execute(sql)
    A = cursor.fetchone()
    
    for x in A:
        print('Votos de Frente de Todos: ', x)