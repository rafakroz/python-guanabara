# Crie um algoritmo que leia um número e mostre
# o seu dobro, triplo e raiz quadrada.

'''
num = int(input('Digite um número: '))

dobro = num * 2
triplo = num * 3
raiz = num ** 0.5

print(f'O dobro de {num} é: {dobro}')
print(f'O triplo de {num} é: {triplo}')
print(f'A raiz quadrada de {num} é: {raiz}')
'''

num = int(input('Digite um número: '))
print(f'O dobro de {num} é {num * 2}')
print(f'O triplo de {num} é {num * 3}')
#print(f'A raiz quadrada de {num} é {num ** (1/2):.2f}')
print(f'A raiz quadrada de {num} é {pow(num, (1/2)):.2f}')
