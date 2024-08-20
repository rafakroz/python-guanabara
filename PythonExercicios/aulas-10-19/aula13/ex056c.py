# Aula 13
# Desafio 056
# Exercício 13.11
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres tem menos de 20 anos.

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

print(f'*' * asteriscos) # --------------------------------------

totalIdade = 0
media = 0

idademaisVelho = 0
nomeMaisVelho = ''
totalHomens = 0

totalMulheres = 0
totalMulheres20 = 0

for pessoa in range(1, 5):

    print(f'---- {pessoa}ª pessoa ----')
    
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip()
    
    totalIdade += idade
    
    print(f'*' * asteriscos) # --------------------------------------
    
    if pessoa == 1 and sexo in 'Mm':
        idademaisVelho = idade
        nomeMaisVelho = nome
    if idade > idademaisVelho and sexo in 'Mm':
        idademaisVelho = idade
        nomeMaisVelho = nome
    if sexo in 'Ff' and idade <= 20:
        totalMulheres20 += 1
        idadeMulher = idade
        nomeMulher = nome
    if sexo in 'Mm':
        totalHomens += 1
    if sexo in 'Ff':
        totalMulheres += 1

media = totalIdade / pessoa

print(f'A média de idade do grupo é {estilo["yellowBold"]}{media}{estilo["clear"]} anos de idade.')

if totalHomens == 0:
    print(f'{estilo["redBold"]}Não há homens na lista.{estilo["clear"]}')
else:
    if idademaisVelho == 1:
        print(f'{nomeMaisVelho} é único homem da lista e tem {idademaisVelho} anos de idade.')
    else:
        print(f'{nomeMaisVelho} é o homem mais velho com {idademaisVelho} anos de idade.')

if totalMulheres == 0:
    print(f'{estilo["redBold"]}Não há mulheres na lista.{estilo["clear"]}')
else:
    if totalMulheres == 1 and totalMulheres20 == 0:
        print(f'Há {totalMulheres} mulher na lista e ela tem idade acima de 20 anos.')
    elif totalMulheres > 1 and totalMulheres20 == 0:
        print(f'Há {totalMulheres} mulheres na lista e elas tem idade acima de 20 anos.')
    elif totalMulheres20 == 1:
        print(f'Na lista, apenas {nomeMulher} tem menos de 20 anos de idade.')
    else:
        print(f'O total de mulheres com menos de 20 anos de idade é de {totalMulheres20}')

print(f'*' * asteriscos) # --------------------------------------