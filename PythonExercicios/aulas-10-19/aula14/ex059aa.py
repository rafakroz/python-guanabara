# Aula 14
# Desafio 059
# Exercício 14.3
# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] soma
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

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

num1 = int(input('Insira o primeiro número: '))
num2 = int(input('Insira o segundo número: '))

acao = 0

print(f'*' * asteriscos) # --------------------------------------

while acao != 5:    
    print('''Selecione uma ação:
          
    [1] Somar os números
    [2] Multiplicar os números
    [3] Exibir o maior número
    [4] Inserir novos números
    [5] Sair
    ''')
    
    print(f'*' * asteriscos) # --------------------------------------
    
    print(f'Números inseridos: {num1} e {num2}.')
    
    acao = int(input(f'{estilo["blueBold"]}Digite a ação: {estilo["clear"]}'))
    
    if acao == 1:
        soma = num1 + num2
        print(f'A soma entre {num1} e {num2} é {soma}.')
        print(f'*' * asteriscos) # --------------------------------------
        sleep(3)
        
    elif acao == 2:
        multi = num1 * num2
        print(f'A multiplicação entre {num1} e {num2} é {multi}.')
        print(f'*' * asteriscos) # --------------------------------------
        sleep(3)
        
    elif acao == 3:
        if num1 > num2:
            print(f'O primeiro número ({num1}) é maior que o segundo número ({num2}).')
            print(f'*' * asteriscos) # --------------------------------------
            sleep(3)
        else:
            print(f'O segundo número ({num2}) é maior que o primero número ({num1})10.')
            print(f'*' * asteriscos) # --------------------------------------
            sleep(3)
            
    elif acao == 4:
        print(f'Números selecionados anteriormente: {num1} e {num2}')
        print(f'Insira novos números.')
        num1 = int(input('Primeiro número: '))
        num2 = int(input('Segundo número: '))
        print(f'*' * asteriscos) # --------------------------------------
        
    elif acao not in (1, 2, 3, 4, 5):
        print(f'{estilo["redBold"]}Ação inválida!{estilo["clear"]}')
        print(f'*' * asteriscos) # --------------------------------------
        sleep(3)

print(f'Programa finalizado!')
sleep(2)
print(f'Até breve!')


print(f'*' * asteriscos) # --------------------------------------