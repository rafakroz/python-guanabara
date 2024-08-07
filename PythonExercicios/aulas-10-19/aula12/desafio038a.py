# Aula 12
# Desafio 038
# Escreva um programa que leia dois números inteiros e compare-os, mostrando na uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

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

num1 = int(input(f'Primeiro número: '))
num2 = int(input(f'Segundo número: '))

print(f'{estilo["cinza"]}*{estilo["limpa"]}' * asteriscos)

if num1 > num2:
    print(f'Primeiro número: {estilo["azulBold"]}{num1}{estilo["limpa"]}')
    print(f'Segundo número: {estilo["verdeBold"]}{num2}{estilo["limpa"]}')
    print(f'O {estilo["azulBold"]}primero número ({num1}){estilo["limpa"]} é maior que o {estilo["verdeBold"]}segundo número ({num2}){estilo["limpa"]}.')
elif num2 > num1:
    print(f'Primeiro número: {estilo["azulBold"]}{num1}{estilo["limpa"]}')
    print(f'Segundo número: {estilo["verdeBold"]}{num2}{estilo["limpa"]}')
    print(f'O {estilo["verdeBold"]}segundo número ({num2}){estilo["limpa"]} é maior que o {estilo["azulBold"]}primeiro número ({num1}){estilo["limpa"]}.')
else:
    print(f'Primeiro número: {estilo["amareloBold"]}{num1}{estilo["limpa"]}')
    print(f'Segundo número: {estilo["amareloBold"]}{num2}{estilo["limpa"]}')
    print(f'{estilo["amareloBold"]}Os dois números são iguais!{estilo["limpa"]}')