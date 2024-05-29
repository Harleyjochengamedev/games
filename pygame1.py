#importado a biblioteca desenvolvida em c
import pygame as jogo

from pygame.locals import(K_UP,QUIT,K_DOWN)

#inicializamos o jogo
jogo.init()

#inicializamos a tela
primeira_tela = jogo.display.set_mode([500,500])

#controle da execução da tela
executando = True
while executando:
    for evento in jogo.event.get():
        if evento.type == jogo.QUIT:
            executando = False
        if evento.type == jogo.K_UP:
            jogo.draw.circle(primeira_tela,(255,0,0),(250,260),75)
        if evento.type == jogo.K_DOWN:
            jogo.draw.circle(primeira_tela,(255,0,0),(250,240),75)
    #desenha um circulo
    jogo.draw.circle(primeira_tela,(255,0,0),(250,250),75)
    jogo.display.flip()

jogo.quit()

