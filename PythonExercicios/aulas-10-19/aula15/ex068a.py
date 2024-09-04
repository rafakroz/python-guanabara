# Aula 15
# Desafio 068
# Exercício 15.3
# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador
# PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

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

escolha = 0
escolhaConfirm = ''
vitoria = 0

while True:
    escolha = int(input(f'0 para PAR ou 1 para ÍMPAR: '))
    if escolha > 1:
        print(f'*' * asteriscos) # --------------------------------------
        print(f'Opção ({escolha}) inválida!')
    else:
        if escolha == 0:
            print(f'PAR!')
        else:
            print(f'ÍMPAR!')
        
        num = int(input(f'Qual o seu número [1 a 100]: '))
        
        if num > 100:
            num = int(input('Escolha um número até 100: '))
        
        numPc = randint(1,100)
        total = num + numPc
        
        if (total % 2 == 0):
            resultado = 0
            parImpar = 'PAR'
        else:
            resultado = 1
            parImpar = 'ÍMPAR'
        
        if escolha != resultado:
            print(f'*' * asteriscos) # --------------------------------------
            print(f'{cor["redBold"]}Você perdeu!{cor["clear"]}')
            print(f'Seu número: {num}')
            print(f'Número computador: {numPc}')
            print(f'Total de {total}, um número {cor["blueBold"]}{parImpar}{cor["clear"]}')
            print(f'Vitórias consecutivas: {vitoria}')
            print(f'*' * asteriscos) # --------------------------------------
            break
        else:
            print(f'*' * asteriscos) # --------------------------------------
            print(f'{cor["greenBold"]}Você ganhou!{cor["clear"]}')
            print(f'Seu número: {num}')
            print(f'Número computador: {numPc}')
            print(f'Total de {total}, um número {cor["blueBold"]}{parImpar}{cor["clear"]}')
            vitoria += 1
            print(f'Vitórias consecutivas: {vitoria}')
            print(f'*' * asteriscos) # --------------------------------------
