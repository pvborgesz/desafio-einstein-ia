class Individuo:
    def __init__(self, solucoes):
        self.nome = ''
        self.solucoes = solucoes
        self.pontuacao = 0  # referente a pontuacao da solucao
    
    def __str__(self):
        return "Nome: " + self.nome + " Pontuacao: " + str(self.pontuacao) + " Solucoes: " + str(self.solucoes)