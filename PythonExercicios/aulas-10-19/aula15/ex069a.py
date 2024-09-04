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
idade = stop =qtdPessoas18 = qtdHomens = qtdMulheres20 = 0
sexo = ''

while True:
    sexo = str(input(f'Sexo da pessoa ({pessoa}): ')).strip()
    idade = int(input(f'Idade: '))
    print(f'*' * asteriscos) # --------------------------------------
    
    if idade >= 18:
        qtdPessoas18 += 1
        
    if sexo in 'm':
        qtdHomens += 1
        
    if (sexo in 'f') and (idade <= 20):
        qtdMulheres20 += 1
        
    stop = int(input(f'[0] para continuar ou [1] para finalizar.'))
    print(f'*' * asteriscos) # --------------------------------------
    
    if stop == 0:
        pessoa += 1
    else:
        print(f'Quantidade pessoas com mais de 18 anos: {qtdPessoas18}')
        print(f'Quantidade de homens: {qtdHomens}')
        print(f'Quantidade de mulheres com menos de 20 anos: {qtdMulheres20}')
        print(f'*' * asteriscos) # --------------------------------------
        break
