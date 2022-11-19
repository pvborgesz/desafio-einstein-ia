class Individuo:
    def __init__(self, solucoes):
        self.nome = ''
        self.solucoes = solucoes
        self.pontuacao = 0  # referente a pontuacao da solucao
    
    def __str__(self):
        return "Nome: " + self.nome + " \nPontuacao: " + str(self.pontuacao) + " \nSolucoes: " + str(self.solucoes)

    def addPonto(self):
        self.pontuacao+=1