#faça um programa que abrar e reproduza um áudio de um arquivo mp3
import pygame

# Inicializa o pygame
pygame.init()

# Carrega o arquivo de áudio
audio_file = "caminho_do_arquivo.mp3"  # Substitua pelo caminho do seu arquivo MP3
pygame.mixer.music.load(audio_file)

# Reproduz o áudio
pygame.mixer.music.play()

# Aguarda o áudio terminar de tocar
while pygame.mixer.music.get_busy():
    continue

# Encerra o pygame
pygame.quit()
