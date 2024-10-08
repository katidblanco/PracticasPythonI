"""
#Ejercicio 1: Calcular el promedio de 5 notas con While
cont=0
suma=0
nota=0

print("***Calcular promedio con WHILE 1***") 

while cont<5:
    nota=int(input("Ingresa la nota"))
    suma=suma+nota
    cont=cont+1

prom=suma/cont
print("El promedio es ", prom)

"""
#***************************************************************
#Ejercicio 2: Calcular el promedio de 5 notas con While, hacer una validación
#para las notas ingresadas donde muestre un mensaje de error si la nota es mayor que 10.
"""
cont=0
suma=0
nota=0

print("***Calcular promedio con WHILE 2***") 

while cont<5:       
    nota=int(input("Ingresa la nota No "+ str(cont+1) + ": "))
    if nota>10 or nota<0:
        print("La nota ingresada no es válida")
    else:
        suma=suma+nota
        cont=cont + 1 #cont=+1
prom=suma/cont
print("El promedio es ", prom)
"""
#***************************************************************
#Ejercicio 3: Calcular el promedio de 5 notas con FOR, hacer una validación
#para las notas ingresadas donde muestre un mensaje de error si la nota es mayor que 10.
"""
cont=0
suma=0
nota=0

print("***Calcular promedio con FOR***") 

for i in range(1,6):       
    nota=int(input("Ingresa la nota No "+ str(cont+1) + ": "))
    if nota>10 or nota<0:
        print("La nota ingresada no es válida")
    else:
        suma=suma+nota
        cont=cont + 1 #cont=+1
prom=suma/cont
print("El promedio es ", prom)
"""
#*********************************************************
#Ejercicio 4 para trabajar solos: 
#Teresa acaba de comenzar a trabajar en un quiosco. Le interesa saber, al final del día, 
# cuanto suman las ventas que ha efectuado a lo largo de la jornada. Escribir un programa 
# que le solicite a Teresa el monto de cada una de las compras. Cómo se desconoce la cantidad 
# de datos que cargarán, el ingreso de datos finaliza cuando Teresa ingresa una venta con 
# monto 0. Al finalizar, informar el total recaudado.
"""
cont=0
venta=0
suma=0
print("***************************")
print("Calcular el total de ventas")
print("***************************")

while venta >= 0:
    venta=float(input("ingresa el importe de la venta No " + str(cont+1) + ": "))
    if venta>0:
        suma=suma+venta
        cont=cont + 1
    else:
        break
print("**********************************")
print("Se realizaron", cont, "ventas ")
print("El total de las ventas es: ", suma)

"""