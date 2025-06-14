def isLeapYear(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

birthYears = []
print("Ingrese los años de nacimiento uno por uno. Escriba 0 para finalizar.")

while True:
    userInput = input("Año: ")
    if userInput == "0":
        break
    try:
        year = int(userInput)
        birthYears.append(year)
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un año válido.")

currentYear = 2025
ages = [currentYear - year for year in birthYears]

evenYears = []
oddYears = []
leapYears = []
allAfter2000 = True

for year in birthYears:
    if year % 2 == 0:
        evenYears.append(year)
    else:
        oddYears.append(year)
    if isLeapYear(year):
        leapYears.append(year)
    if year <= 2000:
        allAfter2000 = False

print("Número de cumpleaños en años pares:", len(evenYears), ":", evenYears)
print("Número de cumpleaños en años impares:", len(oddYears), ":", oddYears)

if allAfter2000:
    print("Grupo Z")
if leapYears:
    print("Tenemos un año especial:", leapYears)

cartesianProduct = [(year, age) for year in birthYears for age in ages]
print("Producto cartesiano de años de nacimiento y edades:")
print(cartesianProduct)
