from Model.Individuo import Individuo

class IndividuoController:
    def __init__(self):
        pass

    def gerarPontuacao(individuo: Individuo):
        # print(Individuo.__str__(individuo))
        for i in range(len(individuo.solucoes[0])): # verificando cores
            if individuo.solucoes[0] == 3 and i == 0:
                individuo.pontuacao += 1
            elif individuo.solucoes[0] == 4 and i == 1:
                individuo.pontuacao += 1
            elif individuo.solucoes[0] == 1 and i == 2:
                individuo.pontuacao += 1
            elif individuo.solucoes[0] == 2 and i == 3:
                individuo.pontuacao += 1
            elif individuo.solucoes[0] == 5 and i == 4:
                individuo.pontuacao += 1

        for i in range(len(individuo.solucoes[1])): # verificando nacionalidade
            if individuo.solucoes[1] == 4 and i == 0:
                individuo.pontuacao += 1
            elif individuo.solucoes[1] == 3 and i == 1:
                individuo.pontuacao += 1
            elif individuo.solucoes[1] == 1 and i == 2:
                individuo.pontuacao += 1
            elif individuo.solucoes[1] == 5 and i == 3:
                individuo.pontuacao += 1
            elif individuo.solucoes[1] == 2 and i == 4:
                individuo.pontuacao += 1
        
        # repita o processo para as proximas caracteristicas

        for i in range(len(individuo.solucoes[2])):
            if individuo.solucoes[2] == 1 and i == 0:
                individuo.pontuacao += 1
            elif individuo.solucoes[2] == 5 and i == 1:
                individuo.pontuacao += 1
            elif individuo.solucoes[2] == 3 and i == 2:
                individuo.pontuacao += 1
            elif individuo.solucoes[2] == 2 and i == 3:
                individuo.pontuacao += 1
            elif individuo.solucoes[2] == 4 and i == 4:
                individuo.pontuacao += 1
        
        for i in range(len(individuo.solucoes[3])):
            if individuo.solucoes[3] == 5 and i == 0:
                individuo.pontuacao += 1
            elif individuo.solucoes[3] == 4 and i == 1:
                individuo.pontuacao += 1
            elif individuo.solucoes[3] == 1 and i == 2:
                individuo.pontuacao += 1
            elif individuo.solucoes[3] == 3 and i == 3:
                individuo.pontuacao += 1
            elif individuo.solucoes[3] == 2 and i == 4:
                individuo.pontuacao += 1
        
        for i in range(len(individuo.solucoes[4])):
            if individuo.solucoes[4] == 2 and i == 0:
                individuo.pontuacao += 1
            elif individuo.solucoes[4] == 1 and i == 1:
                individuo.pontuacao += 1
            elif individuo.solucoes[4] == 4 and i == 2:
                individuo.pontuacao += 1
            elif individuo.solucoes[4] == 5 and i == 3:
                individuo.pontuacao += 1
            elif individuo.solucoes[4] == 3 and i == 4:
                individuo.pontuacao += 1

        print("O individuo pontuou: ", individuo.pontuacao)

        return individuo.pontuacao

''' 
            cor:[3,4,1,2,5],
            nacionalidade:[4,3,1,5,2],
            bebida:[1,5,3,2,4],
            cigarro: [2,3,1,4,5], 
            animal:[3,4,1,5,2]}
'''