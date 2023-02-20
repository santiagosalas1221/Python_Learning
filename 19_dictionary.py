# Diccionarios en python

my_dict = {}
print(type(my_dict))

my_dict = {
    "avion" : "definicion de avion ..",
    "name" : "santiago",
    "last_name" : "salas carrera",
    "age" : "25"
}

print(my_dict)
print(len(my_dict))

# Como leer el diccionario, preguntar por la llave sin saber la pos
print(my_dict["age"])
print(my_dict["last_name"])

#Get sirve por que si no existe python lo manejara para evitar que se reviente le programa
print(my_dict.get("age"))
print(my_dict.get("jfjf"))

#Como validar el dato para saber si existe o no y evitar que se reviente el programa
print("avion" in my_dict)
print("NO existe" in my_dict)

