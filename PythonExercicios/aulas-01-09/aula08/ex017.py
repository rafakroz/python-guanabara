# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa
'''
a = float(input('Informe a comprimento do cateto oposto: '))
b = float(input('Informe a comprimento do cateto adjacente: '))
h = ((a ** 2) + (b ** 2)) ** (1/2)

print(f'O comprimento da hipotenusa é {h:.2f}')

print('-' * 25)'''

# import math
from math import hypot

a = float(input('Informe a comprimento do cateto oposto: '))
b = float(input('Informe a comprimento do cateto adjacente: '))
h = hypot(a, b)

print(f'O comprimento da hipotenusa é {h:.2f}')