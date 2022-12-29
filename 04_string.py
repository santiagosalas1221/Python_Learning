
# Detalles strings en Python
my_name = input("Cual es su nombre? ")
my_lastName = input("Cual es su apellido? ")
my_age = input("Cual es su edad?")
blank_space = " "

print("Los valores digitados son: ", my_name + blank_space + my_lastName)

# Manipular formato en Python con format

template = "Hola, mi nombre es: " + my_name + " y mi apellido es: " + my_lastName + " " + "y tengo " + my_age + " " + "anios"
print("Version 1", template)

template = "Hola mi nombre es: {} y mi apellido es: {} y tengo {} anios".format(my_name, my_lastName, my_age)
print("Version 2", template)

template = f"Hola mi nombre es {my_name} y mi apellido es {my_lastName} y tengo {my_age} anios"
print("Version 3", template)