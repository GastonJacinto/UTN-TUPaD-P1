import re
import inspect
def camelCaseAOracion(cadena):
    oracion = re.sub(r'([A-Z])', r' \1', cadena).capitalize()
    return oracion

def menu(controller):
    # Recibo el controller y obtengo los métodos de la clase
    # que no comienzan con "_", o sea solo los metodos publicos de la clase.
    metodos = {
        i + 1: funcion 
        # El inspect.getmembers es como un Object.entries en Js, retorna todos los miembros de un objeto como pares key, value. El predicate es una funcion que filtra los miembros.
        # En este caso, solo quiero los metodos, por eso uso inspect.ismethod.
        for i, (nombre, funcion) in enumerate(inspect.getmembers(controller, predicate=inspect.ismethod))
        # El nombre de la funcion no debe empezar con "_", para que no me traiga los metodos privados.
    }

    eleccion = 1
    while eleccion != 0:
        print("\n------------------ OPCIONES ------------------")
        for numero, funcion in metodos.items():
            print(f"{numero} - {camelCaseAOracion(funcion.__name__)}")
        print("0 - Salir")
        print("----------------------------------------------")

        try:
            eleccion = int(input("Elegí un método. Usá 0 para salir: "))
            if eleccion in metodos:
                metodos[eleccion]()
            elif eleccion != 0:
                print("Método no encontrado")
        except ValueError:
            print("Por favor, ingresá un número válido.")
