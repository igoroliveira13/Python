# Fatorial com metodo

from math import factorial

numero = int(input('Digite um numero e veja o fatorial: '))

fatorial = factorial(numero)

while numero != 0:
    if numero == 1:
        print(f'{numero} ', end='')
        break
    print(f'{numero} X ', end='')
    numero -= 1
print(f'= {fatorial}')

