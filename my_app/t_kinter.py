from tkinter import *
from ver import resultado
from votar_jxc import voto_jxc
from votar_ft import voto_ft

pantalla = Tk()
pantalla.geometry('350x300+500+120')
pantalla.title('Voto electronico')
pantalla.resizable(width= False, height= False)


Label(pantalla, text='Bienvenido al sistema de voto electronico', font= ('calibri', 12)).place(x='40', y='20')
boton_jxc = Button(pantalla, text= 'Juntos x el cambio', bg= 'gold', command= voto_jxc, state= NORMAL).place(x='40', y='80')
boton_ft =Button(pantalla, text= 'Frente de Todos', bg='light blue', command= voto_ft, state=NORMAL).place(x='210', y='80')
Button(pantalla, text= 'Resultados', bg= 'grey', command= resultado).place(x='145', y='120')



pantalla.mainloop()