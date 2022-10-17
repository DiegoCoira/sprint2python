from random import randint
resultado = 0
n =int(randint(1,3))
if n ==1:
    #Primera pregunta
    print("Cual de estos personajes es un centinela")
    print("a) Sage.")
    print("b) Raze.")
    print("c) Jett.")
    respuesta = input("Elige una(a,b,c): ")
    #Comprobacion respuestas
    if respuesta == 'a':
        resultado = 10
    elif respuesta == 'b':
        resultado = -5
    elif respuesta == 'c':
        resultado = -5
    else:
        resultado = -5

if n == 2:
    #Segunda pregunta
    print("Cual de estos personajes es un duelista")
    print("a) Skye.")
    print("b) Reyna.")
    print("c) Killjoy.")
    respuesta = input("Elige una(a,b,c): ")
    #Comprobación respuestas
    if respuesta == 'a':
        resultado = resultado -5
    elif respuesta == 'b':
        resultado = resultado +10
    elif respuesta == 'c':
        resultado = resultado - 5
    else:
        resultado = resultado -5
        
if n == 3:
    #Tercera pregunta
    print("Cual de estos personajes es un iniciador")
    print("a) Kayo.")
    print("b) Viper.")
    print("c) Neon.")
    respuesta = input("Elige una(a,b,c): ")
    #Comprobación respuestas
    if respuesta == 'a':
        resultado = resultado +10
    elif respuesta == 'b':
        resultado = resultado + -5
    elif respuesta == 'c':
        resultado = resultado + -5
    else:
        resultado = resultado + -5



#Segunda pregunta aleatoria
l =int(randint(1,3))
if int(l) == int(n):
    while l == n:
        l =int(randint(1,3))
    
if l ==1:
    #Primera pregunta
    print("Cual de estos personajes es un centinela")
    print("a) Sage.")
    print("b) Raze.")
    print("c) Jett.")
    respuesta = input("Elige una(a,b,c): ")
    #Comprobacion respuestas
    if respuesta == 'a':
        resultado = 10
    elif respuesta == 'b':
        resultado = -5
    elif respuesta == 'c':
        resultado = -5
    else:
        resultado = -5

if l == 2:
    #Segunda pregunta
    print("Cual de estos personajes es un duelista")
    print("a) Skye.")
    print("b) Reyna.")
    print("c) Killjoy.")
    respuesta = input("Elige una(a,b,c): ")
    #Comprobación respuestas
    if respuesta == 'a':
        resultado = resultado -5
    elif respuesta == 'b':
        resultado = resultado +10
    elif respuesta == 'c':
        resultado = resultado - 5
    else:
        resultado = resultado -5

if l == 3:
    #Tercera pregunta
    print("Cual de estos personajes es un iniciador")
    print("a) Kayo.")
    print("b) Viper.")
    print("c) Neon.")
    respuesta = input("Elige una(a,b,c): ")
    #Comprobación respuestas
    if respuesta == 'a':
        resultado = resultado +10
    elif respuesta == 'b':
        resultado = resultado + -5
    elif respuesta == 'c':
        resultado = resultado + -5
    else:
        resultado = resultado + -5


#Print para crear espacio entre la ultima pregunta y la respuesta
print(" ")
#Resultado Final
print("tu nota es un " + str(resultado) + "/20")
