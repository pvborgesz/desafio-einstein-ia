class Individuo:
    def __init__(self, solucoes, *id):
        if id is not None: self.id= id[0]
        self.solucoes = solucoes
        self.pontuacao = 0  # referente a pontuacao da solucao
    
    def __str__(self):
        return "Nome: " + str(self.id) + " \nPontuacao: " + str(self.pontuacao) + " \nSolucoes: " + str(self.solucoes)

    def addPonto(self):
        self.pontuacao+=1