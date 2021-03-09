import pygame
from ndv import noveDaVelha
import desenhos as desenhos

def main():
    pygame.init()

    jogo = noveDaVelha()

    comprimento = 630
    altura = 630
    win = pygame.display.set_mode((comprimento,altura))
    pos = anterior = (-1, -1)
    jogada_valida = True

    cont = 0

    desenhos.desenha_linhas(win, comprimento, altura)

    run = True

    # loop inicial
    while run:

        pygame.time.delay(100)

        if pygame.mouse.get_pressed()[0] == 1:
            xy = pygame.mouse.get_pos()
            if jogada_valida:
                anterior = pos
                jogada_valida = False
            pos = desenhos.posicao(comprimento, altura, xy)
        
            if jogo.marcaTabuleiro(cont%2, pos, anterior):
                desenhos.desenha_linhas(win, comprimento, altura)
                if cont%2 == 0:
                    desenhos.o(win, comprimento, altura, pos, (0, 0, 255))
                else:
                    desenhos.x(win, comprimento, altura, pos, (255, 0, 0))

                cont += 1
                desenhos.destacaJogo(win, comprimento, altura, pos)
                jogada_valida = True

            for i in range(3):
                for j in range(3):
                    if jogo.tabuleiros[i][j].final() >= 0:
                        desenhos.encerraUnidade(win, comprimento, altura, (j, i),  jogo.tabuleiros[i][j].getVitoria())
                        jogo.marcaTabuleiroMaior((cont+1)%2, (j, i))
            
            if jogo.tabmaior.final() >= 0 or jogo.deuVelha():
                if jogo.deuVelha():
                    desenhos.encerraJdv(win, comprimento, altura, jogo.contaResultado())
                desenhos.encerraJdv(win, comprimento, altura, (cont+1)%2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        pygame.display.update()
    
main()