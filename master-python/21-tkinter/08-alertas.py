from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.config(
    bd=70
)

def sacarAlerta():
    MessageBox.showinfo("Alerta", "Hola soy Victor Robles")
    #MessageBox.showwarning("Alerta", "Hola soy Victor Robles")
    #MessageBox.showerror("Alerta", "Hola soy Victor Robles")

Button(ventana, text="Mostrar Alerta!!!",command=sacarAlerta).pack()


def salir(nombre):
    resultado = MessageBox.askquestion("Salir", "¿Quieres continuar ejecutando la aplicación?")
    
    if resultado!= "yes":
        MessageBox.showinfo("Chao!!", f"Adios {nombre}")
        ventana.destroy()

Button(ventana, text="Salir",command=lambda: salir("Victor Robles")).pack() #lambda sirve para cuando quiero hacer click en el boton


ventana.mainloop()