# Faça um programa que leia um número inteiro e mostre ne tela
# seu sucessor e seu antecessor

num = int(input('Digite um número: '))

anterior = num - 1
proximo = num + 1

print(f'O número anterior a {num} é: {anterior}')
print(f'O número sucessor a {num} é: {proximo}')