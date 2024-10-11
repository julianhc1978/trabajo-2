frase = input("ingrese la palabra o la frase:")
vocales = {"a":0, "e":0, "i":0, "o":0, "u":0}
for letra in frase:
    if letra in vocales:
        vocales[letra] += 1
for i, vocal  in vocales.items():
    print(f"las vocal {i} aparece {vocal} veces" )

