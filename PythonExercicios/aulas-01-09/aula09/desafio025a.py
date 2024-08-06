# Desafio 025
# Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome.

nome = str(input('Digite o seu nome: ')).strip()

nomeBuscado = str('Silva').upper()

print(f'O nome contém {nomeBuscado}? {nomeBuscado in nome.upper()}')