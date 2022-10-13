respuesta= ''
print("Cual de estos personajes es un centinela")
print("a) Sage.")
print("b) Raze.")
print("c) Jett.")
respuesta = input("Elige una(a,b,c): ")
if respuesta == 'a':
    print("Correcto")
elif respuesta == 'b':
    print("Fallo")
elif respuesta == 'c':
    print("Incorrecto")
else:
    print("Formato no soportado")