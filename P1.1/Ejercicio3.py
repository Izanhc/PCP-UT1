def presentar_persona(nombre="Usuario", edad=None, *aficiones):
    if edad is None:
        mensaje = f"{nombre} no ha indicado su edad."
    else:
        mensaje = f"{nombre} tiene {edad} años"
    
    if aficiones:
        # Unimos la lista de aficiones en una cadena separada por comas
        mensaje += " y le gusta: " + ", ".join(aficiones)
    
    print(mensaje)


#   Pruebas
presentar_persona("Izan", 20, "leer", "correr", "viajar")
presentar_persona("Luis", 30, "dibujar")
presentar_persona("Marta")  # solo nombre, sin edad ni aficiones
presentar_persona()         # sin argumentos, usa valores por defecto