#Escribir un programa que, dado un número entero, muestre su valor absoluto.

print("Valor absoluto de un número entero")

ejecutar = input("Desea ingresar? Si o No ")

while ejecutar == "si":
    numero = int(input("Escribe un número "))
    
    if numero>0:
        print("**********************************")
        print("El valor absoluto de " + str(numero) + " es " + str(numero))
        ejecutar = input("Desea ingresar otro número? Si o No ")
    else:
        valorAbsoluto = numero * -1
        print("**********************************")
        print("El valor absoluto de " + str(numero) + " es " + str(valorAbsoluto))
        ejecutar = input("Desea ingresar otro número? Si o No ")

print("Hasta pronto")

    
