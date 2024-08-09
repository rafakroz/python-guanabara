# Aula 12
# Desafio 037
# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

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

numInt = int(input(f'Insira um número {estilo["verdeBold"]}inteiro{estilo["limpa"]}: '))

print(f"""Selecione uma base de conversão
{estilo["azulBold"]}1:{estilo["limpa"]} {estilo["negrito"]}Binária{estilo["limpa"]}
{estilo["azulBold"]}2:{estilo["limpa"]} {estilo["negrito"]}Octal{estilo["limpa"]}
{estilo["azulBold"]}3:{estilo["limpa"]} {estilo["negrito"]}Hexadecimal{estilo["limpa"]}
{estilo["azulBold"]}4:{estilo["limpa"]} {estilo["negrito"]}Todos{estilo["limpa"]}""")

print(f'{estilo["cinza"]}*{estilo["limpa"]}' * asteriscos)

tipo = int(input(f'Digite o {estilo["azulBold"]}tipo{estilo["limpa"]} de conversão: '))

print(f'{estilo["cinza"]}*{estilo["limpa"]}' * asteriscos)

if tipo == 1:
    print(f'Número Inteiro: {numInt}')
    print('Binária:', bin(numInt)[2:])
elif tipo == 2:
    print(f'Número Inteiro: {numInt}')
    print('Octal:', oct(numInt)[2:])
elif tipo == 3:
    print(f'Número Inteiro: {numInt}')
    print('Hexadecimal:', hex(numInt)[2:])
elif tipo == 4:
    print(f'Número Inteiro: {numInt}')
    print('Binária:', bin(numInt)[2:])
    print('Octal:', oct(numInt)[2:])
    print('Hexadecimal:', hex(numInt)[2:])
else:
    print(f'{estilo["vermelhoBold"]}Tipo inválido! Tente novamente!{estilo["limpa"]}')