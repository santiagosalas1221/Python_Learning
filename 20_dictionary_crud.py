# Como mutar datos de un diccioario

person = {
    'name' : 'santiago',
    'last_name': 'salas',
    'langs' : ['python', 'java'],
    'age' : 25
}

print(person)

# modificando el diccionario en el campo nombre por otro nombre
person['name'] = 'otro nombre'
print(person)

# restandoel datos al diccionario en el campo edad
person['age'] -= 5
print(person)

# como agregar dentro de la lista del diccionario
person['langs'].append('rust')
print(person)

# eliminando el campo apellido del diccionario con del
del person['last_name']
print(person)
# otra forma de eliminar elementos con pop
person.pop('age')
print(person)

# como traer items, valores y llaves del diccionario
print('items')
print(person.items())
#
print('keys')
print(person.keys())
#
print('values')
print(person.values())


