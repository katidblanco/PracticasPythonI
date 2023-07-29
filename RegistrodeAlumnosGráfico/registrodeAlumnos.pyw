from tkinter import *

raiz=Tk()
raiz.title("Registro de alumnos")
raiz.resizable(1,1)
raiz.iconbitmap(r"D:\python\practicas\RegistrodeAlumnosGráfico\user-group.ico")
#raiz.geometry("350x350")
#raiz.config(bg="#f4f0e5")

miFrame = Frame(raiz, width="1200",height="1200" )
miFrame.config(bg="#c3e6d4")
miFrame.config(cursor="hand2")
miFrame.pack()

#Cuadros ENTRY***************************************
nombre = StringVar()
cuadroNombre = Entry(miFrame, textvariable=nombre)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)

cuadroNota = Entry(miFrame)
cuadroNota.grid(row=1, column=1, padx=10, pady=10)

#COMENTARIO TEXTO***************************************
textoComentario = Text(miFrame, width="15", height="5")
textoComentario.grid(row=3, column=1, padx=10, pady=10)

scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=3, column=2, sticky="nsew", pady=10)

textoComentario.config(yscrollcommand=scrollVert.set)

#LABELS*************************************************
nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)
nombreLabel.config(bg="#c3e6d4")

notaLabel=Label(miFrame, text="Nota:")
notaLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)
notaLabel.config(bg="#c3e6d4")

comentarioLabel=Label(miFrame, text="Comentario:")
comentarioLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)
comentarioLabel.config(bg="#c3e6d4")

#FUNCION BOTON GUARDAR
def codigoBoton():
    nombresLista.append(cuadroNombre.get)
    print(nombresLista)



nombresLista = []

#BOTON GUARDAR***************************************
botonGuardar = Button(raiz, text="guardar", command=codigoBoton())
botonGuardar.pack()



raiz.mainloop()



