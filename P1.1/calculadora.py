# calculadora.py
import sys
import emoji

def mostrar_ayuda():
    print(emoji.emojize(":cross_mark: Error: Uso incorrecto."))
    print(emoji.emojize("Uso: python calculadora.py <num1> <operador> <num2>"))
    print(emoji.emojize("Operadores válidos: +, -, *, /"))

def calcular(num1, operador, num2):
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        if num2 == 0:
            print(emoji.emojize(":warning: No se puede dividir entre cero"))
            return None
        return num1 / num2
    else:
        print(emoji.emojize(":cross_mark: Operador inválido"))
        return None

def main():
    if len(sys.argv) != 4:
        mostrar_ayuda()
        return

    try:
        num1 = float(sys.argv[1])
        operador = sys.argv[2]
        num2 = float(sys.argv[3])
    except ValueError:
        mostrar_ayuda()
        return

    resultado = calcular(num1, operador, num2)
    if resultado is not None:
        print(emoji.emojize(f":white_check_mark: Resultado: {num1} {operador} {num2} = {resultado}"))

if __name__ == "__main__":
    main()
