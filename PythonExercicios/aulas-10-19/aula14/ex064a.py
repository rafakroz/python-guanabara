# Aula 14
# Desafio 064
# Exercício 14.8
# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

asteriscos = 60

print(f'*' * asteriscos) # --------------------------------------

num = 0
qtdNums = 0
soma = 0
flag = 999

while num != flag:
    num = int(input(f'Insira um número: '))

    if num == 999:
        soma = soma
    else:
        soma += num
        qtdNums += 1

print(f'*' * asteriscos) # --------------------------------------

if qtdNums == 1:
    print(f'Foi digitado apenas {qtdNums} número.')
    print(f'E seu valor é {soma}.')
else:
    print(f'Foram digitados {qtdNums} números.')
    print(f'A soma de todos os números é de {soma}.')