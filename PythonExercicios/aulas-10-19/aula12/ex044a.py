# Aula 12
# Desafio 044
# Elabore um programa que calcule o valor a ser pago por produto, considerando o seu
# preço normal e condição de pagamento:
# À vista dinheiro / Pix / débito / Boleto: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

asteriscos = 60

print(f'*' * asteriscos)

valor = float(input('Valor do produto: '))

print(f'''
===========================
=  Tipos de pagamento:    =
=  [1] Dinheiro           =
=  [2] Pix                =
=  [3] Boleto             =
=  [4] Débito             =
=  [5] Cartão de Crédito  =
===========================
''')

condPag = int(input('Tipo de pagamento: '))

if condPag == 1:
    tipopg = 'Dinheiro'
elif condPag == 2:
    tipopg = 'Pix'
elif condPag == 3:
    tipopg = 'Boleto'
elif condPag == 4:
    tipopg = 'Débito'
elif condPag == 5:
    tipopg = 'Cartão de Crédito'

print(f'*' * asteriscos)

if condPag == 1 or condPag == 2 or condPag == 3 or condPag == 4:
    novoValor = valor - (valor * 10 / 100)
    
    print(f'Valor produto: R${valor:.2f}')
    print(f'Forma de Pagamento: {tipopg}')
    print(f'Desconto de 10%.')
    print(f'Valor final R${novoValor:.2f}')

elif condPag == 5:

    parcela = int(input('Quantidade de Parcelas (Até 10x): '))

    if parcela == 1:
        novoValor = valor - (valor * 5 / 100)
        valorParcelas = novoValor / parcela
        
        print(f'Valor produto: R${valor:.2f}')
        print(f'Forma de Pagamento: {tipopg}')
        print(f'Desconto de 5%.')
        print(f'Parcelado em: {parcela}x de R${valorParcelas:.2f}')
        print(f'Valor final produto: R${novoValor:.2f}')

    elif parcela == 2:
        valorParcelas = valor / parcela
        
        print(f'Valor produto: R${valor:.2f}')
        print(f'Forma de Pagamento: {tipopg}')
        print(f'Parcelado em: {parcela}x de R${valorParcelas:.2f}')
        print(f'Valor final produto: R${valor:.2f}')

    elif 3 <= parcela <= 10:
        novoValor = valor + (valor * 20 / 100)
        valorParcelas = novoValor / parcela
        
        print(f'Valor produto: R${valor:.2f}')
        print(f'Forma de Pagamento: {tipopg}')
        print(f'Acréscimo de 20%.')
        print(f'Parcelado em: {parcela}x de R${valorParcelas:.2f}')
        print(f'Valor final produto: R${novoValor:.2f}')
        
elif condPag > 5:
    
    print('Condição de pagamento inválida!')

print(f'*' * asteriscos)
