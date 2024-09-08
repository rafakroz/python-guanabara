# Aula 15
# Desafio 071
# Exercício 15.6
# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será
# o valor sacado (int) e o programa vai informar quantas cédulas de cada valor serão entregues.
# Obs.: considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.

cor = {'clear':      '\033[m',
       'bold':       '\033[1m',
       'blue':       '\033[34m',
       'blueBold':   '\033[1;34m',
       'cyan':       '\033[36m',
       'cyanBold':   '\033[1;36m',
       'green':      '\033[32m',
       'greenBold':  '\033[1;32m',
       'grey':       '\033[37m',
       'greyBold':   '\033[1;37m',
       'purple':     '\033[35m',
       'purpleBold': '\033[1;35m',
       'red':        '\033[31m',
       'redBold':    '\033[1;31m',
       'yellow':     '\033[33m',
       'yellowBold': '\033[1;33m',
       'blackWhite': '\033[7;30m'}

asteriscos = 60

print(f'*' * asteriscos) # --------------------------------------

print('---- CAIXA ELETRÔNICO ----')
valor = int(input('Valor a sacar: '))
total = valor
cedula = 100
qtdCedula = 0

while True:
    if total >= cedula:
        total -= cedula
        qtdCedula += 1
    else:
        if qtdCedula > 0:
            if qtdCedula == 1:
                print(f'{qtdCedula} cédula de R${cedula:.2f}.')
            else:
                print(f'{qtdCedula} cédulas de R${cedula:.2f}.')
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        elif cedula == 2:
            cedula = 1
        qtdCedula = 0
        if total == 0:
            break



print(f'*' * asteriscos) # --------------------------------------
