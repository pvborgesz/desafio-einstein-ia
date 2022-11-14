from Model.Solucao import Solucao
from Model.Individuo import Individuo
from Controllers.IndividuoController import IndividuoController
import random

class SolucaoController:
    def gerarSolucao(individuo : list):
        solucao = Solucao(individuo[0], individuo[1], individuo[2], individuo[3], individuo[4])
        # print(solucao.__str__())
        return solucao        
    
    def gerarSolucaoAleatoria():        
        solucoes = []
        # solucao = Solucao(random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5))
        todasCores = []
        for i in range (5):
            # solucao = Solucao(random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5))
            cor = SolucaoController.gerarCor(todasCores)
            
            solucao = [random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5)]
            print( "Solucao gerada: ", (solucao.__str__()))
            solucoes.append(solucao) 

        individuo = Individuo(solucoes)

        individuo = IndividuoController.gerarPontuacao(individuo)

        return individuo

    def decoficarSolucao(individuo : list):
        solucao = SolucaoController.gerarSolucao(individuo)
        return solucao

    def gerarCor(todasCores):
        cor = random.randint(1, 5)
        print(todasCores)
        if cor not in todasCores:
            todasCores.append(cor)
            currentColor = cor
            # todasCores.append(currentColor)
            return currentColor
        else:
            SolucaoController.gerarCor(todasCores)
