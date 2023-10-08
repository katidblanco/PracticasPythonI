from tkinter import *

def guardar():
    nombresLista.append(nombre.get)
    print(str(nombre))
    # promedio = (num1.get() + num2.get())/2
    # resultado.set("El Promedio es: " + str(promedio))

def borrar():
    nombre.set("")
    apellido.set("")
    resultado.set("")




ventana=Tk()
ventana.geometry("400x300")
ventana.iconbitmap(r"D:\python\practicas\RegistrodeAlumnosGráfico\user-group.ico")
ventana.title("Registro de alumnos")

#Declaramos variable IntVar, DoubleVar, StringVar******
nombre = StringVar()
apellido = StringVar()
resultado = StringVar()

nombre.set("")
apellido.set("")

nombresLista = []  #Creamos Lista Nombres****************

#Etiquetas************************
nombretiqueta1 = Label(ventana, text="Nombre: ")
nombretiqueta1.place(x=170, y=10)

ApellidoEtiqueta2 = Label(ventana, text="Apellido: ")
ApellidoEtiqueta2.place(x=170, y=70)

#Caja de texto********************
cajaNombre = Entry(ventana, textvariable=nombre)
cajaNombre.place(x=150, y=30)
cajaApellido = Entry(ventana, textvariable=apellido)
cajaApellido.place(x=150, y=90)

#Etiqueta resultado****************
textoR = Label(ventana, textvariable=resultado)
textoR.place(x=160, y=200)

#Botones***************************
botonGuardar= Button(ventana, text="Guardar", command=guardar, bg="#006", fg="white")
botonGuardar.place(x=210, y=140)

botonBorrar= Button(ventana, text="Borrar", command=borrar, bg="#006", fg="white")
botonBorrar.place(x=155, y=140)









ventana.mainloop()



