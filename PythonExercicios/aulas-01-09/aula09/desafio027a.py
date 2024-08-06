# Desafio 027
# Faça um programa que leia o nome de uma pessoa, mostrando em seguida
# o primeiro e o último nome separadamente.
# Exemplo: Ana Maria de Souza
# primeiro: Ana
# segundo: Souza

nome = str(input('Digite seu nome completo: ')).strip()

nomeDividido = nome.split()

print(f'Nome completo: {nome}')
print(f'Primeiro nome: {nomeDividido[0]}')
print(f'Último nome: {nomeDividido[-1]}')
# print(f'Último nome: {nomeDividido[len(nomeDividido)-1]}')

# [-1] indica o último item de uma lista (neste caso, nome dividido)
