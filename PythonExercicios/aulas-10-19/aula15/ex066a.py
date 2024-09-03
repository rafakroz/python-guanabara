# Aula 15
# Desafio 066
# Exercício 15.1
# Crie um programa que leia vário números inteiros pelo teclado. O programa só vai parar quando
# o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

estilo = {'clear':        '\033[m',
          'bold':      '\033[1m',
          'blue':         '\033[34m',
          'blueBold':     '\033[1;34m',
          'cyan':         '\033[36m',
          'cyanBold':     '\033[1;36m',
          'green':        '\033[32m',
          'greenBold':    '\033[1;32m',
          'grey':        '\033[37m',
          'greyBold':    '\033[1;37m',
          'purple':     '\033[35m',
          'purpleBold': '\033[1;35m',
          'red':     '\033[31m',
          'redBold': '\033[1;31m',
          'yellow':      '\033[33m',
          'yellowBold':  '\033[1;33m',
          'blackWhite': '\033[7;30m'}

asteriscos = 60

qtdNums = soma = 0

print(f'*' * asteriscos) # --------------------------------------

while True:
    num = int(input(f'{qtdNums + 1}) Insira um número: '))
    if num == 999:
        break
    qtdNums += 1
    soma += num

print(f'*' * asteriscos) # --------------------------------------

if qtdNums == 1:
    print(f'Foi inserido {qtdNums}, no valor de {soma}.')
else:
    print(f'Foram inseridos {qtdNums} números.')
    print(f'A soma total é de {soma}.')

print(f'*' * asteriscos) # --------------------------------------