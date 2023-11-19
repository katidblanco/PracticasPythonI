'''
Plantear una clase que administre dos listas de 5 nombres de alumnos y sus notas. 
Mostrar un menú de opciones que permita:

1- Cargar alumnos.

2- Listar alumnos.

3- Mostrar alumnos con notas mayores o iguales a 7. 

4- Finalizar programa.
'''

class AdministradorAlumnos:
    def __init__(self):
        self.nombres = []
        self.notas = []

    def cargar_alumnos(self):
        for i in range(5):
            nombre = input("Ingrese el nombre del alumno {}: ".format(i + 1))
            nota = float(input("Ingrese la nota del alumno {}: ".format(i + 1)))
            self.nombres.append(nombre)
            self.notas.append(nota)
        print("Alumnos cargados exitosamente.")

    def listar_alumnos(self):
        print("Lista de Alumnos:")
        for nombre, nota in zip(self.nombres, self.notas):
            print("Nombre: {}, Nota: {}".format(nombre, nota))

    def alum_aprobados(self):
        print("Alumnos con notas mayores o iguales a 7:")
        for nombre, nota in zip(self.nombres, self.notas):
            if nota >= 7:
                print("Nombre: {}, Nota: {}".format(nombre, nota))

    def ejecutar_programa(self):
        while True:
            print("\nMenú de Opciones:")
            print("1- Cargar alumnos.")
            print("2- Listar alumnos.")
            print("3- Mostrar alumnos con notas mayores o iguales a 7.")
            print("4- Finalizar programa.")

            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == '1':
                self.cargar_alumnos()
            elif opcion == '2':
                self.listar_alumnos()
            elif opcion == '3':
                self.alum_aprobados()
            elif opcion == '4':
                print("Programa finalizado.")
                break
            else:
                print("Opción no válida. Por favor, elija una opción válida.")

# Uso de la clase
admin_alumnos = AdministradorAlumnos()
admin_alumnos.ejecutar_programa()