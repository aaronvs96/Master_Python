"""
Crear un programa que tenga:
(hecho) - ventana
(hecho) - tamaño fijo
(hecho) - no redimensiable
(hecho) - un menu (Inicio, añadir, informacion, salir)
(hecho) - opcion de salir
(hecho) - diferentes pantallas
(hecho) formulario de añadir productos
(hecho) guardar datos temporalmente
(hecho) mostrar datos listados en la pantalla home
"""

from cgitb import text
from tkinter import *
from tkinter import ttk

# Definir ventana
ventana=Tk()
# ventana.geometry("500x500")
ventana.minsize(500,500)
ventana. title("Proyecto Tkinter - Master en Python")
ventana.resizable(0,0)

#Pantallas
def home():
    #Montar pantalla    
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial",30),
        padx=190,
        pady=20
    )
    home_label.grid(row=0, column=0)

    products_box.grid(row=2)

    #Listar productos
    """
    for product in products:
        if len(product)==3:
            product.append("added")
            Label(products_box, text=product[0]).grid()
            Label(products_box, text=product[1]).grid()
            Label(products_box, text=product[2]).grid()
            Label(products_box, text="----------------").grid()
    """
    for product in products:
        if len(product)==3:
            product.append("added")
            products_box.insert('',0, text=product[0], values=(product[1]))           

    #Ocultar otras pantallas
    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    add_frame.grid_remove()

def add():
    #Encabezado
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial",30),
        padx=100,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=10)

    #Campos del formulario
    add_frame.grid(row=1)
    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    add_description_label.grid(row=3, column=0, padx=5, pady=5, sticky=NW)
    add_description_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    add_description_entry.config(
        width=30,
        height=5,
        font=("Consolas",12),
        padx=15,
        pady=15
    )

    add_separator.grid(row=4, column=1)

    boton.grid(row=5, column=1, sticky=E)
    boton.config(
        padx=15,
        pady=5,
        bg="green",
        fg="white"
    )

    #Ocultar otras pantallas
    home_label.grid_remove()
    products_box.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    

def info():
    #Montar pantalla  
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial",30),
        padx=140,
        pady=20
    )
    info_label.grid(row=0,column=0)
    data_label.grid(row=1, column=0)

    #Ocultar otras pantallas
    home_label.grid_remove()
    products_box.grid_remove()
    add_label.grid_remove()
    add_frame.grid_remove()

def add_product():
    products.append([
        name_data.get(),
        price_data.get(),
        add_description_entry.get("1.0","end-1c")
    ])
    name_data.set("")
    price_data.set("")
    add_description_entry.delete("1.0", END)

    home()


# Variables importantes
products = []
name_data = StringVar()
price_data=StringVar()


#Definir campos de pantallas (INICIO)
home_label = Label(ventana, text="Inicio")
# products_box = Frame(ventana, width=250)

Label(ventana).grid(row=1)
products_box = ttk.Treeview(height=12, columns=2)
products_box.grid(row=1, column=0, columnspan=2)
products_box.heading("#0",text="Producto", anchor=W)
products_box.heading("#1",text="Precio", anchor=W)

#Definir campos de pantallas (ADD)
add_label = Label(ventana, text="Añadir producto")

# Campos del formulario
add_frame = Frame(ventana)
add_name_label = Label(add_frame,text="Nombre:")
add_name_entry = Entry(add_frame, textvariable=name_data)

add_price_label = Label(add_frame,text="Precio:")
add_price_entry = Entry(add_frame, textvariable=price_data)

add_description_label = Label(add_frame,text="Descripcion:")
add_description_entry = Text(add_frame)

add_separator = Label(add_frame)

boton = Button(add_frame, text="Guardar", command=add_product)


#Definir campos de pantallas (INFO)
data_label = Label(ventana,text="Creado con Victor Robles - 2022")
info_label = Label(ventana, text="Informacion")

#Cargar la pantlla de inicio
home()

# Menu superior
menuSuperior = Menu(ventana)
menuSuperior.add_command(label="Inicio",command=home)
menuSuperior.add_command(label="Añadir",comman=add)
menuSuperior.add_command(label="Información",command=info)
menuSuperior.add_command(label="Salir", command=ventana.quit)

#Cargar menu
ventana.config(menu=menuSuperior)





#Cargar ventana
ventana.mainloop()