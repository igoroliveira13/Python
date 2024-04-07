# Verifica se um numero é primo

numero = int(input('Digite um numero: ')) # Recebe o numero para analisar

lista_divisores = [] # lista para armazenar os numeros divisores

for c in range (1, numero + 1):
    if numero % c == 0:
        lista_divisores.append(c)

print('~' * 22)

if len(lista_divisores) == 2: # Se o numero digitado tiver somente 2 divisores 1 e ele mesmo, é primo.
    print(f'O numero {numero} é primo')
else:
    print(f'O numero {numero} não é primo')
