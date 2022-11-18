import pygame
import random
import time
import adereços

pygame.init()
pygameDisplay = pygame.display
pygameDisplay.set_caption("Jogo da Maça")
altura = 520
largura = 1000
tamanho = (largura, altura)
gameDisplay = pygame.display.set_mode(tamanho)
clock = pygame.time.Clock()
gameEvents = pygame.event
branco = (255,255,255)
fundo = pygame.image.load("adedeços/fundo.jpeg")
cesto = pygame.image.load("adedeços/cesto.png")
maça = pygame.image.load("adedeços/maça.png")




def escreverTexto (texto):
    fonte  = pygame.font.Font("freesansbold.ttf",15)
    textoDisplay = fonte.render(texto,True,branco)
    gameDisplay.blit(textoDisplay, (880,80))
    pygameDisplay.update()

def morreu():
    fonte  = pygame.font.Font("freesansbold.ttf",95)
    fonte2  = pygame.font.Font("freesansbold.ttf",45)
    textoDisplay = fonte.render("MORREUU !!!!",True,branco)
    textoDisplay2 = fonte2.render("press enter to continue !!!!",True,branco)
    gameDisplay.blit(textoDisplay, (150,150))
    gameDisplay.blit(textoDisplay2, (150,350))
    pygameDisplay.update()

def jogar():
    jogando = True
    cestoX = 500
    cestoY = 400
    movimentoCestoX = 0
    larguraCesto = 120
    alturaCesto = 110
    alturaMaça = 250
    larguraMaça = 50
    posicaoMaçaX = 400
    posicaoMaçaY = -240
    velocidadeMaça = 1
    pontos = 0
    pygame.mixer.music.load("assets/ironSound.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(-1)