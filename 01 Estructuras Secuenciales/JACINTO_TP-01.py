print('-------------Ejercicio 1------------')
print('Hola mundo')

print('-------------Ejercicio 2------------')
nom = input("Como te llamas?")
print(f'Hola {nom}')


print('-------------Ejercicio 3------------')
nom = input("Como te llamas? ")
app = input("Cual es tu apellido? ")
edad = input("Cual es tu edad? ")
address = input("Cual es tu dirección? ")

print(f'Soy {nom} {app}, tengo {edad} años y vivo en {address}')


print('-------------Ejercicio 4------------')
radio = float(input("Cual es el radio? "))
pi = 3.1416
area = pi * radio ** 2
perimetro = 2 * pi * radio
print(f'El area es {area} y el perimetro es {perimetro}')


print('-------------Ejercicio 5------------')
segundos = int(input("Cuantos segundos? "))
horas: float = segundos / 3600
print(f'{segundos} segundos son {horas} horas ')


print('-------------Ejercicio 6------------')
num = int(input("De que numero quieres la tabla de multiplicar? "))
for i in range(1, 11):
    print(f'{num} x {i} = {num * i}')


while True:
    print('-------------Ejercicio 7------------')
    num1 = float(input("Cual es el primer numero? Debe ser distinto de 0 "))
    num2 = float(input("Cual es el segundo numero? Debe ser distinto de 0 "))

    if num1 == 0 or num2 == 0:
        print("Ambos numeros deben ser distintos de 0")
        continue  

    print(f'{num1} + {num2} = {num1 + num2}')
    print(f'{num1} - {num2} = {num1 - num2}')
    print(f'{num1} * {num2} = {num1 * num2}')
    print(f'{num1} / {num2} = {num1 / num2}')

    salir = input("Salir? (s/n) ").strip().lower()
    if salir == 's':
        break


print('-------------Ejercicio 8------------')
altura = float(input("Cual es tu altura en metros? "))  
peso = float(input("Cual es tu peso en kg? "))
imc = peso / (altura ** 2)
print(f'Tu IMC es {imc}')


print('-------------Ejercicio 9------------')
celcius = float(input("Cual es la temperatura en Celcius? "))
fahrenheit = (celcius * 1.8) + 32
print(f'La temperatura en Fahrenheit es {fahrenheit}')


print('-------------Ejercicio 10------------')
num1 = float(input("Cual es el primer numero? "))
num2 = float(input("Cual es el segundo numero? "))
num3 = float(input("Cual es el tercer numero? "))
promedio = (num1 + num2 + num3) / 3
print(f'El promedio de los 3 numeros es {promedio}')
