import random
from statistics import mean, median, mode
import datetime 
import re

def camelCaseAOracion(text: str) -> str:
    # Un espacio entre cada palabra
    words = re.sub(r'(?<!^)(?=[A-Z])', ' ', text).lower()
    # Mayúscula a la primera letra
    return words.capitalize()
class tp3Controller:
  def esMayorDeEdad(self):
    #Ejercicio 1
    edad = int(input("Ingrese su edad: "))
    if edad >= 18:
      print("Es mayor de edad")
    else:
      print("Es menor de edad")

  def aprobado(self):
    #Ejercicio 2
    nota = int(input("Ingrese su nota: "))
    if nota >= 6:
      print("Aprobado")
    else:
      print("Desaprobado")

  def esPar(self):
    #Ejercicio 3
    while True:
      num = int(input("Ingrese un numero: "))
      if num % 2 == 0:
        print("Ha ingresado un número par")
      else:
        print("Por favor, ingrese un número par")

      salir = input("Salir? (s/n) ").strip().lower()
      if salir == 's':
        break
  def edadYCategoria(self):
  #Ejercicio 4
   edad = int(input("Ingrese su edad: "))
   if edad<12:
      print("Categoria Niño/a")
   elif edad>=12 and edad<18:
     print("Categoria Adolescente")
   elif  edad>=18 and edad<30:
      print("Categoria Adulto/a joven")
   else:
     print("Categoría Adulto/a")
  def longitudDeContraseña(self):
    #Ejercicio 5
    MIN_LENGTH = 8
    MAX_LENGTH = 14
    while True:
      password = input("Ingrese una contraseña: ")
      if len(password) >= MIN_LENGTH and len(password) <= MAX_LENGTH:
        print("Ha ingresado una contraseña correcta")
        break
      else:
        print(f"Por favor, ingrese una contraseña de entre {MIN_LENGTH} y {MAX_LENGTH} caracteres")
  def calcularSesgo(self):
    #Ejercicio 6
    RANDOM_NUMS = [random.randint(1, 100) for i in range(50)]

    media = mean(RANDOM_NUMS)
    mediana = median(RANDOM_NUMS)
    moda = mode(RANDOM_NUMS)
    print(f"Media: {media}") 
    print(f"Mediana: {mediana}")
    print(f"Moda: {moda}")
    print('------------------')
    sesgoPositivo = media>mediana and mediana>moda
    sesgoNegativo = media<mediana and mediana<moda
    sesgoNulo = media == moda and mediana == moda
    # Si ninguna condición se cumple, puedo considerarlo sesgo indefinido.
    # Ejemplo: Media=47.06, Mediana=47, Moda=47.
    sesto = "positivo" if sesgoPositivo else ("negativo" if sesgoNegativo else ("nulo" if sesgoNulo else "indefinido"))

    print(f"Sesgo: {sesto}")

  def terminaConVocal(self):
    #Ejercicio 7
    palabra = input("Ingrese una palabra: ")
    if palabra[-1] in "aeiouAEIOU":
      print(f"{palabra}!")
    else:
      print(f"{palabra}")

  def opcionesNombre(self):
    # Ejercicio 8
    nombre = input("Ingresa tu nombre: ")
    while True:
        print("Usa un número del 1 al 3 para elegir una opción.")
        print("1 - Escribir mi nombre en mayúsculas")
        print("2 - Escribir mi nombre en minúsculas")
        print("3 - Escribir mi nombre con la primera letra mayúscula")

        try:
            opcion = int(input("Selecciona la opción deseada: "))
            match opcion:
                case 1:
                    print(nombre.upper())
                    break
                case 2:
                    print(nombre.lower())
                    break
                case 3:
                    print(nombre.title())
                    break
                case _:
                    print("Opción inválida, por favor selecciona una opción de las listadas.")
        #El except acá sirve por si el user ingresa una letra. 
        except ValueError:
            print("Por favor ingresa un número válido.")

  def magnitudTerremoto(self):
    #Ejercicio 9
      magnitud = float(input("Ingresa la magnitud del terremoto: "))
      
      if magnitud<3:
        print("Muy leve.")
      elif magnitud>=3 and magnitud<4:
        print("Leve")
      elif magnitud>=4 and magnitud<5:
        print("Moderado")
      elif magnitud>=5 and magnitud<6:
        print("Fuerte")
      elif magnitud >= 6 and magnitud<7:
        print("Muy fuerte")
      else:
        print("Extremo")

  def determinarEstaciones(self):
    #Ejercicio 10
    hemisferio = input("¿En qué hemisferio te encuentras? (Norte o Sur) (N/S): ").strip().upper()
    dia = int(input("¿Qué día es?: "))
    mes = int(input("¿Qué mes del año es? Usa su número (Por ejemplo: Marzo = 3): "))
    año = int(input("¿Qué año es?: "))
    
    fecha_actual = datetime.date(año, mes, dia)

    # Genero tuplas para los rangos de las fechas
    fecha_invierno = (datetime.date(año, 12, 21), datetime.date(año + 1, 3, 20))
    fecha_primavera = (datetime.date(año, 3, 21), datetime.date(año, 6, 20))
    fecha_verano = (datetime.date(año, 6, 21), datetime.date(año, 9, 20))
    fecha_otonio = (datetime.date(año, 9, 21), datetime.date(año, 12, 20))

    # Uso la tupla para determinar la estación
    if fecha_invierno[0] <= fecha_actual <= fecha_invierno[1]:
        estacion_norte = "Invierno"
        estacion_sur = "Verano"
    elif fecha_primavera[0] <= fecha_actual <= fecha_primavera[1]:
        estacion_norte = "Primavera"
        estacion_sur = "Otoño"
    elif fecha_verano[0] <= fecha_actual <= fecha_verano[1]:
        estacion_norte = "Verano"
        estacion_sur = "Invierno"
    elif fecha_otonio[0] <= fecha_actual <= fecha_otonio[1]:
        estacion_norte = "Otoño"
        estacion_sur = "Primavera"
    else:
        print("Fecha fuera de rango.")
        return

    if hemisferio == "N":
        print(f"Estás en el hemisferio norte y la estación es: {estacion_norte}")
    elif hemisferio == "S":
        print(f"Estás en el hemisferio sur y la estación es: {estacion_sur}")
    else:
        print("Hemisferio no válido. Por favor ingresa N o S.")


def main():
  ctrl = tp3Controller()
  opciones = {
          1: ctrl.esMayorDeEdad,
          2: ctrl.aprobado,
          3: ctrl.esPar,
          4: ctrl.edadYCategoria,
          5: ctrl.longitudDeContraseña,
          6: ctrl.calcularSesgo,
          7: ctrl.terminaConVocal,
          8: ctrl.opcionesNombre,
          9: ctrl.magnitudTerremoto,
          10: ctrl.determinarEstaciones,
      }

# Un compañero me mostró este menú, me pareció bueno, asi que decidí implementarlo también pero con algunos cambios.
  eleccion = 1
  while eleccion != 0:
    print("------------------OPIONES------------------")
    for opcion in opciones:
      print(f"{opcion} - {camelCaseAOracion(opciones[opcion].__name__)}")
    print("-------------------------------------------")

    eleccion = int(input(f"Elegí un método. Usa 0 para salir: "))
    if eleccion in opciones:
      opciones[eleccion]()

    elif eleccion != 0:
      print("Método no encontrado")

if __name__ == "__main__":
     main()




