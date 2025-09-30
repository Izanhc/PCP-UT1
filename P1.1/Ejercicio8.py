import sys

def main():
    # sys.argv es una lista con los argumentos de la línea de comandos
    # El primer elemento (posición 0) es siempre el nombre del archivo
    print("Argumentos recibidos:", sys.argv)

    # Si hay argumentos adicionales, los mostramos
    if len(sys.argv) > 1:
        nombre = sys.argv[1]
        print(f"Hola, {nombre} 👋")
    else:
        print("No se proporcionó ningún argumento")

if __name__ == "__main__":
    main()

#Extensión: añade más argumentos (por ejemplo, edad y ciudad) y muestra un mensaje con todos ellos usando f-strings.

import sys

def main():
    print("Argumentos recibidos:", sys.argv)

    if len(sys.argv) > 1:
        nombre = sys.argv[1]
        edad = sys.argv[2] if len(sys.argv) > 2 else "desconocida"
        ciudad = sys.argv[3] if len(sys.argv) > 3 else "desconocida"
        print(f"Hola, {nombre} 👋")
        print(f"Tienes {edad} años y vives en {ciudad}.")
    else:
        print("No se proporcionó ningún argumento")

if __name__ == "__main__":
    main()
