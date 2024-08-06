# Faça um programa que leia um ângulo qualquer e mostre na tela
# o valor do seno, cosseno e tangente desse ângulo

# import math
from math import radians, sin, cos, tan

a = float(input('Informe o ângulo: '))

'''
math.cos(x)
Retorna o cosseno de x radianos.

math.sin(x)
Retorna o seno de x radianos.

math.tan(x)
Retorna o tangente de x radianos.
'''

# seno = math.sin(math.radians(a))
# cosseno = math.cos(math.radians(a))
# tangente = math.tan(math.radians(a))

#Convertendo a para radiano

seno = sin(radians(a))
cosseno = cos(radians(a))
tangente = tan(radians(a))

print(f'O ângulo de {a:.1f} tem o SENO de {seno:.2f}')
print(f'O ângulo de {a:.1f} tem o COSSENO de {cosseno:.2f}')
print(f'O ângulo de {a:.1f} tem o TANGENTE de {tangente:.2f}')
