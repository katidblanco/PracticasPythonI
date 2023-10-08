# A lo largo del año, Viviana ha obtenido 8 calificaciones numéricas. 
# Escribir un programa que, a partir de una lista con esos valores, 
# obtenga su suma y su promedio. Mostrar en la pantalla los elementos de la lista, su suma y su promedio. 
# Pista: utiliza un bucle para recorrer la lista. 

notas = [] #creamos el arreglo, vector o lista



for i in range(1,5): #creamos un bucle FOR para ingresar elementos a la lista con el método append
    nota=float(input("Dime la nota No " + str(i) + ": "))
    notas.append(nota)

print("**************************")
print("las notas ingresadas son: ")
suma=0
for nota in notas:    #nota es la variable que contiene cada uno de los elementos del arreglo, notas es el arreglo o vector o lista
    suma = suma + nota
    prom = suma/4    
    print(nota) 

print("************************")
print("El promedio es: ", prom)

#print(notas)
    


