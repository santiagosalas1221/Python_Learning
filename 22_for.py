
# decirle al ciclo que inicie en el numero uno y termine en el 20
'''
for element in range(1, 21):
    print(element)
'''
# recorrer una lista con el for iterando 5 veces de uno en uno
my_list = [23, 45, 67, 80, 10]
for element in my_list:
    print(element)

# iterar una tupla
my_tuple = ('santiago', 'nicolas')
for element in my_tuple:
    print(element)

product = {
    'name': 'camisa',
    'price': 100,
    'stock': 90
}

# leer la llave en un for de la lista
for key in product:
    print(key, '=>', product[key])