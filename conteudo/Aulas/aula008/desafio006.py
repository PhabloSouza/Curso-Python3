'''Faça um programa em python que abra e reproduza o audio de um arquivo MP3'''

'''Passo 1 - '''

import pygame
pygame.init()
pygame.mixer.music.load('desafio006.mp3')
pygame.mixer.music.play()
pygame.event.wait()