# Calcular fatorial de um numero

numero = int(input('Digite um numero para calcular o fatorial: '))
resultado = 0

while True:

    if resultado == 0:
        resultado = numero * (numero - 1)
    else:
        if numero == 1:
            break
        resultado *= numero - 1

    numero -= 1

print('=-' * 15)
print(f'O fatorial é: {resultado}')
print('Fim')