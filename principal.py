from factorial import func_factorial

print("a)Factorial con recursividad")
print("b)Factorial sin recursividad")
print("")
opcion= str(input("Elige una opción(a,b):"))
print("")
if opcion == "a":
    n = int(input("Dame un número: "))
    solucion=func_factorial(n)
    
if opcion == "b":
    n = int(input("Dame un número: "))
    solucion2=func_factorial2(n)
    
print("El numero factorial de " + str(n) + " es: "+ str(solucion) + ".")