# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua posição inteira
# Exemplo: Digite um número 6.127
# O número 6.127 tem a parte inteira 6.
'''
from math import trunc

numero = float(input('Digite um número: '))

print(f'O número digitado foi {numero} e sua parte inteira é {trunc(numero)}.')'''

numero = float(input('Digite um número: '))

# Convertendo float para int
print(f'O número digitado foi {numero} e sua parte inteira é {int(numero)}.')

print('-' * 20)

