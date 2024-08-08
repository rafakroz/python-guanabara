# Aula 12
# Desafio 039
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# Se ele ainda se vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se já passou do tempo de alistamento
# >> O programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

estilo = {'limpa': '\033[m',
          'negrito': '\033[1m',
          'amarelo': '\033[33m',
          'amareloBold': '\033[1;33m',
          'azul': '\033[34m',
          'azulBold': '\033[1;34m',
          'cinza': '\033[37m',
          'cinzaBold': '\033[1;37m',
          'verde': '\033[32m',
          'verdeBold': '\033[1;32m',
          'vermelho': '\033[31m',
          'vermelhoBold': '\033[1;31m',
          'pretoebranco': '\033[7;30m'}

asteriscos = 60

print(f'{estilo["cinza"]}*{estilo["limpa"]}' * asteriscos)

nome = str(input('Informe o seu nome: ')).strip()
anoNasc = int(input('Informe o seu ano de nascimento: '))

anoAtual = date.today().year
idade = anoAtual - anoNasc 
tempoPendente = 18 - idade

print(f'{estilo["cinza"]}*{estilo["limpa"]}' * asteriscos)

if idade < 18:
    anoExato = anoAtual + tempoPendente
    print(f'{estilo["verdeBold"]}{nome} você ainda não precisa se alistar!{estilo["limpa"]}')
    print(f'Você tem {estilo["verdeBold"]}{idade} anos{estilo["limpa"]}. Ainda faltam {tempoPendente} anos!')
    print(f'Ainda faltam {tempoPendente} anos! Você deve se alistar em {estilo["verdeBold"]}{anoExato}{estilo["limpa"]}.')
elif idade == 18:
    print(f'{estilo["negrito"]}{nome}{estilo["limpa"]} você tem {estilo["amareloBold"]}{idade} anos{estilo["limpa"]}.')
    print(f'{estilo["amareloBold"]}Já pode se alistar!{estilo["limpa"]}')
else:
    excedente = idade - 18
    anoExato = anoAtual - excedente
    print(f'{estilo["negrito"]}{nome}{estilo["limpa"]} você tem {estilo["vermelhoBold"]}{idade} anos{estilo["limpa"]}.')
    print(f'{estilo["vermelhoBold"]}O prazo para alistar expirou!{estilo["limpa"]}')
    print(f'Se passaram {excedente} anos. Você deveria ter se alista no ano de {estilo["vermelhoBold"]}{anoExato}{estilo["limpa"]}.')

print(f'{estilo["cinza"]}*{estilo["limpa"]}' * asteriscos)