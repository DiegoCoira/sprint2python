from random import randint
i = 1
g = 0
p = 0
start = str(input("Quieres jugar a piedra, papel, tijera?(s/n): "))
if start == "s":
    while i < 6:
        print("")
        print("Empieza la ronda número: "+ str(i))
        jugada=str(input("Elije una jugada(piedra, papel, tijera):"))
        n =int(randint(1,3))
        if n== 1:
            jugadaR="piedra"
        elif n == 2:
            jugadaR="papel"
        elif n == 3:
            jugadaR="tijera"
        
        if jugada == jugadaR:
                print("Empate, esta ronda no cuenta.")
        elif jugada == "piedra":
            if jugadaR == "papel":
                    print("Has perdido esta ronda.")
                    p = p +1
                    i = i +1
            elif jugadaR == "tijera":
                    print("Ronda ganada enhorabuena.")
                    g = g + 1
                    i = i +1

        elif jugada == "papel":
            if jugadaR == "piedra":
                print("Ronda ganada enhorabuena.")
                g = g +1
                i = i +1
            elif jugadaR == "tijera":
                print("Has perdido esta ronda.")
                p = p +1
                i = i +1
        
        elif jugada == "tijera":
            if jugadaR == "papel":
                print("Ronda ganada enhorabuena.")
                g = g +1
                i = i +1
            elif jugadaR == "piedra":
                print("Has perdido esta ronda.")
                p = p +1
                i = i +1

    print("")
    print("Has ganado: "+ str(g) + " veces y has perdido " + str(p) + " veces.")
    if g > p:
        print("Por lo tanto... ¡¡¡ENHORABUENA!!!, has ganado el juego.")
    else:
        print("Por lo tanto... Has perdido. La próxima vez será.")
else:
    print("Tu te lo pierdes.")