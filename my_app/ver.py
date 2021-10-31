import conection
from conection import cursor
from conection import db
from tkinter import *

def resultado():
    pantalla2 = Tk()
    pantalla2.geometry('160x150+500+140')
    pantalla2.title('Resultados')
    pantalla2.resizable(width= False, height= False)
    
    sql = ('SELECT voto FROM jxc ORDER BY voto DESC')
    cursor.execute(sql)
    A = cursor.fetchone()
    
    for x in A:
        Label(pantalla2, text='Votos de Juntos x el cambio:', bg= 'gold').pack()
        Label(pantalla2, text= x ).pack()
        
    sql = ('SELECT id FROM ft ORDER BY id DESC')
    cursor.execute(sql)
    A = cursor.fetchone()
    
    for x in A:
        Label(pantalla2, text='Votos de Frente de Todos:', bg= 'light blue').pack()
        Label(pantalla2, text= x ).pack()

