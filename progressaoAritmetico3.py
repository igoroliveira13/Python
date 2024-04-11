inicio = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
contador_termos = 0
fim = 10
continuar = True

while continuar != False:
    print(f'{inicio} - ', end='')
    contador_termos += 1
    inicio += razao
    if contador_termos == fim:
        print('PAUSA')
        mais = int(input('Deseja mostrar mais quantos termos dessa PA: '))
        fim += mais
        if mais == 0:
            continuar = False
print(f'Progressão finalizada com {contador_termos} termos mostrados.')
