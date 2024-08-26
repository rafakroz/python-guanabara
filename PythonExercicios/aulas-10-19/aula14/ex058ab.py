
# Aula 14
# Desafio 058
# Exercício 14.2
# Melhore o jogo do Desafio 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vair tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.

from random import randint
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

print('Tente acertar em que número pensei entre 0 e 10!')

print(f'*' * asteriscos) # --------------------------------------

numPc = randint(0, 10)
tentativas = 1

indiceTentativas = {
    1: 'primeira',
    2: 'segunda',
    3: 'terceira',
    4: 'quarta',
    5: 'quinta',
    6: 'sexta',
    7: 'sétima',
    8: 'oitava',
    9: 'nona',
    10: 'décima'
}

meuNum = int(input('Digite seu número: '))

while meuNum != numPc:
    print('Processando.')
    sleep(0.5)
    print('Processando..')
    sleep(0.5)
    print('Processando...')
    sleep(0.5)
    print(f'{estilo["redBold"]}Você errou!{estilo["clear"]}')
    if meuNum < numPc:
        print(f'Seu número é menor que o meu!')
        print(f'*' * asteriscos) # --------------------------------------
        meuNum = int(input('Tente novamente! Escolhar outro número: '))
    elif meuNum > numPc:
        print(f'Seu número é maior que o meu!')
        print(f'*' * asteriscos) # --------------------------------------
        meuNum = int(input('Tente novamente! Escolhar outro número: '))
    tentativas += 1

print('Processando.')
sleep(0.5)
print('Processando..')
sleep(0.5)
print('Processando...')
sleep(0.5)

print(f'*' * asteriscos) # --------------------------------------

print(f'{estilo["greenBold"]}Você escolheu {meuNum} e acertou na {indiceTentativas[tentativas]} tentativa!{estilo["clear"]}')

print(f'*' * asteriscos) # --------------------------------------