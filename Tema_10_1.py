from tkinter import *

root = Tk()
root.geometry('400x400')
root.title('El Calificador')

valor = StringVar(value=' ')
pizarra = Label(text=' ')
calificacion = ['Pesimo', 'Malo', 'Regular', 'Bueno', 'Excelente']

def mostrarValor(event):
    pizarra['text'] = event.widget.cget('value')

def resetear(event):
    valor.set(' ')
    pizarra['text'] = ' '

Label(text = 'Selecciona tu calificación:').pack(
    anchor = NW, padx = 15, pady = 15
    )

opciones = Frame(root)
opciones.pack(side=LEFT, fill=Y, pady=15, padx=25)
radios = []
for n in range(5):
    radios.append(
        Radiobutton(
            opciones,
            text = f'{n * 5} puntos', 
            value = f'{calificacion[n]}', 
            variable = valor
            )
    )
    radios[n].bind('<Button-1>', mostrarValor)
    radios[n].pack(anchor=NW)

pizarra.pack(fill=BOTH, expand=YES)

reset = Button(text='Resetear')
reset.bind('<Button-1>', resetear)
reset.pack(pady=25)

root.mainloop()