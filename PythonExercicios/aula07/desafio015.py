# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por Km rodada

precoDia = float(60)
precoKm = float(0.15)

diasAlugado = int(input('Por quantos dias alugou? '))
kmRodados = float(input('Rodou quantos Km? '))

totalDias = precoDia * diasAlugado
totalKm = precoKm * kmRodados

totalFinal = totalDias + totalKm

print(f'Você usou o automóvel por {diasAlugado}.')
print(f'Rodou o total de {kmRodados}km.')
print(f'O valor total é R${totalFinal:.2f}.')

'''
precoDia = 60
precoKm = 0.15

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))

valorFinal = (precoDia * dias) + (precoKm * km)

print(f'O total a pagar é de R${valorFinal:.2f}.')'''