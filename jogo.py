import pygame
import time
import random
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
fundo = pygame.image.load("assets/fundo.jpg")
cesto = pygame.image.load("assets/cesto.jpg")
maça = pygame.image.load("assets/maça.jpg")




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

    missileSound = pygame.mixer.Sound("assets/missile.wav")
    missileSound.set_volume(1)
    pygame.mixer.Sound.play(missileSound)

    explosaoSound = pygame.mixer.Sound("assets/explosao.wav")
    explosaoSound.set_volume(1)
    while True:
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movimentoCestoX = -15
                elif event.key == pygame.K_RIGHT:
                    movimentoCestoX = 15
                elif event.key == pygame.K_RETURN:
                    jogar()
            elif event.type == pygame.KEYUP:
                movimentoCestoX = 0
            
        if jogando:
            if posicaoMaçaY > altura:
                posicaoMaçaY = -240
                posicaoMaçaX = random.randint(0,largura)
                #velocidadeMissile = velocidadeMissile + 1
                pontos = pontos + 1
                pygame.mixer.Sound.play(missileSound)
            else:
                posicaoMaçaY =posicaoMaçaY + velocidadeMaça

            if cestoX + movimentoCestoX >0 and cestoX + movimentoCestoX< largura-larguraCesto:
                cestoX = cestoX + movimentoCestoX
            gameDisplay.fill(branco)
            gameDisplay.blit(fundo,(0,0))
            gameDisplay.blit(cesto, (cestoX,cestoY))
            
            gameDisplay.blit(maça, (posicaoMaçaX,posicaoMaçaY))
            escreverTexto("Pontos: "+str(pontos))

            pixelsXCesto = list(range(cestoX, cestoX+larguraCesto))
            pixelsY = list(range(cestoY, cestoY+alturaCesto))

            pixelXMaça = list(range(posicaoMaçaX, posicaoMaçaX+larguraMaça))
            pixelYMaça = list(range(posicaoMaçaY, posicaoMaçaY+alturaMaça))

            colisaoY = len(list(set(pixelYMaça) & set(pixelsYMaça) ))
            if colisaoY > 0:
                colisaoX = len(list(set(pixelXMaça) & set(pixelsXCesto) ))
                print(colisaoX)
                if colisaoX > 45:
                    morreu()
                    jogando=False
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(explosaoSound)


        pygameDisplay.update()
        clock.tick(60)

jogar()
