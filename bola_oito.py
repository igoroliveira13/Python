'''
Usuario faz uma pergunta ao código e o mesmo responde com sim, não e talvez
'''

from random import randint
respostas = ['Os planos do universo estão alinhados com os seus.', 'Não em um futuro próximo. Mas se insistir nesse caminho obterá sucesso.', 'Você esta diante de uma bifurcação, seu futuro se divide da mesma forma que os caminhos a sua frente.']

while True:
    numero = randint (0, 2)

    usuario = input('O que deseja saber: ')

    print(respostas[numero])

