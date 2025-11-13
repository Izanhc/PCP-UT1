import random
import carga_palabras

GREEN_BG = "\033[42m"
YELLOW_BG = "\033[43m"
GRAY_BG = "\033[47m"
RESET = "\033[0m"

def colorear_letra(letra: str, estado: str) -> str :
    """ 
     La función recive una letra y y un estado de la letra y  devuelve la letra coloreada 
    """
    if estado == "verde":
        return f"{GREEN_BG} {letra.upper()} {RESET}"
    elif estado == "amarillo":
        return f"{YELLOW_BG} {letra.upper()} {RESET}"
    else:
        return f"{GRAY_BG} {letra.upper()} {RESET}"

# TODO_____________________

def elegir_palabra(palabras: list[str]) -> str: 
    """
    Selecciona aleatoriamente la palabra del día de la lista de palabras.

    Parámetros:
        palabras (list): lista de palabras en mayúsculas

    Retorna:
        str: palabra seleccionada
    """
    palabras: list[str] = []
    for palabra in carga_palabras.cargar_palabras_limpias():
        palabras.append(palabra)
        
    seleccionada = random.choice(palabras)
    print(f"Palabra seleccionada: {seleccionada}")
    return seleccionada


def comprobar_intento(palabra_secreta: str, intento: str):
    """
    Compara el intento con la palabra secreta y devuelve una lista indicando
    para cada letra si es:
        - "verde" -> letra correcta y en la posición correcta
        - "amarillo" -> letra presente en otra posición
        - "gris" -> letra no presente

    Parámetros:
        palabra_secreta (str): palabra a adivinar
        intento (str): intento del jugador

    Retorna:
        list[str]: lista de estados por letra
    """
    resultado = []
    for i, letra in enumerate(intento):
        if letra == palabra_secreta[i]:
            resultado.append("verde")
        elif letra in palabra_secreta:
            resultado.append("amarillo")
        else:
            resultado.append("gris")
    return resultado


def mostrar_feedback(intento, resultado):
    """
    Muestra el intento en la consola con feedback de colores.

    Parámetros:
        intento (str): palabra intentada
        resultado (list[str]): lista con estados por letra ("verde", "amarillo", "gris")

    Ejemplo:
        intento = "CASA"
        resultado = ["amarillo", "gris", "gris", "verde"]
        => se muestra cada letra con el color correspondiente
    """
    for letra, estado in zip(intento, resultado):
        print(colorear_letra(letra, estado), end="")
    print()  # salto de línea al final
    


def validar_intento(intento, palabras):
    """
    Valida que el intento:
      - tenga 5 letras
      - esté en la lista de palabras cargadas

    Parámetros:
        intento (str): intento del jugador
        palabras (list): lista de palabras válidas

    Retorna:
        bool: True si es válido, False si no
    """
    if len(intento) != 5:
        return False
    if intento not in palabras:
        return False
    return True


# Esto solo se ejecuta si ejecutamos esta librería directamente
# pero no si la importamos en otro fichero
if __name__ == "__main__":
  """  Ejemplo de uso:
  
  palabra = "carta"
  intento = "casas"

  resultado = []
  for i, letra in enumerate(intento):
      if letra == palabra[i]:
          resultado.append(colorear_letra(letra, "verde"))
      elif letra in palabra:
          resultado.append(colorear_letra(letra, "amarillo"))
      else:
          resultado.append(colorear_letra(letra, "gris"))

  print("".join(resultado))
  """
palabrafinal = elegir_palabra(carga_palabras.cargar_palabras_limpias())
for i in range(6):
    intento = input("Introduce tu intento (5 letras): ").strip().upper()
    if not validar_intento(intento, carga_palabras.cargar_palabras_limpias()):
        print("Intento inválido. Debe tener 5 letras y estar en la lista de palabras.")
        continue
    resultado = comprobar_intento(palabrafinal, intento)
    mostrar_feedback(intento, resultado)
    if intento == palabrafinal:
        print("¡Felicidades! Has adivinado la palabra.")
        break

    if i == 5:
        print(f"Lo siento, has agotado tus intentos. La palabra era: {palabrafinal}")




