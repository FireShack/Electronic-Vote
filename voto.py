import conexion
from conexion import cursor
from conexion import db


class voto:
    print('''
          Juntos por el cambio (indique jxc)
          Frente de Todos (indique ft)
          
          ''')
    N = input('Introduzca un partido:')
    
    if N == 'jxc':
        sql = ("INSERT INTO jxc (partido) VALUE ('{0}')").format(N)
        cursor.execute(sql)
        db.commit()
        print('Voto efectuado.')
        
    if N == 'ft':
        sql = ("INSERT INTO ft (partido) VALUE ('{0}')").format(N)
        cursor.execute(sql)
        db.commit()
        print('Voto efectuado.')
      
        

     
    
        
            
    
    
    
