from tkinter import *

def guardar():
    promedio = (num1.get() + num2.get())/2
    resultado.set("El Promedio es: " + str(promedio))

def borrar():
    num1.set("")
    num2.set("")
    resultado.set("")




ventana=Tk()
ventana.geometry("400x300")
ventana.iconbitmap(r"D:\python\practicas\RegistrodeAlumnosGráfico\user-group.ico")
ventana.title("Promedio")
#Declaramos variable IntVar, DoubleVar, StringVar******
num1 = IntVar()
num2 = IntVar()
resultado = StringVar()

num1.set("")
num2.set("")

#Etiquetas************************
textoEtiqueta1 = Label(ventana, text="Escribe la nota 1: ")
textoEtiqueta1.place(x=170, y=10)

textoEtiqueta2 = Label(ventana, text="Escribe la nota 2: ")
textoEtiqueta2.place(x=170, y=70)

#Caja de texto********************
caja1 = Entry(ventana, textvariable=num1)
caja1.place(x=150, y=30)
caja2 = Entry(ventana, textvariable=num2)
caja2.place(x=150, y=90)

#Etiqueta resultado****************
textoR = Label(ventana, textvariable=resultado)
textoR.place(x=160, y=200)

#Botones***************************
boton1= Button(ventana, text="Guardar", command=guardar, bg="#006", fg="white")
boton1.place(x=210, y=140)

boton2= Button(ventana, text="Borrar", command=borrar, bg="#006", fg="white")
boton2.place(x=155, y=140)









ventana.mainloop()