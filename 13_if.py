if True:
    print("deberia ejecutarse")

pet = input("Cual es su mascota favorita? ")
if pet == "perro":
    print("Su mascota es un perro")

elif pet == "gato":
    print("su mascota favorita es gato")

elif pet ==  "pez":
    print("Excelente noticia")
else:
    print("No tienes una mascota conocida")

stock = int(input("Digite el stock: "))
if 100 <= stock <= 1000:
    print("El stock es correcto")
else:
    print("El stock es incorrecto")


# par o impar

num = int(input("Digite un numero: "))
if num % 2 == 0:
    print("El numero ingresado es par", num)
else:
    print("numero ingresado es impar", num)

