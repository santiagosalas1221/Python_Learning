# Crud listas

numbers = [1, 2, 3, 4, 5]
print(numbers[1])
#Cambiando el valor del ultimo elemento de la lista
numbers[-1] = 10
print(numbers)

#Agregar un valor al final de la lista
numbers.append(700)
print(numbers)
#Agregar elemento al inicio de la lista
numbers.insert(3, "hola")
print(numbers)

#Fusionar listas
tasks = ["todo 1", "todo 2", "todo 3"]
new_list = numbers + tasks
print(new_list)
#Preguntar en que pocision esta un elemento si no lo sabemos
index = new_list.index("todo 2")
new_list[index] = "todo changed"
print(new_list)

#Remover elementos de una lista
new_list.remove("todo 3")
print(new_list)

#Remueve el ultimo elemento de la lista siempre
new_list.pop()
print(new_list)
#Remueve el elemento de la lista indicado
new_list.pop(0)
print(new_list)

#Darle la vuelta a toda la lista
new_list.reverse()
print(new_list)

#Ordenar elementos de una lista
numbers_a = [1, 8, 6, 3]
numbers_a.sort()
print(numbers_a)
#Ordenar lista strings
strings = ['xy', 're', 'ab', 'ed']
strings.sort()
print(strings)