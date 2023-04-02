def power(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power(x * x, n // 2)
    else:
        return x * power(x, n - 1)

x = int(input("Entrez un nombre entier x : "))
n = int(input("Entrez un nombre entier n pour l'exposant : "))
print(x, "puissance", n, "est égal à", power(x, n))