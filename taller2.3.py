def filtrar_palabras_por_letra():
    palabras = []  # Lista para almacenar las palabras ingresadas por el usuario

    # Pedir palabras al usuario hasta que ingrese "salir"
    while True:
        palabra = input("Ingresa una palabra (o 'salir' para terminar): ")
        if palabra.lower() == 'salir':  # Finalizar cuando el usuario ingrese 'salir'
            break
        palabras.append(palabra)  # Agregar la palabra a la lista

    # Pedir la letra por la cual se filtrarán las palabras
    letra = input("Ingresa la letra por la cual quieres filtrar las palabras: ").lower()

    # Filtrar palabras que comiencen con la letra ingresada
    palabras_filtradas = [palabra for palabra in palabras if palabra.lower().startswith(letra)]

    # Imprimir las palabras que comienzan con la letra
    print(f"Palabras que comienzan con '{letra}': {palabras_filtradas}")


# Llamar a la función
filtrar_palabras_por_letra()