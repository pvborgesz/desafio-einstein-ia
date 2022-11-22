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
        individuo.pontuacao = IndividuoController.newFitness(individuo)
        # individuo.pontuacao = Regras.fitness(individuo)
        # print(individuo.__str__())
        return individuo

    def gerarValorNaoRepetido(lista : list):
        valor = random.randint(1, 5)
        while valor in lista and len(lista) < 5:
            valor = random.randint(1, 5)
        lista.append(valor)    
        return valor

    def criarGeracao(qtdIndividuos:int, geracaoAnterior, maxGeracoes):
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
        
        # novaGeracao = SolucaoController.mutacao(novaGeracao)
        novaGeracao.sort(key=lambda x: x.pontuacao, reverse=True)
        cont = 0

        for i in range(int(len(geracao)* 0.1), 0, -1): # sobrevivencia dos 10% piores pontuados
            novaGeracao.append(geracao[i])


        for i in range(int(len(geracao)* 0.6)):
            pai = random.randint(0, int(len(geracao) * 0.1) - 1)
            mae = random.randint(0, int(len(geracao) * 0.1) - 1)
            while pai == mae:
                mae = random.randint(0, int(len(geracao) * 0.1) - 1)
            filho = SolucaoController.crossover(geracao[pai], geracao[mae])
            filho.pontuacao = IndividuoController.newFitness(filho)
            novaGeracao.append(filho)
            cont += 1

        geracaoId = 1

        while novaGeracao[0].pontuacao <= 15: #quantidade de pontos necessárias para gabaritar
            cont += 1 
            geracaoId += 1
            novaGeracao = SolucaoController.criarNovaGeracao(novaGeracao, qtdIndividuos)
            novaGeracao = SolucaoController.mutacao(novaGeracao) #DESCOMENTAR PARA ATIVAR MUTACAO
            novaGeracao.sort(key=lambda x: x.pontuacao, reverse=True)
            print("o melhor da geração é: ", novaGeracao[0].__str__())
            print("Geração: ", cont)
            
            if (novaGeracao[0].pontuacao == 15):
                print("Solucao Vencedora: ", novaGeracao[0].__str__())

            if (geracaoId >= maxGeracoes):
                novaGeracao.sort(key=lambda x: x.pontuacao, reverse=True)
                print("o melhor da geração é: ", novaGeracao[0].__str__())
                print("Geração: ", cont)
                break

        return novaGeracao

    def criarNovaGeracao(geracaoAnterior, qtdIndividuos):
        novaGeracao = []

        geracaoAnterior.sort(key=lambda x: x.pontuacao, reverse=True)

        for i in range(int(len(geracaoAnterior) * 0.1)): #salvando 30% dos melhores
            if len(novaGeracao) >= qtdIndividuos:
                break
            novaGeracao.append(geracaoAnterior[i])
        
        cont = 0
        for i in range(int(len(geracaoAnterior))-1,int(len(geracaoAnterior) * 0.05), -1): # salvando os 5% piores
            if len(novaGeracao) >= qtdIndividuos:
                break
            novaGeracao.append(geracaoAnterior[i])

        contador = 0
        for i in range(int(len(geracaoAnterior) * 0.85)):
            pai = geracaoAnterior[i]
            mae = geracaoAnterior[len(geracaoAnterior) - 1 - contador]
            contador += 1
            filho = SolucaoController.crossover(pai, mae)
            # filho.pontuacao = IndividuoController.fit(filho)
            filho.pontuacao = IndividuoController.newFitness(filho)

            novaGeracao.append(filho)
            cont += 1

        # for i in range(int(len(geracaoAnterior) * 0.85)): # recombinando os 65% restantes
        #     pai = random.randint(0, int(len(geracaoAnterior) * 0.1) - 1)
        #     mae = random.randint(0, int(len(geracaoAnterior) * 0.1) - 1)
        #     while pai == mae:
        #         mae = random.randint(0, int(len(geracaoAnterior) * 0.1) - 1)
        #     filho = SolucaoController.crossover(geracaoAnterior[pai], geracaoAnterior[mae])
        #     # filho.pontuacao = IndividuoController.fit(filho)
        #     filho.pontuacao = IndividuoController.newFitness(filho)

        #     novaGeracao.append(filho)
        #     cont += 1
        #     if len(novaGeracao) >= qtdIndividuos:
        #         break

        # print("a nova geracao tem tamanho: ", len(novaGeracao))
        return novaGeracao
    
    def recombinacao(pai: Individuo, mae:Individuo): #gerava problema de valores repetidos
        arg1 = [pai.solucoes[0][0], mae.solucoes[0][1], pai.solucoes[0][2], mae.solucoes[0][3], pai.solucoes[0][4]]
        arg2 = [mae.solucoes[1][0], pai.solucoes[1][1], mae.solucoes[1][2], pai.solucoes[1][3], mae.solucoes[1][4]]
        arg3 = [pai.solucoes[2][0], mae.solucoes[2][1], pai.solucoes[2][2], mae.solucoes[2][3], pai.solucoes[2][4]]
        arg4 = [mae.solucoes[3][0], pai.solucoes[3][1], mae.solucoes[3][2], pai.solucoes[3][3], mae.solucoes[3][4]]
        arg5 = [pai.solucoes[4][0], mae.solucoes[4][1], pai.solucoes[4][2], mae.solucoes[4][3], pai.solucoes[4][4]]
        # filho = Individuo([pai.solucoes[0], mae.solucoes[1], pai.solucoes[2], mae.solucoes[3], pai.solucoes[4]], pai.id + 1)
        filho = Individuo([arg1, arg2, arg3, arg4, arg5], pai.id + 1)
        return filho


    ''' esse método funciona da seguinte maneira: 
        1 - é gerado um número aleatório entre 0 e 1, caso seja 0, o filho terá 2 genes do pai e 3 genes da mãe, caso seja 1, o filho terá 3 genes do pai e 2 genes da mãe
        2 - é substituido o valor do gene do fakePai para None. Foi criado um fakepai para que o valor do pai nao seja alterado por referencia.
        3 - é feito um loop para substituir os valores do filho pelos valores da mãe, caso o valor do gene seja None.
    '''
    def crossover(pai : Individuo, mae: Individuo): 
        fakePai = pai
        fakeMae = mae

        randomChoice = random.randint(0, 1)
        cont = 0
        if randomChoice == 1:
            for i in fakePai.solucoes:
                for j in i:
                    if cont % 2 == 0:
                        j = None
                    cont += 1
            filho = Individuo([fakePai.solucoes[0],fakePai.solucoes[1] , fakePai.solucoes[2], fakePai.solucoes[3], fakePai.solucoes[4]], fakePai.id )
        else:
            for i in fakePai.solucoes:
                for j in i:
                    if cont % 2 != 0:
                        j = None
                    cont += 1
            filho = Individuo([fakePai.solucoes[0], fakePai.solucoes[1], fakePai.solucoes[2], fakePai.solucoes[3], fakePai.solucoes[4]], fakePai.id )    

        for i in filho.solucoes:
            for j in range(len(i)):
                if i[j] == None:
                    for k in fakeMae.solucoes:
                        for l in range(len(k)):
                            if k[l] not in i:
                                i[j] = k[l]
                                break
        return filho

    def mutacao(geracao: list):
        k = random.randint(1, 30)
        flagMutacao = False
        randomValue = random.randint(0, len(geracao)-1) # gerar valor aleatorio para usar como index
        olderValue = 0
        randomRow, randomColumn = random.randint(0, 4), random.randint(0, 4)
        
        if k == 1:
            flagMutacao = True
            for i in range (len(geracao)):
                if i == randomValue:
                    olderValue = geracao[i].solucoes[randomRow][randomColumn]
                    geracao[i].solucoes[randomRow][randomColumn] = random.randint(1, 5)
                    # verify if has any value equal to the new value, if has change to the older value
                    for j in range(len(geracao[i].solucoes)):
                        for k in range(len(geracao[i].solucoes[j])):
                            if geracao[i].solucoes[j][k] == geracao[i].solucoes[randomRow][randomColumn]:
                                geracao[i].solucoes[j][k] = olderValue
                                break
        return geracao

    def run(qtdIndividuos:int, qtdGeracoes : int ):
        geracao = SolucaoController.criarGeracao(qtdIndividuos,[], qtdGeracoes)