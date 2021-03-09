class tabuleiro:

    def __init__(self):
        self.tab = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        self.vitoria = -1
        self.jogadas = 0

    def getVitoria(self):
        return self.vitoria

    def marcarPosicao(self, id, coordenadas):
        if self.posicaoMarcada(coordenadas):
            return False

        if id == 0:
            self.tab[coordenadas[1]][coordenadas[0]] = 0
        else:
            self.tab[coordenadas[1]][coordenadas[0]] = 1
        
        self.jogadas += 1
        
        return True
    
    def posicaoMarcada(self, coordenadas):
        if self.tab[coordenadas[1]][coordenadas[0]] != -1:
            return True
        else:
            return False

    def final(self):

        if self.vitoria == -1:
            if (self.tab[0][0] == self.tab[0][1]) and (self.tab[0][0] == self.tab[0][2]) and self.tab[0][0] != -1:
                self.vitoria = self.tab[0][0]
                return self.tab[0][0]

            elif (self.tab[0][0] == self.tab[1][0]) and (self.tab[0][0] == self.tab[2][0]) and self.tab[0][0] != -1:
                self.vitoria = self.tab[0][0]
                return self.tab[0][0]

            elif (self.tab[0][0] == self.tab[1][1]) and (self.tab[0][0] == self.tab[2][2]) and self.tab[0][0] != -1:
                self.vitoria = self.tab[0][0]
                return self.tab[0][0]

            elif (self.tab[0][2] == self.tab[1][2]) and (self.tab[0][2] == self.tab[2][2]) and self.tab[0][2] != -1:
                self.vitoria = self.tab[0][2]
                return self.tab[0][2]

            elif (self.tab[0][2] == self.tab[1][1]) and (self.tab[0][2] == self.tab[2][0]) and self.tab[0][2] != -1:
                self.vitoria = self.tab[0][2]
                return self.tab[0][2]                                               

            elif (self.tab[1][0] == self.tab[1][1]) and (self.tab[1][0] == self.tab[1][2]) and self.tab[1][0] != -1:
                self.vitoria = self.tab[1][0]
                return self.tab[1][0]
            
            elif (self.tab[2][0] == self.tab[2][1]) and (self.tab[2][0] == self.tab[2][2]) and self.tab[2][0] != -1:
                self.vitoria = self.tab[2][0]
                return self.tab[2][0]
            
            elif (self.tab[0][1] == self.tab[1][1]) and (self.tab[0][1] == self.tab[2][1]) and self.tab[0][1] != -1:
                self.vitoria = self.tab[0][1]
                return self.tab[0][1]
                        
        return self.getVitoria()

    def getValor(self, coordenadas):
        return self.tab[coordenadas[1]][coordenadas[0]]
