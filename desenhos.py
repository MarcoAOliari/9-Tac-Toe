import pygame
# import draw (comentario teste)

def desenhaJogoIndividual(win, cini, cfim, aini, afim, cor):
    pygame.draw.line(win, cor, (cini + int((cfim - cini)/3), aini), (cini + int((cfim - cini)/3), afim), 2)
    pygame.draw.line(win, cor, (cini + 2*int((cfim - cini)/3), aini), (cini + 2*int((cfim - cini)/3), afim), 2)
    pygame.draw.line(win, cor, (cini, aini + int((afim - aini)/3)), (cfim, aini + int((afim - aini)/3)), 2)
    pygame.draw.line(win, cor, (cini, aini + 2*int((afim - aini)/3)), (cfim, aini + 2*int((afim - aini)/3)), 2)

def linhasPrincipais(win, comprimento, altura):
    pygame.draw.line(win, (255, 255, 255), (comprimento/3, 0), (comprimento/3, altura), 5)
    pygame.draw.line(win, (255, 255, 255), (2*comprimento/3, 0), (2*comprimento/3, altura), 5)
    pygame.draw.line(win, (255, 255, 255), (0, altura/3), (comprimento, altura/3), 5)
    pygame.draw.line(win, (255, 255, 255), (0, 2*altura/3), (comprimento, 2*altura/3), 5)

def x(win, comprimento, altura, coeficientes, cor):
    pygame.draw.line(win, cor, (coeficientes[0]*comprimento/9, coeficientes[1]*altura/9), ((coeficientes[0]+1)*comprimento/9, (coeficientes[1]+1)*altura/9), 3)
    pygame.draw.line(win, cor, (coeficientes[0]*comprimento/9, (coeficientes[1]+1)*altura/9), ((coeficientes[0]+1)*comprimento/9, coeficientes[1]*altura/9), 3)

def o(win, comprimento, altura, coeficientes, cor):
    pygame.draw.circle(win, cor, (int((1+2*coeficientes[0])*comprimento/18), int((1+2*coeficientes[1])*altura/18)), int(comprimento/18 - 3), 3)

def posicao(comprimento, altura, coordenadas):
    return ((int(9*coordenadas[0]/altura), int(9*coordenadas[1]/comprimento)))

def desenha_linhas(win, comprimento, altura):
    linhasPrincipais(win, comprimento, altura)
    pygame.draw.rect(win, (255, 255, 255), (0, 0, comprimento, altura), 5)

    deltac = int(comprimento/3)
    deltaa = int(altura/3)

    for i in range(3):
        for j in range(3):
            if (i+j)%2 == 0:
                desenhaJogoIndividual(win, i*deltac, (i+1)*deltac, j*deltaa, (j+1)*deltac, (0, 255, 255))
            else:
                desenhaJogoIndividual(win, i*deltac, (i+1)*deltac, j*deltaa, (j+1)*deltac, (255, 255, 0))

def jogadaAnterior(win, comprimento, altura, coeficientes, id):
    if coeficientes != (-1, -1):
        if id == 0:
            x(win, comprimento, altura, coeficientes, (0, 0, 255))
        elif id == 1:
            o(win, comprimento, altura, coeficientes, (255, 0, 0))

def encerraUnidade(win, comprimento, altura, coeficientes, id):
    pygame.draw.rect(win, (0, 0, 0), (coeficientes[0]*comprimento/3, coeficientes[1]*altura/3, comprimento/3, altura/3))

    if id == 0:
        pygame.draw.circle(win, (0, 0, 255), (int((1+2*coeficientes[0])*comprimento/6), int((1+2*coeficientes[1])*altura/6)), int(comprimento/6 - 10), 3)
    elif id == 1:
        pygame.draw.line(win, (255, 0, 0), (coeficientes[0]*comprimento/3 + 20, coeficientes[1]*altura/3 + 20), ((coeficientes[0]+1)*comprimento/3 - 20, (coeficientes[1]+1)*altura/3 - 20), 3)
        pygame.draw.line(win, (255, 0, 0), (coeficientes[0]*comprimento/3 + 20, (coeficientes[1]+1)*altura/3 - 20), ((coeficientes[0]+1)*comprimento/3 - 20, coeficientes[1]*altura/3 + 20), 3)

def destacaJogo(win, comprimento, altura, coeficientes):
    pygame.draw.rect(win, (0, 255, 0), ((coeficientes[0] - coeficientes[0]//3*3)*comprimento/3, (coeficientes[1] - coeficientes[1]//3*3)*altura/3, comprimento/3, altura/3), 5)

def encerraJdv(win, comprimento, altura, id):
    pygame.draw.rect(win, (0, 0, 0), (0, 0, comprimento, altura))

    if id == 0:
        pygame.draw.circle(win, (0, 0, 255), (int(comprimento/2), int(altura/2)), int(comprimento/2 - 20), 10)
    else:
        pygame.draw.line(win, (255, 0, 0), (20, 20), (comprimento - 20, altura - 20), 10)
        pygame.draw.line(win, (255, 0, 0), (comprimento - 20, 20), (20, altura - 20), 10)