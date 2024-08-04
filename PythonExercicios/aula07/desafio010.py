# Crie um programa que leia quanto dinheiro uma tem na carteira e
# mostre quantos dólares ela pode comprar
# Considerar: USS 1 = R$ 3,27

money = int(input('Informe o valor da carteira: '))

dolar = 3.27
cambio = money / dolar

print(f'R${money}, no cotação de US${dolar}, equivale a US${cambio}.')
