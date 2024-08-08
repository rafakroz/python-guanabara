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

estilo = {'limpa':        '\033[m',
          'negrito':      '\033[1m',
          'amarelo':      '\033[33m',
          'amareloBold':  '\033[1;33m',
          'azul':         '\033[34m',
          'azulBold':     '\033[1;34m',
          'cinza':        '\033[37m',
          'cinzaBold':    '\033[1;37m',
          'roxo':     '\033[35m',
          'roxoBold': '\033[1;35m',
          'verde':        '\033[32m',
          'verdeBold':    '\033[1;32m',
          'vermelho':     '\033[31m',
          'vermelhoBold': '\033[1;31m',
          'pretoebranco': '\033[7;30m'}

asteriscos = 60

print(f'{estilo["cinza"]}*{estilo["limpa"]}' * asteriscos)

nome = str(input('Nome do aluno: ')).strip()
anoNasc = int(input('Ano de nascimento: '))

anoAtual = date.today().year
# anoAtual = 2017 ano aula
idade = anoAtual - anoNasc

print(f'''
===========================
= \033[7m     \033[1mFAIXAS ETÁRIAS    \033[m =
=  {estilo["roxoBold"]}Até 9 anos: MIRIM{estilo["limpa"]}      =
=  {estilo["amareloBold"]}Até 14 anos: INFANTIL{estilo["limpa"]}  =
=  {estilo["azulBold"]}Até 19 anos: JUNIOR{estilo["limpa"]}    =
=  {estilo["verdeBold"]}Até 20 anos: SÊNIOR{estilo["limpa"]}    =
=  {estilo["vermelhoBold"]}Acima: MASTER{estilo["limpa"]}          =
===========================
''')

print(f'{estilo["cinza"]}*{estilo["limpa"]}' * asteriscos)

print(f'{estilo["azulBold"]}Aluno: {nome}{estilo["limpa"]}')
print(f'Ano de Nascimento: {anoNasc}')

if anoNasc > anoAtual:
    print(f'{estilo["vermelhoBold"]}Erro! Insira um abaixo do atual!{estilo["limpa"]}')
else:
    if idade <= 9:
        print(f'Idade: {estilo["roxoBold"]}{idade}{estilo["limpa"]}')
        print(f'Categoria: {estilo["roxoBold"]}MIRIM{estilo["limpa"]}')
    elif 10 <= idade <= 14:
        print(f'Idade: {estilo["amareloBold"]}{idade}{estilo["limpa"]}')
        print(f'Categoria: {estilo["amareloBold"]}INTANTIL{estilo["limpa"]}')
    elif 15 <= idade <= 19:
        print(f'Idade: {estilo["azulBold"]}{idade}{estilo["limpa"]}')
        print(f'Categoria: {estilo["azulBold"]}JUNIOR{estilo["limpa"]}')
    elif 20 <= idade <= 25:
        print(f'Idade: {estilo["verdeBold"]}{idade}{estilo["limpa"]}')
        print(f'Categoria: {estilo["verdeBold"]}SÊNIOR{estilo["limpa"]}')
    elif idade > 25:
        print(f'Idade: {estilo["vermelhoBold"]}{idade}{estilo["limpa"]}')
        print(f'Categoria: {estilo["vermelhoBold"]}MASTER{estilo["limpa"]}')

print(f'{estilo["cinza"]}*{estilo["limpa"]}' * asteriscos)