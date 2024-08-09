# Aula 13
# Desafio 049
# Exercício 13.4
# Refaça o Desafio 009 / ex009, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

asteriscos = 60

print(f'*' * asteriscos)

num = int(input('Tabuada de: '))

print(f'*' * asteriscos)

for i in range(1, 11):
    print(f'{num} x {i:2} = {num * i}')

print(f'*' * asteriscos)