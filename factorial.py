def func_factorial(n):
    if n == 0:
        return 1
    else:
        return n*func_factorial(n-1)

print(func_factorial(0))