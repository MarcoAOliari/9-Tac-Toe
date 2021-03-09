from tabuleiro import tabuleiro

class noveDaVelha:

    def __init__(self):
        self.tabuleiros = [[tabuleiro(), tabuleiro(), tabuleiro()], [tabuleiro(), tabuleiro(), tabuleiro()], [tabuleiro(), tabuleiro(), tabuleiro()]]
        self.vitoria = -1
        self.tabmaior = tabuleiro()
        self.inicio = 0
        
    def marcaTabuleiro(self, id_tab, coordenadas, jogadaAnterior):
        if self.unidadeTerminada(((jogadaAnterior[0] - jogadaAnterior[0]//3*3), (jogadaAnterior[1] - jogadaAnterior[1]//3*3)), 0):
            if not self.unidadeTerminada(coordenadas, 1):
                return self.tabuleiros[int(coordenadas[1]/3)][int(coordenadas[0]/3)].marcarPosicao(id_tab, (int(coordenadas[1]%3), int(coordenadas[0]%3)))
            else:
                return False
        elif (self.unidadeCorreta(coordenadas, jogadaAnterior) and not self.unidadeTerminada(coordenadas, 1)) or self.primeiraJogada():
            return self.tabuleiros[int(coordenadas[1]/3)][int(coordenadas[0]/3)].marcarPosicao(id_tab, (int(coordenadas[1]%3), int(coordenadas[0]%3)))
    
    def getValor(self, coordenadas):
        return self.tabuleiros[int(coordenadas[1]/3)][int(coordenadas[0]/3)].getValor((int(coordenadas[0]%3), int(coordenadas[1]%3)))

    def marcaTabuleiroMaior(self, id_tab, coordenadas):
        return self.tabmaior.marcarPosicao(id_tab, coordenadas)

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
    
    def unidadeTerminada(self, coordenadas, idu):
        if idu == 0:
            if self.tabmaior.tab[coordenadas[1]][coordenadas[0]] != -1:
                return True
            else:
                return False
        if idu == 1:
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

        return cont == 9

    def contaResultado(self):
        o_counter = 0
        x_counter = 0
        for i in range(3):
            for j in range(3):
                if self.tabmaior.tab[i][j] == 0:
                    o_counter += 1
                else:
                    x_counter += 1
        
        return 0 if o_counter > x_counter else 1