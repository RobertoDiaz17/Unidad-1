class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
#Aplicacion De La Herencia
class Estudiante(Persona):
    def __init__(self, nombre, edad, calificaciones=[]):
        super().__init__(nombre, edad)
        self.calificaciones = calificaciones
    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)
    def promedio_calificaciones(self):
        return sum(self.calificaciones) / len(self.calificaciones)
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Promedio de calificaciones: {self.promedio_calificaciones()}")
#Aplicacion De La Herencia
class Docente (Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    def calcular_salario(self, salario_por_hora, horas_por_semana):
        return salario_por_hora * horas_por_semana 
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Salario: {self.calcular_salario(float(input('Ingrese el salario por hora: ')), float(input('Ingrese las horas por semana: ')))}")        
# Ejemplo de uso:
nombre = input("Ingrese el nombre: ")
edad = int(input("Ingrese la edad: "))
estudiante = Estudiante(nombre, edad)
for i in range(3):
    estudiante.agregar_calificacion(float(input(f"Ingrese la calificación {i+1}: ")))
estudiante.mostrar_informacion()
nombre = input("Ingrese El Nombre Del Docente: ")
edad = int(input("Ingrese La Edad Del Docente: "))
docente = Docente (nombre, edad)
docente.mostrar_informacion()