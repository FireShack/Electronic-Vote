import conection
from conection import cursor
from conection import db
from tkinter import *



def voto_ft():
    N = 'ft'
    pantalla3 = Tk()
    pantalla3.geometry('160x150+500+140')
    pantalla3.title('Resultados')
    pantalla3.resizable(width= False, height= False)
    
    sql = ("INSERT INTO ft (partido) VALUE ('{0}')").format(N)
    cursor.execute(sql)
    db.commit()
    Label(pantalla3, text= 'Voto efectuado.', font=('calibri', 12)).place(x=30, y=40)
    
