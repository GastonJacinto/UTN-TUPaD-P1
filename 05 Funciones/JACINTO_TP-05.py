# Esto es para que Python me permita importar la funcion "menu" desde otro archivo, por la forma en la que esta estructurado el proyecto.
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#-----------Common imports-------------
from utils.utils import menu

class tp4Controller:

  def numerosDelUnoAlCienMultiplosDeCuatro(self):
    for i in range(4, 101, 4):
      print(i)

  def mostrarPenultimoElementoDeUnaLista(self):
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"El penultimo elemento de la lista es: {lista[-2]}")

  def agregarTresPalabrasALista(self):
    lista = []
    for i in range(3):
      palabra = input("Ingrese una palabra: ")
      lista.append(palabra)

    print(f"La lista con las palabras es: {lista}")

  def reemplazarSegundoYUltimoElementoDeListaDeAnimales(self):
    animales=["perro","gasto","conejo","pez"]

    animales[1]= "loro"
    animales[-1]= "oso"

    print(f"La lista con los animales reemplazados es: {animales}")

  def explicacionDeRemoveConMax(self):
    numeros= [8,15,3,22,7]
    maxNum = max(numeros)
    print(f"El elemento con el mayor valor de la lista es: {maxNum}")
    print(f"Por lo que si ejecutamos lo siguiente: numeros.remove(max(numeros))")
    numeros.remove(maxNum)
    print("Lo que se está haciendo es remover el numero más alto que se encuentre en el array de numeros.")
    print(f"Por lo tanto, la lista sin el elemento con el mayor valor es: {numeros}")
  def listaDelDiezAlTreintaConSaltosDeCincoYMostrarDosUltimos(self):
    lista = []
    for i in range(10, 31, 5):
      lista.append(i)

    print(f"La lista es: {lista}")
    print(f"Los dos ultimos elementos de la lista son: {lista[-2:]}")
    
  def reemplazarDosValoresCentralesDeLista(self):
    autos = ["sedan","polo","suran","gol"]

    autos[1] = "hb20"
    autos[-2] = "corsa"

    print(f"La lista con los autos reemplazados es: {autos}")

  def agregarDobleDeCincoDiezYQuince(self):
    dobles = []
    for i in range(5, 16, 5):
      dobles.append(i*2)

    print(f"La lista con los dobles de 5, 10 y 15 es: {dobles}")

  def compras(self):
    compras=[["pan","leche"],["arroz","fideos","salsa"],["agua"]]
    print(f"Estado actual de la lista: {compras}")
    compras[2].append("jugo")
    print(f"Agregar 'jugo' a la tercera lista: {compras}")
    compras[1][1] = "tallarines"
    print(f"Reemplazar 'fideos' por 'tallarines': {compras}")
    compras[0].remove("pan")
    print(f"Remover 'pan' de la primera lista: {compras}")
    print(f"Estado final de la lista: {compras}")
  
  def listaAnidada(self):
    listaAnidada = [15, True,[25.5,57.9,30.6],False]
    print(f"La lista anidada es: {listaAnidada}")
def main():
  menu(tp4Controller())
if __name__ == "__main__":
     main()
