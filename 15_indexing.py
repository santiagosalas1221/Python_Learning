

text = "El sabe programar"
# Ir a una pocision especifica
print(text[5])
print(text[1])

# Saber ultimo caracter del texto
size = len(text)
print("size", size)
print(text[size - 1])
# Alternativa para saber ultimo caracter de texto
print(text[size - 1])
print(text[-1])

# slicing obtener un rango segun la pocision exacta
print(text[8:17])
print(text[0:8])
# Desde una pocision hasta el final del texto
print(text[3:])
# Desde el inicio hasta el final
print(text[:])

# Saltos, tercer valor segun cuantos saltos quiero dar
print(text[10:17:1])
print(text[10:17:2])
print(text[::2])