# Aula 13
# Desafio 055
# Exercício 13.10
# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi
# o maior e o menor peso lidos.

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

maior = 0
menor = 0
pMenor = 0
pMaior = 0

for pessoa in range(1, 6):
    peso = float(input(f'Informe o peso da {pessoa}° pessoa: '))
    
    if pessoa == 1:
        menor = peso
        pMenor += pessoa
        maior = peso
        pMaior = pessoa
    else:
        if peso < menor:
            menor = peso
            pMenor = pessoa
        if peso > maior:
            maior = peso
            pMaior = pessoa

print(f'O {pMaior}° peso informado, foi o {estilo["redBold"]}maior com {maior}kg{estilo["clear"]}.')
print(f'O {pMenor}° peso informado, foi o {estilo["greenBold"]}menor com {menor}kg{estilo["clear"]}.')