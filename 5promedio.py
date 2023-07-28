#Aldo quiere comprobar si con las tres notas que tiene en Historia 
#está aprobado o no. Para ayudarlo, escribe un programa que le solicite 
#los tres valores, y que luego muestre el promedio de sus notas.

print("Promedio de notas")
nota1 = float(input("Ingrese 1ra nota "))
nota2 = float(input("Ingrese 2da nota "))
nota3 = float(input("Ingrese 3ra nota "))

promedio= (nota1 + nota2 + nota3)/3

if promedio>=7:
   print("promedio: ", promedio)
   print("APROBADO")
else:
    print("promedio: ", promedio)
    print("DESAPROBADO")
