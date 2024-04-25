# Gera numeros aleatoriamente para jogos da Mega Sena

from random import randint

gerados = []

while len(gerados) < 6:
    numero = randint(1, 10)
    if numero in gerados:
        continue
    else:
        gerados.append(numero)
gerados = sorted(gerados)
print(gerados)
