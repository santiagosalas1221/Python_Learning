
# Transformaciones en Python

name = "Santiago"
print(type(name))
# Cambiando de forma dinamica el tipo de dato, ahora es INT
name = 12
print(type(name))

name = True
print(type(name))

# Tranformando el dato para poder concatenarlo
age = 25
print("Mi edad es: " + str(age))
print(f"Mi edad es: {age}")

# Convertir de String a int para poder realizar sumas
age = input("Digite su edad: ")
print(type(age))
age = int(age)
age += 10
print(f"Tu edad en 10 anios sera: {age}")