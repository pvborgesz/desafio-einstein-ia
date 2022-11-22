class Individuo:
    def __init__(self, solucoes, *id):
        if id is not None: self.id= id[0]
        self.solucoes = solucoes
        self.pontuacao = 0  # referente a pontuacao da solucao
        self.solucaoCorreta = [[3,4,1,2,5], [4,3,1,5,2],
            [1,5,3,2,4],
            [2,3,1,4,5], 
            [3,4,1,5,2]]
    
    def __str__(self):
        return "Nome: " + str(self.id) + " \nPontuacao: " + str(self.pontuacao) + " \nSolucoes: " + str(self.solucoes)

    def addPonto(self):
        self.pontuacao+=1