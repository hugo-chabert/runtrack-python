def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Entrez un nombre entier : "))
print("La factorielle de", n, "est", factorial(n))