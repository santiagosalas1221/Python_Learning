text = "El sabe Programar en python"
print("java" in text)
print("programar" in text)

# Busqueda de una palabra dentro de un texto
if "python" in text:
    print("Elegiste bien")
else:
    print("Tambien ha elegido bien")

# saber cuantos caracteres tiene
size = len("hola")
print(size)

# pasar a mayusculas o minusculas el texto
print(text, text.upper())
print(text, text.lower())
# contar cuantas veces aparece una letra en el texto
print(text.count("y"))

# Invierte las letras de mayusculas a minusculas y viceversa
print(text.swapcase())

# Preguntar si el texto inicia con esa plabra
print(text.startswith("El"))
print(text.endswith("java"))

# Reemplazar texto
print(text.replace("python", "Javascript"))

text_2 = "este es un titulo"
print(text_2)
# Pone la primera letra en mayuscula
print(text_2.capitalize())
# Pone la primer letra de cada palabra en mayuscula
print(text_2.title())
# Nos dice si es un digito
print(text_2.isdigit())
print("398".isdigit())

