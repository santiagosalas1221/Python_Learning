##Mini juego piedra papel o tijera

user_option = input("Piedra, Papel o Tijera?: ")
user_option = user_option.lower()
computer_option = "piedra"
computer_option = computer_option.lower()

if user_option == computer_option:
    print("EMPATE!!")
elif user_option == "papel":
    print("GANASTE!!")
elif user_option == "tijera":
    print("PERDISTE!!")
