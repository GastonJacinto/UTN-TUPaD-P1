# Esto es para que Python me permita importar la funcion "menu" desde otro archivo, por la forma en la que esta estructurado el proyecto.
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#-----------Common imports-------------
from utils.utils import menu

import random

class tp4Controller:

  def desdeCeroHastaCien(self):
    #Ejercicio 1
    for i in range(101):
      print(i)
  
  def cuantosDigitosTiene(self):
    #Ejercicio 2
    num = int(input("Ingrese un número: "))
    print(f"El número {num} tiene {len(str(num))} dígitos")	

  def sumarValoresIntermedios(self):
    #Ejercicio 3

    num1= int(input("Ingrese un número: "))
    num2= int(input("Ingrese un número: "))
    suma = 0
    for i in range(min(num1, num2)+ 1, max(num1, num2) ):
      suma += i

    print(f"El resultado de la suma de los números que están entre {num1} y {num2} es {suma}")

  def sumarSecuenciaDeNumeros(self):
    #Ejercicio 4
    suma = 0
    while True:
      num = int(input("Ingrese un número (0 para salir): "))
      if num == 0:
        break
      suma += num

    print(f"La suma de los números ingresados es {suma}")

  def adivinarElNumero(self):
    #Ejercicio 5
    numSecreto = random.randint(0, 9)
    intentos = 0
    while True:
      num = int(input("Ingrese un número: "))
  
      intentos += 1
      if num == numSecreto:
        print(f"¡Adivinaste! Lo lograste en {intentos} intentos")
        break
  def imprimirNumerosParesEnOrdenDecreciente(self):
    #Ejercicio 6
    for i in range(100,0, -2):
      print(i)


  def calcularSumaEntreCeroYNumero(self):
    #Ejercicio 7

    num = int(input("Ingrese un número: "))
    suma = 0
    for i in range(0,num + 1):
      suma += i

    print(f"La suma de los números entre 0 y {num} es: {suma}")
  
  def calcularParesEImpares(self):
    #Ejercicio 8
    pares = 0
    impares = 0
    nums=10
    
    for i in range(nums):
      num = int(input("Ingrese un número: "))
      if num % 2 == 0:
        pares += 1
      else:
        impares += 1

    print(f"Se ingresaron {pares} números pares y {impares} números impares")
    
  def calcularPromedio(self):
    #Ejercicio 9
    suma = 0
    nums = 10

    for i in range(nums):
      suma += int(input("Ingrese un número: "))

    print(f"El promedio de los números ingresados es: {suma/nums}")

  def invertirDigitos(self):
    #Ejercicio 10
    num = int(input("Ingrese un número: "))
    invertedNum = "".join(reversed(str(num)))
    print(f"El número {num} invertido es: {invertedNum}")



  def imprimirHastaElSieteYFrenarEnNueve(self):
    #Ejercicio 11
    for i in range(1,10):
      if i == 7:
        continue
      print(i)
      if i == 9:
        break

def main():
  menu(tp4Controller())
if __name__ == "__main__":
     main()
