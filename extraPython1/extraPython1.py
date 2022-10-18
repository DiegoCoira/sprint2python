from random import randint
opc = 1
i = 1
g = 0
p = 0
start = str(input("Quieres jugar a piedra, papel, tijera?(s/n): "))
if start == "s":
    while i < 6:
        print("")
        print("Empieza la ronda número: "+ str(i))
        for opc in range(1):
            jugada=str(input("Elije una jugada(piedra, papel, tijera):"))
            n =int(randint(1,3))
            if jugada != "piedra" and jugada != "papel" and jugada != "tijera":
                print("")
                print("Eso no sirve :(, vuelve a elegir.")
                print("")
                print("")
                
            if n== 1:
                jugadaR="piedra"
                opc = opc + 1
            elif n == 2:
                jugadaR="papel"
                opc = opc + 1
            elif n == 3:
                jugadaR="tijera"
                opc= opc + 1
                
            
        
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
    if g> 1 and p > 1:
        print("Has ganado "+ str(g) + " veces y has perdido " + str(p) + " veces.")
    
    if g == 1:
        print("Has ganado "+ str(g) + " vez y has perdido " + str(p) + " veces.")
    
    if p == 1:
        print("Has ganado "+ str(g) + " vez y has perdido " + str(p) + " vez.")
         
    if g > p:
        print("Por lo tanto... ¡¡¡ENHORABUENA!!!, has ganado el juego.")
    else:
        print("Por lo tanto... Has perdido. La próxima vez será.")
else:
    print("Tu te lo pierdes.")