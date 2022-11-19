from Model.Solucao import Solucao
from Model.Individuo import Individuo
from Controllers.IndividuoController import IndividuoController
import random

class SolucaoController:
    def gerarSolucao(individuo : list):
        solucao = Solucao(individuo[0], individuo[1], individuo[2], individuo[3], individuo[4])
        # print(solucao.__str__())
        return solucao        
    
    def gerarSolucaoAleatoria(id : int):        
        solucoes = []
        todasCores = []
        for i in range (5):
            # solucoes.append(SolucaoController.gerarValorNaoRepetido(todasCores), SolucaoController.gerarValorNaoRepetido(todasCores), SolucaoController.gerarValorNaoRepetido(todasCores), SolucaoController.gerarValorNaoRepetido(todasCores), SolucaoController.gerarValorNaoRepetido(todasCores))
            solucao = [SolucaoController.gerarValorNaoRepetido(todasCores), SolucaoController.gerarValorNaoRepetido(todasCores), SolucaoController.gerarValorNaoRepetido(todasCores), SolucaoController.gerarValorNaoRepetido(todasCores), SolucaoController.gerarValorNaoRepetido(todasCores)]
            # print( "Solucao gerada: ", (solucao.__str__()))
            solucoes.append(solucao)
            if len (solucao) == 5:
                todasCores = []
        individuo = Individuo(solucoes, id)

        # individuo.pontuacao = IndividuoController.gerarPontuacao(individuo)
        # individuo.pontuacao = IndividuoController.fitness(individuo)

        individuo.pontuacao = IndividuoController.fit(individuo)
        # print(individuo.__str__())
        return individuo

    def gerarValorNaoRepetido(lista : list):
        valor = random.randint(1, 5)
        while valor in lista and len(lista) < 5:
            valor = random.randint(1, 5)
        lista.append(valor)    
        return valor

    def criarGeracao(qtdIndividuos:int):
        geracao = []
        for i in range(qtdIndividuos):
            geracao.append(SolucaoController.gerarSolucaoAleatoria(i))
        
        print("Iniciando recombinação:")
        #ordenar a geracao pela pontuacao
        geracao.sort(key=lambda x: x.pontuacao, reverse=True)
        print("O indivio com a maior pontuação da geração foi: ", geracao[0].__str__())
        novaGeracao = []
        for i in range(len(geracao)//2):
            SolucaoController.recombinacao(geracao[i], geracao[i])
            novaGeracao.append(SolucaoController.recombinacao(geracao[i], geracao[i+1]))
        return geracao
    
    def recombinacao(pai: Individuo, mae:Individuo):
        solucoesFilho = []
        if pai.id % 2 == 0: # se o pai for par, o filho vai ter 3 caracteristicas dele e 2 da mae.
            for i in range(3):
                solucoesFilho.append(pai.solucoes[i])
            for i in range(3, 5):
                solucoesFilho.append(mae.solucoes[i])
        else: #caso contrario, o filho vai ter 3 caracteristicas da mae e 2 do pai.
            for i in range(3):
                solucoesFilho.append(mae.solucoes[i])
            for i in range(3, 5):
                solucoesFilho.append(pai.solucoes[i])
        filho = Individuo(solucoesFilho, pai.id + mae.id)
        return filho