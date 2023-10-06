from PPlay.window import *
from PPlay.sprite import *
from PPlay.keyboard import *
import time

jogador_1 = 0
jogador_2 = 0

# Cria uma janela
janela = Window(800, 600)
janela.set_title("Pedro Vargas")

# Integrando o teclado ao programa
teclado = Window.get_keyboard()

# Criação dos Pads E (esquerda) e D (direita)
padE = Sprite("padE.png")
padD = Sprite("padD.png")

# Posicionamento dos Pads
padE.x = 7
padE.y = janela.height / 2 - padE.height / 2

padD.x = janela.width - padD.width - 7
padD.y = janela.height / 2 - padD.height / 2

velP = 300

# Cria uma bolinha de 40x40 pixels no centro da tela
bolinha = Sprite("bolinha.png")

# Define a velocidade da bolinha
vel_x = 0  # Inicialmente, a bolinha não se move horizontalmente
vel_y = 0  # Inicialmente, a bolinha não se move verticalmente

# Centraliza a bola inicialmente
bolinha.x = janela.width / 2 - bolinha.width / 2
bolinha.y = janela.height / 2 - bolinha.height / 2

# Controle de tempo para a bolinha esperar no meio
tempo_espera = 1.5  # 2 segundos
tempo_inicial = time.time()
esperando = True

while True:
    # Define a cor de fundo como roxo espacial (26, 4, 60)
    janela.set_background_color((26, 4, 60))

    # Verifica se a bolinha está esperando no meio
    if esperando:
        if time.time() - tempo_inicial >= tempo_espera:
            esperando = False
            vel_x = 500  # Inicia o movimento horizontal
            vel_y = 250  # Inicia o movimento vertical

    # Adiciona o movimento da bolinha ao loop
    bolinha.x += vel_x * janela.delta_time()
    bolinha.y += vel_y * janela.delta_time()

    # Restringe o movimento dos Pads
    if teclado.key_pressed("W") and padE.y > 0:  # Move o Pad esquerdo para cima
        padE.y -= velP * janela.delta_time()
    if teclado.key_pressed("S") and padE.y + padE.height < janela.height:  # Move o Pad esquerdo para baixo
        padE.y += velP * janela.delta_time()
    if teclado.key_pressed("UP") and padD.y > 0:  # Move o Pad direito para cima
        padD.y -= velP * janela.delta_time()
    if teclado.key_pressed("DOWN") and padD.y + padD.height < janela.height:  # Move o Pad direito para baixo
        padD.y += velP * janela.delta_time()

    # Verifica se a bolinha saiu da tela e depois joga ela no meio
    if (bolinha.x + bolinha.width >= janela.width):
        jogador_1 += 1
        vel_x = 0  # Para a bolinha horizontalmente
        vel_y = 0  # Para a bolinha verticalmente
        bolinha.x = janela.width / 2 - bolinha.width / 2
        bolinha.y = janela.height / 2 - bolinha.height / 2
        esperando = True
        tempo_inicial = time.time()
    if (bolinha.x <= 0):
        jogador_2 += 1
        vel_x = 0  # Para a bolinha horizontalmente
        vel_y = 0  # Para a bolinha verticalmente
        bolinha.x = janela.width / 2 - bolinha.width / 2
        bolinha.y = janela.height / 2 - bolinha.height / 2
        esperando = True
        tempo_inicial = time.time()

    # Verifica se a bolinha bateu nas bordas da tela
    if (bolinha.y <= 0):
        vel_y *= -1
        bolinha.y = 0
    if (bolinha.y + bolinha.height >= janela.height):
        vel_y *= -1
        bolinha.y = janela.height - bolinha.height

    # Verifica se a bolinha colide com os Pads
    if (
        bolinha.x < padE.x + padE.width and
        bolinha.x + bolinha.width > padE.x and
        bolinha.y < padE.y + padE.height and
        bolinha.y + bolinha.height > padE.y
    ):
        vel_x *= -1
        bolinha.x = padE.x + padE.width

    if (
        bolinha.x < padD.x + padD.width and
        bolinha.x + bolinha.width > padD.x and
        bolinha.y < padD.y + padD.height and
        bolinha.y + bolinha.height > padD.y
    ):
        vel_x *= -1
        bolinha.x = padD.x - bolinha.width

    janela.draw_text("{} jogador 1 x {} jogador 2".format(jogador_1,jogador_2), janela.width / 2 - 100 , 30, 20, (255, 255, 255), "Arial", True, False)

    padE.draw()
    padD.draw()
    bolinha.draw()

    janela.update()

    if janela.get_keyboard().key_pressed("ESC"):
        break

janela.close()