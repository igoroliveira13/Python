# Recebe um CPF e verifica se é valido 

cpf = []

numero_digitado = [int(numero) for numero in input('Didite os numeros do CPF separados por espaço: ').split()]

cpf.extend(numero_digitado)

resultado_primeira_multiplicacao = 0
resultado_segundo_multiplicacao = 0

contador = 0

# Calculo do primeiro digito verificador
for numero in range(10, 1, -1):
    resultado_primeira_multiplicacao += numero * cpf[contador]
    contador += 1

contador = 1

# Calculo do segundo digito verificador
for numero in range(10, 1, -1):
    resultado_segundo_multiplicacao += numero * cpf[contador]
    contador += 1

# Calculando o digito verificardor
primeiro_digito_verificador = 11 - (resultado_primeira_multiplicacao % 11)
segundo_digito_verificardor = 11 - (resultado_segundo_multiplicacao % 11)

if cpf[9] == primeiro_digito_verificador and cpf[10] == segundo_digito_verificardor:
    print('Este é um CPF válido')
else:
    print('Verifique o numero digitado e tente novamente')

