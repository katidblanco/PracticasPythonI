class Empleado:

    def __init__(self, nombre, sueldo):
        self.nombre=nombre
        self.sueldo=sueldo


    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Sueldo: ", self.sueldo)

    def paga_imp(self):
        if self.sueldo>30000:
            print("Debe pagar impuesto")
        else:
            print("No paga impuestos")


#Main

empleado1=Empleado("Juan", 50000)
empleado1.imprimir()
empleado1.paga_imp()