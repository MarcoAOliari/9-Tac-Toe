from tabuleiro import tabuleiro

class noveDaVelha:

    def __init__(self):
        self.tabuleiros = [[tabuleiro(), tabuleiro(), tabuleiro()], [tabuleiro(), tabuleiro(), tabuleiro()], [tabuleiro(), tabuleiro(), tabuleiro()]]
        self.vitoria = -1
        self.tabmaior = tabuleiro()
        self.inicio = 0
        
    def marcaTabuleiro(self, id, coordenadas, jogadaAnterior):
        if self.unidadeTerminada(((jogadaAnterior[0] - jogadaAnterior[0]//3*3), (jogadaAnterior[1] - jogadaAnterior[1]//3*3)), 0):
            if not self.unidadeTerminada(coordenadas, 1):
                return self.tabuleiros[int(coordenadas[1]/3)][int(coordenadas[0]/3)].marcarPosicao(id, (int(coordenadas[1]%3), int(coordenadas[0]%3)))
            else:
                return False
        elif (self.unidadeCorreta(coordenadas, jogadaAnterior) and not self.unidadeTerminada(coordenadas, 1)) or self.primeiraJogada():
            return self.tabuleiros[int(coordenadas[1]/3)][int(coordenadas[0]/3)].marcarPosicao(id, (int(coordenadas[1]%3), int(coordenadas[0]%3)))
    
    def getValor(self, coordenadas):
        return self.tabuleiros[int(coordenadas[1]/3)][int(coordenadas[0]/3)].getValor((int(coordenadas[0]%3), int(coordenadas[1]%3)))

    def marcaTabuleiroMaior(self, id, coordenadas):
        return self.tabmaior.marcarPosicao(id, coordenadas)

    def unidadeCorreta(self, pos, jogadaAnterior):
        if pos[0]//3 == (jogadaAnterior[0] - jogadaAnterior[0]//3*3) and pos[1]//3 == (jogadaAnterior[1] - jogadaAnterior[1]//3*3):
            return True
        else:
            return False
    
    def primeiraJogada(self):
        if self.inicio == 0:
            self.inicio = 1
            return True
        else:
            return False
    
    def unidadeTerminada(self, coordenadas, id):
        if id == 0:
            if self.tabmaior.tab[coordenadas[1]][coordenadas[0]] != -1:
                return True
            else:
                return False
        if id == 1:
            if self.tabmaior.tab[coordenadas[1]//3][coordenadas[0]//3] != -1:
                return True
            else:
                return False

    def deuVelha(self):
        cont = 0
        for i in range(3):
            for j in range(3):
                if self.tabuleiros[i][j].jogadas == 9 or self.tabuleiros[i][j].vitoria != -1:
                   cont += 1

        return True if cont == 9 else False 

    def contaResultado(self):
        o = 0
        x = 0
        for i in range(3):
            for j in range(3):
                if self.tabmaior.tab[i][j] == 0:
                    o += 1
                else:
                    x += 1
        
        return 0 if o > x else 1