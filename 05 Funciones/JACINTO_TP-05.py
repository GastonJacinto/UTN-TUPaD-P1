# Esto es para que Python me permita importar la funcion "menu" desde otro archivo, por la forma en la que esta estructurado el proyecto.
import sys
import os
import math
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#-----------Common imports-------------
from utils.utils import menu

class tp4Controller:
  def imprimirHolaMundo(self):
    # Ejercicio 1
    print("Hola, mundo!")
  def saludarUsuario(nombre):
    # Ejercicio 2
    print(f"Hola, {nombre}!")
  def informacionPersonal(nombre, apellido,edad,residencia):
    # Ejercicio 3
    print(f"Soy {nombre} {apellido}, tengo {edad} y vivo en {residencia}")
  def areaYPerimetro():
    # Ejercicio 4
    def calcularArea(radio):
      return math.pi * radio ** 2
    def calcularPerimetro(radio):
      return 2 * math.pi * radio

    radio = float(input("Cual es el radio? "))
    area = calcularArea(radio)
    perimetro = calcularPerimetro(radio)
    print(f"El area es {area} y el perimetro es {perimetro}")
  def segundosAHoras():
    # Ejercicio 5
    segundos = int(input("Cuantos segundos quieres convertir? "))
    horas = segundos / 3600
    print(f"{segundos} segundos son {horas} horas ")

  def tablaMultiplicar():
    # Ejercicio 6
    def imprimirTabla(x):
      for i in range(1, 11):
        print(f"{x} x {i} = {x * i}")
    num = int(input("Ingrese un número: "))
    imprimirTabla(num)
  def operacionesBasicas(a,b):
    # Ejercicio 7
    def ops(a,b):
      return a + b, a - b, a * b, a / b if b != 0 else "No se puede dividir por cero"
    resultado = ops(a,b)
    print("Resultados de las operaciones básicas:")
    print(f"Suma: {resultado[0]}")
    print(f"Resta: {resultado[1]}")
    print(f"Multiplicación: {resultado[2]}")
    print(f"División: {resultado[3]}")
  def calcularImc():
    # Ejercicio 8
    def calcularIMC(peso, altura):
      return peso / (altura ** 2)
    peso = float(input("Cual es tu peso en kg? "))
    altura = float(input("Cual es tu altura en metros? "))
    imc = calcularIMC(peso, altura)
    print(f"Tu IMC es {imc}")
  def celsiusAFarenheit():
    # Ejercicio 9
    def convert(celcius):
      return (celcius * 1.8) + 32
    celcius = float(input("Cual es la temperatura en Celcius? "))
    fahrenheit = convert(celcius)
    print(f"La temperatura en Fahrenheit es {fahrenheit}")
  def calcularPromedio():
    # Ejercicio 9
    def prom(nums):
      return sum(nums) / len(nums)
    nums = []
    for i in range(3):
      nums.append(int(input("Ingrese un numero: ")))
    promedio = prom(nums)
    print(f"El promedio de los numeros ingresados es: {promedio}")
