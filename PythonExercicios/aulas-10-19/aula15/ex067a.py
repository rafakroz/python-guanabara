# Aula 15
# Desafio 067
# Exercício 15.2
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

estilo = {'clear':        '\033[m',
          'bold':      '\033[1m',
          'blue':         '\033[34m',
          'blueBold':     '\033[1;34m',
          'cyan':         '\033[36m',
          'cyanBold':     '\033[1;36m',
          'green':        '\033[32m',
          'greenBold':    '\033[1;32m',
          'grey':        '\033[37m',
          'greyBold':    '\033[1;37m',
          'purple':     '\033[35m',
          'purpleBold': '\033[1;35m',
          'red':     '\033[31m',
          'redBold': '\033[1;31m',
          'yellow':      '\033[33m',
          'yellowBold':  '\033[1;33m',
          'blackWhite': '\033[7;30m'}

asteriscos = 60

print(f'*' * asteriscos) # --------------------------------------

print('--- Tabuada ---')

num = int(input('Tabuada de: '))

while True:
    for i in range(1, 11):
        print(f'{num} x {i:2} = {num * i:2}')
    
    print(f'*' * asteriscos) # --------------------------------------
    num = int(input(f'Digite um número negativo para sair ou outro número: '))
    print(f'*' * asteriscos) # --------------------------------------
    
    if num < 0:
        break
    else:
        print(f'Tabuada de: {num}')

print('Programa finalizado. Até a próxima!')

print(f'*' * asteriscos) # --------------------------------------