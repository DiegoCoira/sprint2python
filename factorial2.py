def func_factorial2(n):
    if n <= 0:
        return 1
    factorial = 1
    while n > 0:
        factorial = factorial * n
        n -= 1
    return factorial

print(func_factorial2(7))