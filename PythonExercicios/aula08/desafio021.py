# Faça um programa em Python que abra e reproduza um áudio de um arquivo mp3.

import pygame

# Iniciar o pygame
pygame.init()

# Carregar o arquivo
pygame.mixer.music.load('/home/rafaelsilva/Projetos/python-guanabara/PythonExercicios/aula08/x.mp3')

# Executar o arquivo
pygame.mixer.music.play()

input()

# Aguardar o fim da reprodução
pygame.event.wait()
