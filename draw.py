import pygame

def desenhaLinhas(win, comprimento, altura):
    pygame.draw.line(win, (255, 255, 255), (comprimento/3, 0), (comprimento/3, altura), 2)
    pygame.draw.line(win, (255, 255, 255), (2*comprimento/3, 0), (2*comprimento/3, altura), 2)
    pygame.draw.line(win, (255, 255, 255), (0, altura/3), (comprimento, altura/3), 2)
    pygame.draw.line(win, (255, 255, 255), (0, 2*altura/3), (comprimento, 2*altura/3), 2)

def x(win, comprimento, altura, coeficientes, cor):
    pygame.draw.line(win, cor, (coeficientes[0]*comprimento/3 + 20, coeficientes[1]*altura/3 + 20), ((coeficientes[0]+1)*comprimento/3 - 20, (coeficientes[1]+1)*altura/3 - 20), 3)
    pygame.draw.line(win, cor, (coeficientes[0]*comprimento/3 + 20, (coeficientes[1]+1)*altura/3 - 20), ((coeficientes[0]+1)*comprimento/3 - 20, coeficientes[1]*altura/3 + 20), 3)

def o(win, comprimento, altura, coeficientes, cor):
    pygame.draw.circle(win, cor, (int((1+2*coeficientes[0])*comprimento/6), int((1+2*coeficientes[1])*altura/6)), int(comprimento/6 - 10), 3)

def posicao(win, comprimento, altura, coordenadas):
    if coordenadas[0] < comprimento/3:
        if coordenadas[1] < altura/3:
            return (0, 0)
        elif coordenadas[1] < 2*altura/3:
            return (0, 1)
        elif coordenadas[1] < 3*altura/3:
            return (0, 2)
    
    elif coordenadas[0] < 2*comprimento/3:
        if coordenadas[1] < altura/3:
            return (1, 0)
        elif coordenadas[1] < 2*altura/3:
            return (1, 1)
        elif coordenadas[1] < 3*altura/3:
            return (1, 2)
    
    elif coordenadas[0] < 3*comprimento/3:
        if coordenadas[1] < altura/3:
            return (2, 0)
        elif coordenadas[1] < 2*altura/3:
            return (2, 1)
        elif coordenadas[1] < 3*altura/3:
            return (2, 2)

def encerraJdv(win, comprimento, altura, id):
    pygame.draw.rect(win, (0, 0, 0), (0, 0, comprimento, altura))

    if id == 0:
        pygame.draw.circle(win, (0, 0, 255), (int(comprimento/2), int(altura/2)), int(comprimento/2 - 20), 10)
    else:
        pygame.draw.line(win, (255, 0, 0), (20, 20), (comprimento - 20, altura - 20), 10)
        pygame.draw.line(win, (255, 0, 0), (comprimento - 20, 20), (20, altura - 20), 10)

def jogadaAnterior(win, comprimento, altura, coordenadas, id):
    if coordenadas != (-1, -1):
        if id == 0:
            x(win, comprimento, altura, coordenadas, (255, 0, 0))
        else:
            o(win, comprimento, altura, coordenadas, (0, 0, 255))