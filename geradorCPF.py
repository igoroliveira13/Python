# Gera numeros automaticamente e faz a verificação se é um numero de CPF válido em seguida

# =============== Parte 1 - gera os numeros randomicamente ===============
from random import randint

# função que gera os numeros
def GerarNumeros():
    numeros_gerados = []
    while len(numeros_gerados) != 11:
        numero = randint(0, 9)
        numeros_gerados.append(numero)
    return(numeros_gerados)

# =============== parte 2 - verifica se o numero gerado é um CPF válido ===============
tentativas = 0

while True:
    numeros_gerados = GerarNumeros()

    total_primeira_multiplicacao = total_segunda_multiplicacao = 0
    primeito_digito_verificador = segundo_digito_verificardor = 0

    contador = 0

    for numero in range(10, 1, -1):
        total_primeira_multiplicacao += numero * numeros_gerados[contador]
        contador += 1

    primeito_digito_verificador = 11 - (total_primeira_multiplicacao % 11)

    contador = 1

    for numero in range(10, 1, -1):
        total_segunda_multiplicacao += numero * numeros_gerados[contador]
        contador += 1
    
    segundo_digito_verificardor = 11 - (total_segunda_multiplicacao % 11)

    if numeros_gerados[9] == primeito_digito_verificador and numeros_gerados[10] == segundo_digito_verificardor:
        print('=-' * 20)
        print(f'Este é um CPF gerador automaticamente {numeros_gerados}')
        print(f'Gerado após {tentativas} tentativas')
        break
    else:
        tentativas += 1
        print(f'Tentativa numero {tentativas}º')
        continue



    