# Pedimos al usuario una lista de números separados por comas
entrada = input("Introduce una lista de números separados por comas (por ejemplo: 4,5,6,7): ")
numeros = [int(num) for num in entrada.split(",")]

# Funciones para calcular suma, promedio, máximo y mínimo
def calcular_suma(lista):
    return sum(lista)

def calcular_promedio(lista):
    if lista:
        return sum(lista) / len(lista)
    return 0

def calcular_maximo(lista):
    if lista:
        return max(lista)
    return None

def calcular_minimo(lista):
    if lista:
        return min(lista)
    return None

# Calculamos los resultados
suma = calcular_suma(numeros)
promedio = calcular_promedio(numeros)
maximo = calcular_maximo(numeros)
minimo = calcular_minimo(numeros)

# Mostramos los resultados
print(f"La suma es {suma}, el promedio es {promedio}, el máximo es {maximo}, el mínimo es {minimo}.")