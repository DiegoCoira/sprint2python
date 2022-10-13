
print("Cual de estos personajes es un centinela")
print("a) Sage.")
print("b) Raze.")
print("c) Jett.")
respuesta = input("Elige una(a,b,c): ")

if respuesta == 'a':
    resultado = 10
elif respuesta == 'b':
    resultado = -5
elif respuesta == 'c':
    resultado = -5
else:
    resultado = -5

print("Cual de estos personajes es un duelista")
print("a) Skye.")
print("b) Reyna.")
print("c) Killjoy.")
respuesta = input("Elige una(a,b,c): ")

if respuesta == 'a':
    resultado = resultado -5
elif respuesta == 'b':
    resultado = resultado +10
elif respuesta == 'c':
    resultado = resultado - 5
else:
    resultado = resultado -5

print("Cual de estos personajes es un iniciador")
print("a) Kayo.")
print("b) Viper.")
print("c) Neon.")
respuesta = input("Elige una(a,b,c): ")

if respuesta == 'a':
    resultado = resultado +10
elif respuesta == 'b':
    resultado = resultado + -5
elif respuesta == 'c':
    resultado = resultado + -5
else:
    resultado = resultado + -5

print(" ")
print("tu nota es un " + str(resultado) + "/30")
