# Ejercicio 1 (recogida de datos)
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
altura = float(input("Introduce tu altura en metros: "))
peso = float(input("Introduce tu peso en kg: "))

# Ejercicio 2 (funciones)
def saludar(nombre):
    return f"Hola {nombre}, ¡bienvenido!"

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Llamadas a las funciones
print(saludar(nombre))
imc = calcular_imc(peso, altura)
print(f"Tu IMC es: {imc:.2f}")