# Aula 12
# Desafio 036
# Escreva um programa para aprovar o empréstimo bancário para a compra e uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo ela não pode execeder 30% do salário ou então
# o empréstimo será negado.

estilo = {'limpa': '\033[m',
          'negrito': '\033[1m',
          'amarelo': '\033[33m',
          'amareloBold': '\033[1;33m',
          'azul': '\033[34m',
          'azulBold': '\033[1;34m',
          'cinza': '\033[37m',
          'cinzaBold': '\033[1;37m',
          'verde': '\033[32m',
          'verdeBold': '\033[1;32m',
          'vermelho': '\033[31m',
          'vermelhoBold': '\033[1;31m',
          'pretoebranco': '\033[7;30m'}

asteriscos = 60

print(f'{estilo["cinza"]}*{estilo["limpa"]}' * asteriscos)

valorImovel = float(input(f'{estilo["negrito"]}Valor do imóvel: {estilo["limpa"]}R$'))
salario = float(input(f'{estilo["negrito"]}Salário atual: {estilo["limpa"]}R$'))
anosParcelas = int(input(f'{estilo["negrito"]}Anos do financiamento: {estilo["limpa"]}'))

parcelas = anosParcelas * 12
percentualSalario = salario * 0.30
valorParcela = float(valorImovel / parcelas)

print(f'{estilo["cinza"]}*{estilo["limpa"]}' * asteriscos)

if valorParcela == percentualSalario:
    print(f'Salário atual: {estilo["negrito"]}R${salario:.2f}{estilo["negrito"]}')
    print(f'Valor de {estilo["azulBold"]}R${valorImovel:.2f}{estilo["limpa"]}')
    print(f'Prazo estimado de {estilo["negrito"]}{anosParcelas} anos{estilo["limpa"]}')
    print(f'Quantidade quantidade de parcelas: {estilo["negrito"]}{parcelas}{estilo["limpa"]}')
    print(f'Mensalidade: {estilo["amareloBold"]}R${valorParcela:.2f}{estilo["limpa"]}')
    print(f'Status Financiamento: {estilo["verdeBold"]}Aprovado{estilo["limpa"]}')
elif valorParcela < percentualSalario:
    print(f'Salário atual: {estilo["negrito"]}R${salario:.2f}{estilo["negrito"]}')
    print(f'Valor de {estilo["azulBold"]}R${valorImovel:.2f}{estilo["limpa"]}')
    print(f'Prazo estimado de {estilo["negrito"]}{anosParcelas} anos{estilo["limpa"]}')
    print(f'Quantidade quantidade de parcelas: {estilo["negrito"]}{parcelas}{estilo["limpa"]}')
    print(f'Mensalidade: {estilo["amareloBold"]}R${valorParcela:.2f}{estilo["limpa"]}')
    print(f'Status Financiamento: {estilo["verdeBold"]}Aprovado{estilo["limpa"]}')
else:
    print(f'Salário atual: {estilo["negrito"]}R${salario:.2f}{estilo["negrito"]}')
    print(f'Valor de {estilo["azulBold"]}R${valorImovel:.2f}{estilo["limpa"]}')
    print(f'Prazo estimado de {estilo["negrito"]}{anosParcelas} anos{estilo["limpa"]}')
    print(f'Quantidade quantidade de parcelas: {estilo["negrito"]}{parcelas}{estilo["limpa"]}')
    print(f'Mensalidade: {estilo["vermelhoBold"]}R${valorParcela:.2f}{estilo["limpa"]}')
    print(f'O valor da mensalidade execede {estilo["vermelhoBold"]}30% (R${percentualSalario:.2f}){estilo["limpa"]} do seu salário')
    print(f'Status Financiamento: {estilo["vermelhoBold"]}Reprovado{estilo["limpa"]}')

print(f'{estilo["cinza"]}*{estilo["limpa"]}' * asteriscos)