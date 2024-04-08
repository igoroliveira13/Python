from random import randint

numero_tentativas = 0
numero_sorteado = randint(1, 10)

print('=-' * 15)
print('===== JOGO ADIVINHAÇÃO =====')
print('=-' * 15)

print('Pensei em um numero entre 1 e 10. Consegue adivinhar qual é?')

while True:
    palpite = int(input('Digite seu palpite: '))

    # Verifica se o numero esta dentro do intervalo informado
    if palpite < 1 or palpite > 10:
        print('O numero em que pensei está entre 1 e 10.')
        numero_tentativas += 1
        continue

    # Verifica se o usuario acertou
    if palpite == numero_sorteado:
        numero_tentativas += 1
        print('Parabéns. Você acertou!')
        print(f'Acertou após {numero_tentativas} tentativa(s)')
        break
    elif palpite < numero_sorteado:
        print('É um numero maior. Tente novamente')
        numero_tentativas += 1
    elif palpite > numero_sorteado:
        print('É um numero menor. Tente novamente')
        numero_tentativas += 1

print('Obrigado por jogar!')