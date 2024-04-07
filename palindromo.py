# PROGRAMA VERIFICA SE PALAVRA OU FRASE É UM PALINDROMO

from random import randint

lista_de_palavras_palindromas = ['Arara', 'Ana', 'Ada', 'Asa', 'Ele', 'Esse', 'Mamam', 'Matam', 'Mirim', 'Oco', 'Radar', 'Raiar', 'Osso', 'Ovo', 'Reler', 'Reviver', 'Rir', 'Salas', 'Socos', 'Saias', 'Sopapos']
lista_de_frases_palindromas = ['A base do teto desaba', 'A cara rajada da jararaca.', 'Acuda cadela da Leda caduca.',
                               'A dama admirou o rim da amada.', 'A Daniela ama a lei? Nada!', 'Adias a data da saída.',
                               'A diva em Argel alegra-me a vida.', 'A droga do dote é todo da gorda.', 'A gorda ama a droga.',
                               'A grama é amarga.', 'Aí, Lima falou: “Olá, família!”.', 'Ajudem Edu, já!', 'A lupa pula.',
                               'A mãe te ama.', 'A mala nada na lama.', 'Ame o poema.', 'A miss é péssima!', 'Anotaram a data da maratona.',
                               'A pateta ama até tapa.', 'Após a sopa.', 'Arara rara.', 'Ato idiota.', 'A torre da derrota.',
                               'E até o Papa poeta é.', 'Irene ri.', 'Luz azul.', 'Mega bobagem.', 'Missa é assim.', 'O céu sueco.',
                               'O galo ama o lago', 'Olá, galo!', 'O lobo ama o bolo.', 'Roma é amor.', 'Socorram-me, subi no ônibus em Marrocos.']

frase = input('Digite uma palavra ou frase: ').upper()

original = ''

# Removendo os espaços
for letra in range (0, len(frase)):
    if frase[letra] != ' ':
        original += frase[letra]

inverso = ''

# escrevendo ao contrario
for letra in range (len(original) -1, -1, -1): # PEGA AS LETRAS DO FIM ATÉ O INICIO
    inverso += original[letra]

# VERIFICA SE É UM PALINDROMO COMPARANDO O ORIGINAL COM O INVERSO
if original == inverso:
    print(f'É um palindromo!')
else:
    print('Não é um palindromo')

numero = randint(0, len(lista_de_frases_palindromas))
print('=-' * 20)
print('Um palindromo é uma palavra, frase ou número que permanece igual quando lida de trás para frente. Por Exemplo:')
print(lista_de_frases_palindromas[numero])
