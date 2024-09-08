# Aula 15
# Desafio 069
# Exercício 15.4
# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoas cadastrada, o programa deverá
# perguntar se o usuário quer ou não continuar. No final mostre:
# A - Quantas pessoas tem mais de 18 anos.
# B - Quantos homens foram cadastrados.
# C - Quantas mulheres tem menos de 20 anos.

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

pessoa = 1
total18 = 0
totalHomens = 0
totalMulheres = 0

while True:
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input(f'Sexo da pessoa ({pessoa}): ')).strip().upper()[0]
    idade = int(input(f'Idade: '))
    
    if idade >= 18:
        total18 +=1
    
    if sexo == 'M':
        totalHomens += 1
    
    if sexo == 'F' and idade < 20:
        totalMulheres += 1
    
    pessoa += 1
    
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input(f'Quer continuar [S / N]? ')).strip().upper()[0]
    
    if resposta == 'N':
        break

print('Programa finalizado!')
print(f'Total de pessoas com mais de 18 anos: {total18}.')

if totalHomens == 0:
    print(f'Nenhum homem foi cadastrado!')
elif totalHomens == 1:
    print(f'Ao todo temos {totalHomens} homem cadastrado.')
else:
    print(f'Ao todo temos {totalHomens} homens cadastrados.')

if totalMulheres == 0:
    print(f'Nenhuma mulher foi cadastrada!')
elif totalMulheres == 1:
    print(f'E temos {totalMulheres} mulher com menos de 20 anos.')
else:
    print(f'E temos {totalMulheres} mulheres com menos de 20 anos.')