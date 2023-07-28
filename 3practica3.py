
#Calcula el importe, se ingresan la cantidad de productos 
#y el valor unitario de los productos
#****Convertimos a flotante los numeros ingresados por input directamente*****

print("Calculamos el importe ")
cantidad = float(input ("Ingresa la cantidad "))# float: convertimos a decimal o real el ingreso por teclado
valorUnitario = float(input("Ingresa el valor unitario ")) # float: convertimos a decimal o real el ingreso por teclado

importe = cantidad * valorUnitario
print("El importe es ", importe)