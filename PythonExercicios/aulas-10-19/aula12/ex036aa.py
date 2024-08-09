# Aula 12
# Desafio 036
# Escreva um programa para aprovar o empréstimo bancário para a compra e uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo ela não pode execeder 30% do salário ou então
# o empréstimo será negado.

asteriscos = 60

print('*' * asteriscos)

valorImovel = float(input('Valor do imóvel: R$'))
salario = float(input('Salário atual: R$'))
anosParcelas = int(input('Anos do financiamento: '))

parcelas = anosParcelas * 12
percentualSalario = salario * 0.30
valorParcela = float(valorImovel / parcelas)

print('*' * asteriscos)

if valorParcela == percentualSalario:
    print(f'Salário atual: R${salario:.2f}')
    print(f'Valor de R${valorImovel:.2f}')
    print(f'Prazo estimado de {anosParcelas} anos')
    print(f'Quantidade quantidade de parcelas: {parcelas}')
    print(f'Mensalidade: R${valorParcela:.2f}')
    print(f'Status Financiamento: Aprovado')
elif valorParcela < percentualSalario:
    print(f'Salário atual: R${salario:.2f}')
    print(f'Valor de R${valorImovel:.2f}')
    print(f'Prazo estimado de {anosParcelas} anos')
    print(f'Quantidade quantidade de parcelas: {parcelas}')
    print(f'Mensalidade: R${valorParcela:.2f}')
    print(f'Status Financiamento: Aprovado')
else:
    print(f'Salário atual: R${salario:.2f}')
    print(f'Valor de R${valorImovel:.2f}')
    print(f'Prazo estimado de {anosParcelas} anos')
    print(f'Quantidade quantidade de parcelas: {parcelas}')
    print(f'Mensalidade: R${valorParcela:.2f}')
    print(f'O valor da mensalidade execede 30% (R${percentualSalario:.2f}) do seu salário')
    print(f'Status Financiamento: Reprovado')

print('*' * asteriscos)