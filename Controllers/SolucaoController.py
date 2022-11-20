from Model.Solucao import Solucao
from Model.Individuo import Individuo
from Controllers.IndividuoController import IndividuoController
from Model.Regras import Regras
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
        # individuo.pontuacao = Regras.fitness(individuo)
        # print(individuo.__str__())
        return individuo

    def gerarValorNaoRepetido(lista : list):
        valor = random.randint(1, 5)
        while valor in lista and len(lista) < 5:
            valor = random.randint(1, 5)
        lista.append(valor)    
        return valor

    def criarGeracao(qtdIndividuos:int, geracaoAnterior):
        geracao = []
        if len(geracaoAnterior) < 1 :
            for i in range(qtdIndividuos):
                geracao.append(SolucaoController.gerarSolucaoAleatoria(i))
        else:
            geracao = geracaoAnterior
        
        print("Iniciando recombinação:")

        #ordenar a geracao pela pontuacao
        geracao.sort(key=lambda x: x.pontuacao, reverse=True)

        novaGeracao = []

        for i in range(int(len(geracao) * 0.4)): # sobrevivencia dos 20% melhores pontuados
            novaGeracao.append(geracao[i])
        
        novaGeracao = SolucaoController.mutacao(novaGeracao)
        novaGeracao.sort(key=lambda x: x.pontuacao, reverse=True)
        cont = 0

        for i in range(int(len(geracao)* 0.6)):
            pai = random.randint(0, int(len(geracao) * 0.1) - 1)
            mae = random.randint(0, int(len(geracao) * 0.1) - 1)
            while pai == mae:
                mae = random.randint(0, int(len(geracao) * 0.1) - 1)
            filho = SolucaoController.recombinacao(geracao[pai], geracao[mae])
            filho.pontuacao = IndividuoController.fit(filho)
            novaGeracao.append(filho)
            cont += 1

        
        while novaGeracao[0].pontuacao < 20: #quantidade de pontos necessárias para gabaritar
            cont += 1 
            # print(len(novaGeracao), "len nova geracao 1 ")
            novaGeracao = SolucaoController.criarNovaGeracao(novaGeracao, qtdIndividuos)
            novaGeracao = SolucaoController.mutacao(novaGeracao)
            novaGeracao.sort(key=lambda x: x.pontuacao, reverse=True)
            print("o melhor da geração é: ", novaGeracao[0].__str__())
            for i in range(len(novaGeracao)-1, 0, -1):
                print(novaGeracao[i].solucoes, novaGeracao[i].pontuacao)
            print("Geração: ", cont)

        return novaGeracao

    def criarNovaGeracao(geracaoAnterior, qtdIndividuos):
        novaGeracao = []

        geracaoAnterior.sort(key=lambda x: x.pontuacao, reverse=True)

        for i in range(int(len(geracaoAnterior) * 0.4)): #salvando 40% dos melhores
            if len(novaGeracao) >= qtdIndividuos:
                break
            novaGeracao.append(geracaoAnterior[i])
        
        cont = 0
        for i in range(int(len(geracaoAnterior))-1,int(len(geracaoAnterior) * 0.2), -1): # salvando os 20% piores
            if len(novaGeracao) >= qtdIndividuos:
                break
            novaGeracao.append(geracaoAnterior[i])

        for i in range(int(len(geracaoAnterior) * 0.4)): # recombinando os 40% restantes
            pai = random.randint(0, int(len(geracaoAnterior) * 0.1) - 1)
            mae = random.randint(0, int(len(geracaoAnterior) * 0.1) - 1)
            while pai == mae:
                mae = random.randint(0, int(len(geracaoAnterior) * 0.1) - 1)
            filho = SolucaoController.recombinacao(geracaoAnterior[pai], geracaoAnterior[mae])
            filho.pontuacao = IndividuoController.fit(filho)

            novaGeracao.append(filho)
            cont += 1
            if len(novaGeracao) >= qtdIndividuos:
                break

        print("a nova geracao tem tamanho: ", len(novaGeracao))
        return novaGeracao
    
    def recombinacao(pai: Individuo, mae:Individuo):
        arg1 = [pai.solucoes[0][0], mae.solucoes[0][1], pai.solucoes[0][2], mae.solucoes[0][3], pai.solucoes[0][4]]
        arg2 = [mae.solucoes[1][0], pai.solucoes[1][1], mae.solucoes[1][2], pai.solucoes[1][3], mae.solucoes[1][4]]
        arg3 = [pai.solucoes[2][0], mae.solucoes[2][1], pai.solucoes[2][2], mae.solucoes[2][3], pai.solucoes[2][4]]
        arg4 = [mae.solucoes[3][0], pai.solucoes[3][1], mae.solucoes[3][2], pai.solucoes[3][3], mae.solucoes[3][4]]
        arg5 = [pai.solucoes[4][0], mae.solucoes[4][1], pai.solucoes[4][2], mae.solucoes[4][3], pai.solucoes[4][4]]
        

        # filho = Individuo([pai.solucoes[0], mae.solucoes[1], pai.solucoes[2], mae.solucoes[3], pai.solucoes[4]], pai.id + 1)
        filho = Individuo([arg1, arg2, arg3, arg4, arg5], pai.id + 1)
        return filho

    def mutacao(geracao: list):
        k = random.randint(1, 30)
        flagMutacao = False
        if k == 2:
            for i in range(len(geracao)):
                if(flagMutacao):
                    break
                for j in range(len(geracao[i].solucoes)):
                    if(flagMutacao):
                        break
                    for l in range(len(geracao[i].solucoes[j])):
                        if(flagMutacao):
                            break
                        if l == k:
                            geracao[i].solucoes[j][l] = random.randint(1, 5)
                            print('OCORREU UMA MUTAÇÃO ')
                            flagMutacao = True
                            break

        else:
            return geracao
        return geracao

    def run(qtdIndividuos:int):
        geracao = SolucaoController.criarGeracao(qtdIndividuos,[])
        # # geracao.sort(key=lambda x: x.pontuacao, reverse=True)
        # # cont = 0
        # # while geracao[0].pontuacao < 25:
        # # # while cont < 25:
        # #     cont += 1 
        # #     geracao = SolucaoController.criarGeracao(qtdIndividuos)
        # #     geracao.sort(key=lambda x: x.pontuacao, reverse=True)
        # #     print("O individuo com a maior pontuação da geração foi: ", geracao[0].__str__())
        #     print("Geração: ", cont)