# 1. Escribir un programa que, dado un número entero, muestre su valor absoluto.
# El valor absoluto de un número es su positivo.

# numero=int(input("dime un número"))
# if (numero<0):
#     print("el valor absoluto de ", numero , "es ", numero*-1)
# else:
#     print("el valor absoluto de ",str(numero) , "es ", numero)


# 2. Elaborar un programa que solicite los precios de los artículos comprados,
# Escribe 0 para finalizar
# al finalizar debes mostrar cuantos artículos se compraron y el importe total.
# aplicar una validación para que ningún artículo tenga un precio menor de 1000 $.


# precio = 0
# importe=0
# cont=0

# precio= float(input("Dime el precio del artículo o escribe fin para finalizar "))
# if(precio==0):
#     print("Hasta luego")
# else:
    
#     if(precio<1000):
#         print("el precio no es correcto") 
#     else:       
#         while(precio>=1000 and precio!=0):        
#             importe=importe+precio
#             cont=cont + 1
#             precio= float(input("Dime el precio del artículo o escribe fin para finalizar "))
#             if(precio<1000):
#                 precio=0    

# print("El importe es", importe)
# print("Cantidad de artículos: ", cont)

#Para calcular el gasto de una línea de producción solicitamos: La cantidad de productos y el gasto unitario de cada uno 
#Mostrar en pantalla el gasto el gasto total

# cantArt=int(input("dime la cantidad de artículos: "))

# i=0
# suma=0
# for i in range(1, cantArt+1):
#     gasto=float(input("dime el gasto del artículo " + str(i) + ": " ))
#     suma=suma+gasto

# print("Gasto total: ", suma)









