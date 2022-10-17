from factorial import func_factorial
import time
from datetime import datetime
from factorial2 import func_factorial2

print("a)Factorial con recursividad")
print("b)Factorial sin recursividad")
print("")
opcion= str(input("Elige una opción(a,b):"))
print("")
if opcion == "a":
    n = int(input("Dame un número: "))
    start_time = time.time()
    solucion=func_factorial(n)
    end_time = time.time()
    
if opcion == "b":
    n = int(input("Dame un número: "))
    start_time = time.time()
    end_time = time.time()
    solucion=func_factorial2(n)
    
    
    
print("El numero factorial de " + str(n) + " es: "+ str(solucion) + ".")
print("La ejecución tardo " + str(end_time-start_time) + " en ejecutarse.")