
class Solucao:
    def __init__(self, cor, nacionalidade, bebida, cigarro, animal):
        self.cor = cor
        self.nacionalidade = nacionalidade
        self.bebida = bebida
        self.cigarro = cigarro
        self.animal = animal
        
        self.solucaoCorreta = {
            cor:[3,4,1,2,5],
            nacionalidade:[4,3,1,5,2],
            bebida:[1,5,3,2,4],
            cigarro: [2,3,1,4,5], 
            animal:[3,4,1,5,2]}

    def __str__(self):
        return "Cor: " + str(self.cor) + " Nacionalidade: " + str(self.nacionalidade) + " Bebida: " + str(self.bebida) + " Cigarro: " + str(self.cigarro) + " Animal: " + str(self.animal)
