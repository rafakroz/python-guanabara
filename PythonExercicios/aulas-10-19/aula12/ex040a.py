# Aula 12
# Desafio 040
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma
# mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.1 a 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

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

aluno = str(input('Nome do aluno: ')).strip()
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))

media = (nota1 + nota2) / 2

print(f'{estilo["cinza"]}*{estilo["limpa"]}' * asteriscos)

print(f"""
======================================
= \033[7m        \033[1mFAIXAS DAS MÉDIAS         \033[m =
= {estilo["vermelhoBold"]}Média abaixo de 5.0:   REPROVADO{estilo["limpa"]}   =
= {estilo["amareloBold"]}Média entre 5.1 a 6.9: RECUPERAÇÃO{estilo["limpa"]} =
= {estilo["verdeBold"]}Média 7.0 ou superior: APROVADO{estilo["limpa"]}    =
======================================
""")

if media >= 7.0:
    print(f'{estilo["azulBold"]}Aluno: {aluno}{estilo["limpa"]}')
    print(f'Primeira nota: {nota1}')
    print(f'Segunda nota: {nota2}')
    print(f'Média: {media}')
    print(f'Status aluno: {estilo["verdeBold"]}Aprovado{estilo["limpa"]}')
elif media >= 5.1 and media <= 6.9:
    print(f'{estilo["azulBold"]}Aluno: {aluno}{estilo["limpa"]}')
    print(f'Primeira nota: {nota1}')
    print(f'Segunda nota: {nota2}')
    print(f'Média: {media}')
    print(f'Status aluno: {estilo["amareloBold"]}Recuperação{estilo["limpa"]}')
elif media <= 5.0:
    print(f'{estilo["azulBold"]}Aluno: {aluno}{estilo["limpa"]}')
    print(f'Primeira nota: {nota1}')
    print(f'Segunda nota: {nota2}')
    print(f'Média: {estilo["vermelhoBold"]}{media}{estilo["limpa"]}')
    print(f'Status aluno: {estilo["vermelhoBold"]}Reprovado{estilo["limpa"]}')

print(f'{estilo["cinza"]}*{estilo["limpa"]}' * asteriscos)