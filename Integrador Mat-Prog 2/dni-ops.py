# Debe instalar "tabulate" para poder visualizar las tablas y poder correr el programa:
# pip install tabulate

from tabulate import tabulate


#region Validations
def isValidDni(dni):
    return dni.isdigit() and len(dni) in (7, 8)

def isDniEqual(dni1, dni2):
    return dni1 == dni2
#endregion

#region Set Operations
def generateSet(dni):
    return set(dni)

def getUnion(set1, set2):
    return set1 | set2

def getIntersection(set1, set2):
    return set1 & set2

def getDifference(set1, set2):
    return set1 - set2

def getSimmetricDifference(set1, set2):
    return set1 ^ set2

def sumSetElements(s):
    return sum(int(i) for i in s)
def countDigitFrequency(dni):
    freq = {}
    for digit in dni:
        if digit in freq:
            freq[digit] += 1
        else:
            freq[digit] = 1
    return freq

#endregion

#region Console Outputs
def printTable(data,headers):
    print("\n" + tabulate(data, headers=headers, tablefmt="fancy_grid"))
#endregion

#region Main program
def main():
    while True:
        dni1 = input("Ingresa el DNI 1: ")
        dni2 = input("Ingresa el DNI 2: ")

        if not isValidDni(dni1) or not isValidDni(dni2):
            print("Ingresa DNIs válidos. (7 u 8 dígitos, solo números)")
            continue

        if isDniEqual(dni1, dni2):
            print("Los DNI deben ser diferentes.")
            continue

        break

    set1 = generateSet(dni1)
    set2 = generateSet(dni2)

    # Table with DNI, set and sum
    base_info = [
        ["DNI 1", dni1, set1, sumSetElements(set1)],
        ["DNI 2", dni2, set2, sumSetElements(set2)],
    ]
    printTable(base_info, ["DNI", "Conjunto", "Suma"])

    # Table with operations
    operations = [
        ["Unión", getUnion(set1, set2)],
        ["Intersección", getIntersection(set1, set2)],
        ["Diferencia (DNI1 - DNI2)", getDifference(set1, set2)],
        ["Diferencia (DNI2 - DNI1)", getDifference(set2, set1)],
        ["Diferencia simétrica", getSimmetricDifference(set1, set2)],
    ]

    printTable(operations, ["Operación", "Resultado"])

    # Table with frequencies
    freq1 = countDigitFrequency(dni1)
    freq2 = countDigitFrequency(dni2)

    freq_table = [
        ["DNI 1", dni1, freq1],
        ["DNI 2", dni2, freq2],
    ]
    printTable(freq_table, ["DNI", "Valor", "Frecuencia"])

if __name__ == "__main__":
    main()
#endregion
