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
        freq[digit] = freq.get(digit, 0) + 1
    return freq
#endregion

#region Console Outputs
def printTable(data, headers):
    print("\n" + tabulate(data, headers=headers, tablefmt="fancy_grid"))
#endregion

#region Logical Expressions
def hasEvenAndOdd(s):
    hasEven = any(int(d) % 2 == 0 for d in s)
    hasOdd = any(int(d) % 2 != 0 for d in s)
    return hasEven and hasOdd

def isBalancedDiversity(set1, set2):
    simDiff = getSimmetricDifference(set1, set2)
    return hasEvenAndOdd(set1) and hasEvenAndOdd(set2) and len(simDiff) == 3

def isConcentratedSet(set1, set2):
    inter = getIntersection(set1, set2)
    perc1 = len(inter) / len(set1)
    perc2 = len(inter) / len(set2)
    return perc1 > 0.6 or perc2 > 0.6
def checkEvenOddConditions(s):
    hasEven = any(int(d) % 2 == 0 for d in s)
    hasOdd = any(int(d) % 2 != 0 for d in s)
    return hasEven, hasOdd

def getIntersectionPercentages(set1, set2):
    inter = getIntersection(set1, set2)
    perc1 = len(inter) / len(set1) * 100
    perc2 = len(inter) / len(set2) * 100
    return perc1, perc2
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
    baseInfo = [
        ["DNI 1", dni1, set1, sumSetElements(set1)],
        ["DNI 2", dni2, set2, sumSetElements(set2)],
    ]
    printTable(baseInfo, ["DNI", "Valor", "Conjunto", "Suma"])

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

    freqTable = [
        ["DNI 1", dni1, freq1],
        ["DNI 2", dni2, freq2],
    ]
    printTable(freqTable, ["DNI", "Valor", "Frecuencia"])

    # Balanced diversity details
    even1, odd1 = checkEvenOddConditions(set1)
    even2, odd2 = checkEvenOddConditions(set2)
    simDiff = getSimmetricDifference(set1, set2)
    cumpleDiversidad = even1 and odd1 and even2 and odd2 and len(simDiff) == 3

    diversityTable = [[
        "Diversidad equilibrada",
        "✅" if even1 and even2 else "❌",
        "✅" if odd1 and odd2 else "❌",
        "✅" if len(simDiff) == 3 else f"❌ ({len(simDiff)})",
        "✅" if cumpleDiversidad else "❌"
    ]]
    printTable(diversityTable, [
        "Expresión lógica",
        "Tiene par (A y B)",
        "Tiene impar (A y B)",
        "Diff. sim. = 3",
        "¿Cumple la expresión?"
    ])

    #  Concentrated set details
    perc1, perc2 = getIntersectionPercentages(set1, set2)
    cumpleConcentrado = perc1 > 60 or perc2 > 60

    concentrationTable = [[
        "Conjunto concentrado",
        f"{perc1:.1f}%",
        f"{perc2:.1f}%",
        "✅" if cumpleConcentrado else "❌",
        "✅" if cumpleConcentrado else "❌"
    ]]
    printTable(concentrationTable, [
        "Expresión lógica",
        "% intersección A",
        "% intersección B",
        "Alguno > 60%",
        "¿Cumple la expresión?"
    ])

if __name__ == "__main__":
    main()
#endregion
