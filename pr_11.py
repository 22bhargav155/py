def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = 5
for i in range(1, n+1):
    print("Factorial of", i, "is", factorial(i))