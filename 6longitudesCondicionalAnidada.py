#Un pie equivale a 12 pulgadas y una pulgada son 2,54 cm. 
#Escribir un programa que pida al usuario una longitud expresada en pies y pulgadas 
#y que escriba esa longitud en centímetros.

print("Conversor de longitudes")
um = input("Qué desea ingresar, pies o pulgadas ")

if um == "pies" or um == "pie" or um == "Pie" or um == "Pies" or um == "PIE" or um == "PIES":
    pies = float(input("ingrese pies: "))
    pulgadas = pies*12
    centimetros= pulgadas*2.54
    print("la medida en pulgadas es: ", pulgadas)
    print("la medida en centímetros es: ", centimetros, "cm")

if um == "pulgadas" or um == "pulgada" or um == "Pulgada" or um=="Pulgadas":
    pulgadas = float(input("ingrese pulgadas: "))
    pies = pulgadas/12
    centimetros= pulgadas*2.54
    print("la medida en pies es: ", pies, "pies")
    print("la medida en centímetros es: ", centimetros, "cm")

else:
    print("El valor ingresado no es válido, ingrese pies o pulgadas")
