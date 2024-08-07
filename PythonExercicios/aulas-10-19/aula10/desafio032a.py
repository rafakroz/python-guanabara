# Aula 10
# Desafio 032
# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

print('*' * 30)

print('Informe o ano de interesse ou 0 para ano atual.')

ano = int(input('Digite o ano de interesse: '))

if ano == 0:
    ano = date.today().year

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano {ano} é Bissexto!')
else:
    print(f'O ano {ano} Não é Bissexto!')

print('*' * 30)