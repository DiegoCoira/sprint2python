from factorial import func_factorial

n = int(input("Dame un número: "))
solucion=func_factorial(n)
solucion2=func_factorial2(n)
print("El numero factorial de " + str(n) + " es: "+ str(solucion) + ".")