from PPlay.window import *
from PPlay.sprite import Sprite

# Cria uma janela
janela = Window(800, 600)
janela.set_title("Pedro Vargas")

# Define a cor de fundo como branco (255, 255, 255)
janela.set_background_color((0, 0, 0))

while True:
    # Loop do jogo aqui

    # Cria uma bolinha de 40x40 pixels no centro da tela
    bolinha = Sprite("bolinha.png")
    bolinha.x = janela.width / 2 - bolinha.width / 2
    bolinha.y = janela.height / 2 - bolinha.height / 2

    # Desenha a bolinha na tela
    bolinha.draw()

    janela.update()

    if janela.get_keyboard().key_pressed("ESC"):
        break

janela.close()

