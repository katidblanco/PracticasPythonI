#Crear una aplicación que permita el ingreso de las notas de un estudiante y a través de la selección
#de opciones permita: Ingresar notas, Mostrar notas, Sumar notas, Eliminar notas, Calcular el promedio y Salir

#FUNCION INGRESAR NOTAS**************************
def ingresarNotas(ingresar):
        print("_______________________________")
        print ("INGRESAR NOTAS -0- para salir")
        ingresar = "0"
        while ingresar != "menu": 
              ingresar = float(input()) #//5
               
              if int(ingresar)>1 and int(ingresar) <= 10: #// 5
                  notasValidas.append(ingresar)
                  
              else:
                  if int(ingresar)<0 or int(ingresar) > 10:
                       print("Esta nota no es válida")
                       print ("Ingresa nota válida, -0- para salir\n")

                  else:
                      ingresar="menu"

#FUNCION SUMAR NOTAS**************************                    
def sumarNotas(notas):
         print("_______________________________")
         print("SUMAR NOTAS INGRESADAS:\n")
         suma=0
         for nota in notas:              
              suma = suma + nota
         return suma                      

#FUNCIÓN ELIMINAR NOTA************************
def eliminarNota(eliminar):
         print("_______________________________")
         print("ELIMINAR NOTA:\n")
         notaEliminada = float(input("Escribe la nota que desea eliminar: ") )
         notasValidas.remove(notaEliminada)
         return notaEliminada
                      

def promedioNotas(nota):
     suma=sumarNotas(notasValidas)
     promedio = suma/len(notasValidas)
     return promedio



#INICI0***************************************

print("CALIFICACIONES")

notasValidas = []

menu = input("Escribe -menu- para ver el Menú de opciones \n")

while menu == "menu":
   print("________________________________")
   print("MENÚ DE OPCIONES")
   print("Elige una opción:")
   print("1-Ingresar nota")
   print("2-Mostrar notas ingresadas")
   print("3-Sumar notas ingresadas")
   print("4-Eliminar nota")
   print("5-Calcular promedio")
   print("6-Salir")
   print("________________________________")

   opcion = input()

   match opcion:
    case "1":
        ingresarNotas(notasValidas)    
      
    case "2":                      #INGRESAR NOTAS
        print("_______________________________")
        print("NOTAS INGRESADAS:\n")
        for nota in notasValidas:
            print (nota)

    case "3":                      #SUMAR NOTAS
        suma = sumarNotas(notasValidas)
        print ("La Suma de las notas es: ", suma) 

    case "4":
        notaEliminada = eliminarNota(notasValidas) #ELIMINAR NOTAS
        print("Nota ", notaEliminada, " eliminada con éxito" )
         

    case "5":                      #PROMEDIO DE NOTAS
         print("_______________________________") 
         print("PROMEDIO DE NOTAS:\n")
         promedio=promedioNotas(notasValidas)      
         print ("El promedio de las notas es: ",promedio)

    case "6":                     #SALIR*************
         print("_______________________________")
         print("SALIR:\n")
         salir = input("¿Confirma que desea salir? -si- ó -no-\n")
         if salir == "si":
             menu="si"
             print("Hasta pronto")
         else:
            menu = "menu"


              
        
        
          
            

            




