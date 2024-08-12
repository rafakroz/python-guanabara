# Aula 13
# Desafio 054
# Exercício 13.9
# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas ainda não atingiram a maioridade [21 anos] e quantas já são maiores.

from datetime import date

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

anoAtual = date.today().year
menores = 0
adultos = 0

for i in range(1, 8):

    ano = int(input(f'{i}° Ano de nascimento: '))
    idade = anoAtual - ano
    print(f'Idade: {idade}')
    
    if idade < 18:
        menores += 1
    elif idade >= 18:
        adultos += 1

print(f'*' * asteriscos) # --------------------------------------

print(f'Qtd. {estilo["redBold"]}menores{estilo["clear"]} de idade: {menores}')
print(f'Qtd. {estilo["greenBold"]}maiores{estilo["clear"]} de idade: {adultos}')
