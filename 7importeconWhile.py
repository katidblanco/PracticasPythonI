#Calcula el importe, se ingresan la cantidad de productos 
#y el valor unitario de los productos

print("Calculamos el importe ")
cantidad = int(input ("Ingresa la cantidad "))

i = 1
suma = 0

while i<=cantidad:

    precioProducto= float((input("Ingresa el precio de producto No " + str(i) + ") ")))
    suma = suma + precioProducto
    i = i + 1
    
print("El importe es ", suma)  