# Pedimos los datos al usuario
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
altura = float(input("Introduce tu altura en metros: "))

# Mostramos el mensaje con f-string
print(f"Hola {nombre}, tienes {edad} años y mides {altura} metros.")

# Mostramos el tipo de cada variable
print("Tipo de 'nombre':", type(nombre))
print("Tipo de 'edad':", type(edad))
print("Tipo de 'altura':", type(altura))
