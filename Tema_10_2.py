from tkinter import *
root = Tk()
root.geometry('250x300')
root.title('El Comprador')

Label(text='Lista de compras:').pack(pady = 15)

lista = ['Harina', 'Arroz', 'Frijoles', 'Café', 'Azúcar', 'Sal']
miLista = Listbox()
miLista.pack(pady = 15)
miLista.insert(END, *lista)

root.mainloop()