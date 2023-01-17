##Mini juego piedra papel o tijera

user_option = input("Piedra, Papel o Tijera?: ")
computer_option = "Piedra"

if user_option == computer_option:
    print("EMPATE!!")
elif user_option == "Papel":
    print("GANASTE!!")
elif user_option == "Tijera":
    print("PERDISTE!!")
