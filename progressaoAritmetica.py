# Codigo le o primeiro termo e a razao de uma PA. No final, mostra a quantidade de termos solicitada

quantidade_termos = int(input('Quantidade de termos da PA: '))

inicio = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

numero_termos = inicio + (quantidade_termos - 1) * razao

lista_termos = []

for c in range (inicio, numero_termos + 1, razao):
    lista_termos.append(c)
print(lista_termos)

