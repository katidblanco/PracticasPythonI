from tkinter import *
raiz=Tk()
raiz.title("Registro de alumnos")
raiz.resizable(1,1)
raiz.iconbitmap(r"D:\python\practicas\RegistrodeAlumnos\user-group.ico")
#raiz.geometry("350x350")
#raiz.config(bg="#f4f0e5")

miFrame = Frame(raiz, width="1200",height="1200" )
miFrame.config(bg="#c3e6d4")
miFrame.config(cursor="hand2")
miFrame.pack()

cuadroNombre = Entry(miFrame)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=1, column=1, padx=10, pady=10)

nombreLabel=Label(miFrame, text="Nombre")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)
nombreLabel.config(bg="#c3e6d4")

apellidoLabel=Label(miFrame, text="Apellido")
apellidoLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)
apellidoLabel.config(bg="#c3e6d4")








raiz.mainloop()



