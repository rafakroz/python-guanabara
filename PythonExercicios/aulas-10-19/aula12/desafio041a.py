# Aula 12
# Desafio 041
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e
# mostre sua categoria, de acordo com a idade: 
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 25 anos: SÊNIOR
# Acima: MASTER

from datetime import date

estilo = {'clear':        '\033[m',
          'bold':      '\033[1m',
          'blue':         '\033[34m',
          'blueBold':     '\033[1;34m',
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

print(f'{estilo["grey"]}*{estilo["clear"]}' * asteriscos)

nome = str(input('Nome do aluno: ')).strip()
anoNasc = int(input('Ano de nascimento: '))

anoAtual = date.today().year
# anoAtual = 2017 ano aula
idade = anoAtual - anoNasc

print(f'''
===========================
= \033[7m     \033[1mFAIXAS ETÁRIAS    \033[m =
=  {estilo["purpleBold"]}Até 9 anos: MIRIM{estilo["clear"]}      =
=  {estilo["yellowBold"]}Até 14 anos: INFANTIL{estilo["clear"]}  =
=  {estilo["blueBold"]}Até 19 anos: JUNIOR{estilo["clear"]}    =
=  {estilo["greenBold"]}Até 20 anos: SÊNIOR{estilo["clear"]}    =
=  {estilo["redBold"]}Acima: MASTER{estilo["clear"]}          =
===========================
''')

print(f'{estilo["grey"]}*{estilo["clear"]}' * asteriscos)

print(f'{estilo["blueBold"]}Aluno: {nome}{estilo["clear"]}')
print(f'Ano de Nascimento: {anoNasc}')

if anoNasc > anoAtual:
    print(f'{estilo["redBold"]}Erro! Insira um ano abaixo do atual!{estilo["clear"]}')
else:
    if idade <= 9:
        print(f'Idade: {estilo["purpleBold"]}{idade}{estilo["clear"]}')
        print(f'Categoria: {estilo["purpleBold"]}MIRIM{estilo["clear"]}')
    elif 10 <= idade <= 14:
        print(f'Idade: {estilo["yellowBold"]}{idade}{estilo["clear"]}')
        print(f'Categoria: {estilo["yellowBold"]}INTANTIL{estilo["clear"]}')
    elif 15 <= idade <= 19:
        print(f'Idade: {estilo["blueBold"]}{idade}{estilo["clear"]}')
        print(f'Categoria: {estilo["blueBold"]}JUNIOR{estilo["clear"]}')
    elif 20 <= idade <= 25:
        print(f'Idade: {estilo["greenBold"]}{idade}{estilo["clear"]}')
        print(f'Categoria: {estilo["greenBold"]}SÊNIOR{estilo["clear"]}')
    elif idade > 25:
        print(f'Idade: {estilo["redBold"]}{idade}{estilo["clear"]}')
        print(f'Categoria: {estilo["redBold"]}MASTER{estilo["clear"]}')

print(f'{estilo["grey"]}*{estilo["clear"]}' * asteriscos)