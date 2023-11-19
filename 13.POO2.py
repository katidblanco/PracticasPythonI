class Operacion:

    def __init__(self):
        self.valor1=int(input("Ingresa un número"))
        self.valor2=int(input("Ingresa otro número"))
        self.sumar()
        self.restar()
        self.mult()
        self.divicion()


    def sumar(self):
        suma=self.valor1+self.valor2
        print("La suma es", suma)



    def restar(self):
        resta=self.valor1-self.valor2
        print("La resta es", resta)


    
    def mult(self):
        multiplicar=self.valor1*self.valor2
        print("El producto es", multiplicar)


    def divicion(self):
        if self.valor2 != 0:
            dividir = self.valor1 / self.valor2
            print("La division es", dividir)
        else:
            print("No se puede dividir por cero.")
            

#Main

operacion1=Operacion()