# Faça um algoritmo que leia o preço de um produto e
# mostre seu nome preço, com 5% de desconto

prod = 'iPhone 15'
valor = int(10000)
valorDesconto = int(valor - (valor * 0.05))

print(f'O valor do {prod} é R${valor} \nCom 5% de desconto fica R${valorDesconto}.')