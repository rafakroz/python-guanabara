# Aula 15
# Desafio 070
# Exercício 15.5
# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
# se o usuário vai continuar. No final, mostre:
# A - Qual é o total gasto na compra.
# B - Quantos produtos custam mais de R$ 1000
# C - Qual é o nome do produto mais barato.

cor = {'clear':      '\033[m',
       'bold':       '\033[1m',
       'blue':       '\033[34m',
       'blueBold':   '\033[1;34m',
       'cyan':       '\033[36m',
       'cyanBold':   '\033[1;36m',
       'green':      '\033[32m',
       'greenBold':  '\033[1;32m',
       'grey':       '\033[37m',
       'greyBold':   '\033[1;37m',
       'purple':     '\033[35m',
       'purpleBold': '\033[1;35m',
       'red':        '\033[31m',
       'redBold':    '\033[1;31m',
       'yellow':     '\033[33m',
       'yellowBold': '\033[1;33m',
       'blackWhite': '\033[7;30m'}

asteriscos = 60

print(f'*' * asteriscos) # --------------------------------------

produtoMaisBarato = ' '
total = qtdMaiorMil = maisBarato = qtdProd = 0

while True:
    produto = str(input('Qual produto: ')).strip()
    precoProd = float(input('Valor: R$'))
    qtdProd += 1
    total += precoProd
    
    print(f'*' * asteriscos) # --------------------------------------
    
    if precoProd > 1000:
        qtdMaiorMil += 1
    
    if qtdProd == 1 or precoProd < maisBarato:
        maisBarato = precoProd
        produtoMaisBarato = produto
    
    escolha = ' '
    
    while escolha not in 'SN':
        escolha = str(input(f'Adicionar mais produtos? [S/N] ')).strip().upper()[0]
    
    if escolha == 'N':
        break

print(f'*' * asteriscos) # --------------------------------------
print(f'O total gasto foi R${total:.2f}.')
print(f'{qtdMaiorMil} produtos custam acima de R$1.000.')
print(f'O produto mais barato é {produtoMaisBarato}, no valor de R${maisBarato:.2f}.')

print(f'*' * asteriscos) # --------------------------------------
