# ciclos while en python
# ciclo infinito
'''
while True:
    print('se ejecuto')

counter = 0

while counter < 10:
    counter += 1
    print(counter)


# detener el ciclo cuando lo requiera con break
counter = 0
while counter < 20:
    counter += 1
    if counter == 15:
        break
    print(counter)
'''

# continue nos permite pasar a la siguiente iteracion saltandose lo que siga de ahi en adelnate
counter = 0
while counter < 20:
    counter += 1
    if counter < 15:
        continue
    print(counter)
