from math import *

# Reszta z dzielenia
print(10%2.7)

# Wartość bezwzględna
numero = -10
print(abs(numero))

# Potęgowanie 3^2
print(pow(3,2))

# Znajdowanie max
print(max(1,40,100))

# Zaokrąglanie
print(round(3.49))

# Zaokrąglanie w dół
print(floor(3.2))

# Zaokrąglanie w górę
print(ceil(3.2))

# Pierwiastkowanie
print(sqrt(36))


def power(a: int, b: int):
    result = 1
    for index in range(0, b):
        result = result*a
    return result

print("The result of 3^5 is: " + str(power(3,5)))



