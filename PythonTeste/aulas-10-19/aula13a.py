asteriscos = 60

for c in range(1, 7):
    print(c)
print('Fim')


print(f'*' * asteriscos) # --------------------------------------


i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c)
print('Fim')


print(f'*' * asteriscos) # --------------------------------------


soma = 0

for c in range(0, 4):

    n = int(input(f'{c + 1}) Digite um valor: '))
    
    soma += n

print(f'O somatório de todos os valores foi {soma}.')
