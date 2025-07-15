import math
import random


def aleatorio(a, b):
    n = b - a
    c = math.ceil(math.log(n, 2))
    r = n + 1
    while r > n:
        digitos = 0
        for i in range(c):
            pot = math.pow(2, i)
            randint = random.randint(0, 1)
            digitos += randint * pot
        r = digitos
    return a + r


print(aleatorio(0, 15))
