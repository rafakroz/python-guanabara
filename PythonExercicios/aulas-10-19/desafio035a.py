# Aula 10
# Desafio 035
# Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário
# se elas podem ou não formar um triângulo.

print('*' * 30)

r1 = float(input('Informa o comprimento da reta 1: '))
r2 = float(input('Informa o comprimento da reta 2: '))
r3 = float(input('Informa o comprimento da reta 3: '))

print('*' * 30)

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('É possível formar um triângulo!')
else:
    print('Não é possível formar um triângulo!')

print('*' * 30)