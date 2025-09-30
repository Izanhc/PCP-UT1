# Pedimos los datos al usuario
nombre = input("Introduce tu nombre: ")

while True:
    try:
        edad = int(input("Introduce tu edad: "))
        break
    except ValueError:
        print("Por favor, introduce un número entero válido para la edad.")

while True:
    try:
        altura = float(input("Introduce tu altura en metros: "))
        break
    except ValueError:
        print("Por favor, introduce un número decimal válido para la altura.")

# Mostramos el mensaje con f-string
print(f"Hola {nombre}, tienes {edad} años y mides {altura} metros.")

# Mostramos el tipo de cada variable
print("Tipo de 'nombre':", type(nombre))
print("Tipo de 'edad':", type(edad))
print("Tipo de 'altura':", type(altura))
