class Persona:
    def inicializar(self, nom):
        self.nombre=nom

    def mostrar(self):
        print("Nombre: ", self.nombre)


persona1=Persona()
persona1.inicializar("juan")
persona1.mostrar()

persona2=Persona()
persona2.inicializar("Sofia")
persona2.mostrar()