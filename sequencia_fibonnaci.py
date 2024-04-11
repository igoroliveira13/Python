quantidade_termos = int(input('Quantos termos da sequencia deseja: '))

contador = 0

primeiro = 0
segundo = 1
terceiro = 1

while quantidade_termos != contador:
    print(f'{primeiro}' , end=' ')
    primeiro = segundo
    segundo = terceiro
    terceiro = primeiro + segundo

    contador += 1
