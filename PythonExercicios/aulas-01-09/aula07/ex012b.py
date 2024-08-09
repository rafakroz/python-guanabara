# Faça um algoritmo que leia o preço de um produto e
# mostre seu nome preço, com 5% de desconto

produto = input('Qual o nome do produto? ')

preco = float(input('Qual o valor? '))

print(f'O produto {produto} custa R${preco:.2f}.')

desconto = float(input('Qual o percentual de desconto? '))

novoValor = preco - (preco * desconto / 100)

print(f'Foi concedido o desconto de {desconto:.2f}% \nO valor final é R${novoValor:.2f}.')