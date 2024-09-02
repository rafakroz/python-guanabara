# Aula 14
# Desafio 065
# Exercício 14.9
# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

asteriscos = 60

print(f'*' * asteriscos) # --------------------------------------

acao = 'S'

qtdNum = maior = menor = soma = media = 0 # Todos recebem valor 0
indice = 1

while acao in 'SS':
    num = int(input(f'{indice}) Insira um número: '))
    soma += num
    qtdNum += 1
    
    if qtdNum == 1:
        maior = menor = num # Ao iniciar, o número é tanto o maior, quanto menor
    else:
        if num > maior:
            maior = num # Maior número
        if num < menor:
            menor = num # Menor número

    acao = str(input(f'Continuar [s / n]? ')).strip().upper()[0]

print(f'*' * asteriscos) # --------------------------------------

media = soma / qtdNum

if qtdNum > 1:
    print(f'Foram digitados {qtdNum} números.')
    print(f'A soma deles é de {soma}.')
    print(f'A média é de {media}.')
    print(f'O maior número é {maior}.')
    print(f'O menor número é {menor}.')
else:
    print(f'Foi digitado apenas {qtdNum} número.')
    print(f'O seu valor é de {soma}.')
