# Aula 16
# Desafio 072
# Exercício 16.1
# Crie um programa que tenha uma tupla preenchida com uma contagem por extensão, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extensão.

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

lista = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 
         'seis', 'sete', 'oito', 'nove', 'dez', 
         'onze', 'doze', 'treze', 'catorze', 'quinze', 
         'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    while num < 0 or num > 20:
        num = int(input('Valor inválido! Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {num} ({lista[num]}).')
    print(f'*' * asteriscos) # --------------------------------------
    
    escolha = ' '
    
    while escolha not in 'NS':
        escolha = str(input(f'Quer continuar [S / N]? ')).strip().upper()[0]
        print(f'*' * asteriscos) # --------------------------------------
    
    if escolha == 'N':
        break
print('Programa finalizado!')

print(f'*' * asteriscos) # --------------------------------------
