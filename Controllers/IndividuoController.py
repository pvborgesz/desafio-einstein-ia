from Model.Individuo import Individuo
''' 
            cor:[3,4,1,2,5],
            nacionalidade:[4,3,1,5,2],
            bebida:[1,5,3,2,4],
            cigarro: [2,3,1,4,5], 
            animal:[3,4,1,5,2]}
'''
class IndividuoController:
    def __init__(self):
        pass

    def fit (individuo : Individuo):
        IndividuoController.newFitness(individuo)
        # print(individuo.__str__())
        cor, nacionalidade, bebida, cigarro, animal = individuo.solucoes[0], individuo.solucoes[1], individuo.solucoes[2], individuo.solucoes[3], individuo.solucoes[4]
        # print(cor, nacionalidade, bebida, cigarro, animal)

        for i in range(len(cor)):
            if (i == 0 and cor[i] == 3) or (i == 1 and cor[i] == 4) or (i == 2 and cor[i] == 1) or (i == 3 and cor[i] == 2) or (i == 4 and cor[i] == 5):
                individuo.pontuacao += 1
        
        # por enquanto só avalia as posicoes, não as proposicoes em si. 
        for i in range(len(nacionalidade)):
            if (i == 0 and nacionalidade[i] == 4) or (i == 1 and nacionalidade[i] == 3) or (i == 2 and nacionalidade[i] == 1) or (i == 3 and nacionalidade[i] == 5) or (i == 4 and nacionalidade[i] == 2):
                individuo.pontuacao += 1
                # print("o valor na posicao [0][1] era ", i, nacionalidade[i])
        for i in range(len(bebida)):
            if (i == 0 and bebida[i] == 1) or (i == 1 and bebida[i] == 5) or (i == 2 and bebida[i] == 3) or (i == 3 and bebida[i] == 2) or (i == 4 and bebida[i] == 4):
                individuo.pontuacao += 1
                # print("o valor na posicao [0][2] era ", i, bebida[i])
        for i in range(len(cigarro)):
            if (i == 0 and cigarro[i] == 2) or (i == 1 and cigarro[i] == 3) or (i == 2 and cigarro[i] == 1) or (i == 3 and cigarro[i] == 4) or (i == 4 and cigarro[i] == 5):
                individuo.pontuacao += 1
                # print("o valor na posicao [0][3] era ", i, cigarro[i])
        for i in range(len(animal)):
            if (i == 0 and animal[i] == 3) or (i == 1 and animal[i] == 4) or (i == 2 and animal[i] == 1) or (i == 3 and animal[i] == 5) or (i == 4 and animal[i] == 2):
                individuo.pontuacao += 1
                # print("o valor na posicao [0][4] era ", i, animal[i])

        # print("a pontuacao do individuo é : ", individuo.pontuacao)
        return individuo.pontuacao
        

    def gerarPontuacao(individuo: Individuo):
        # print(individuo.__str__(), 'das')
        # print(individuo.solucoes[0][0], 'qwe')
        for i in range(len(individuo.solucoes[0])): # verificando cores
            if individuo.solucoes[0][0] == 3 and i == 0:
                individuo.pontuacao += 1
                print("o valor na posicao [0][0] era ", individuo.solucoes[0][0])
            elif individuo.solucoes[0][1] == 4 and i == 1:
                individuo.pontuacao += 1
                print("o valor na posicao [0][1] era ", individuo.solucoes[0][1])
            elif individuo.solucoes[0][2] == 1 and i == 2:
                individuo.pontuacao += 1
                print("o valor na posicao [0][2] era ", individuo.solucoes[0][2])
            elif individuo.solucoes[0][3] == 2 and i == 3:
                individuo.pontuacao += 1
                print("o valor na posicao [0][3] era ", individuo.solucoes[0][3])
            elif individuo.solucoes[0][4] == 5 and i == 4:
                individuo.pontuacao += 1
                print("o valor na posicao [0][4] era ", individuo.solucoes[0][4])

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


    def fitness(individuo: Individuo):

        ## "O Norueguês vive na primeira casa."
        if (Nacionalidades(Solucao.getNacionalidade()[0]).value == 4):
            individuo.addPonto()


        ## "O Inglês mora na casa vermelha."
        for nacionalidades in Solucao.getNacionalidade():
            if (Nacionalidades(nacionalidades).value == 1):
                casa = Solucao.getNacionalidade().index(nacionalidades)
                if (Nacionalidades(Solucao.getCorCasa()[casa]).value == 2):
                    individuo.addPonto()

        ## "O Sueco tem Cachorros como animais de estimação."
        for nacionalidades in Solucao.getNacionalidade():
            if (Nacionalidades(nacionalidades).value == 2):
                casa = Solucao.getNacionalidade().index(nacionalidades)
                if (Animais(Solucao.getCorCasa()[casa]).value == 2):
                    individuo.addPonto()                

        ## "O Dinamarquês bebe chá."
        for nacionalidades in Solucao.getNacionalidade():
            if (Nacionalidades(nacionalidades).value == 3):
                casa = Solucao.getNacionalidade().index(nacionalidades)
                if (Bebidas(Solucao.getCorCasa()[casa]).value == 5):
                    individuo.addPonto()

        ## "A casa verde está imediatamente à esquerda da casa branca."
        for cores in Solucao.getCorCasa():
            if (CorCasas(cores).value == 2):
                casa = Solucao.getCorCasa().index(cores)
                if (casa != 4):
                    if (CorCasas(casa+1).value == 5):
                        individuo.addPonto()

        ## "O dono da casa verde bebe café."
        for cores in Solucao.getCorCasa():
            if (CorCasas(cores).value == 2):
                casa = Solucao.getCorCasa().index(cores)
                if (Bebidas(Solucao.getCorCasa()[casa]).value == 2):
                    individuo.addPonto()

        ## "A pessoa que fuma Pall Mall cria pássaros."
        for cigarros in Solucao.getCigarro():
            if (Cigarro(cigarros).value == 1):
                casa = Solucao.getCigarro().index(cigarros)
                if (Animais(Solucao.getBebida()[casa]).value == 1):
                    individuo.addPonto()
        ## "O dono da casa amarela fuma Dunhill."
        for cores in Solucao.getCigarro():
            if (CorCasas(cores).value == 3):
                casa = Solucao.getCorCasa().index(cores)
                if (Cigarro(Solucao.getCigarro()[casa]).value == 2):
                    individuo.addPonto()

        ## "O homem que vive na casa do centro bebe leite."
        if (Bebidas(Solucao.getBebida()[2]).value == 3):
            individuo.addPonto()

        ## "O alemão fuma Prince."
        for nacionalidades in Solucao.getNacionalidade():
            if (Nacionalidades(nacionalidades).value == 5):
                casa = Solucao.getNacionalidade().index(nacionalidades)
                if (Cigarro(Solucao.getCigarro()[casa]).value == 4):
                    individuo.addPonto()

        ## "O norueguês vive ao lado da casa azul."
        for nacionalidades in Solucao.getNacionalidade():
            if (Nacionalidades(nacionalidades).value == 4):
                casa = Solucao.getNacionalidade().index(cigarros)
                if (casa == 0):
                    if (CorCasas(Solucao.getCorCasa()[casa+1]).value == 4):
                        individuo.addPonto()
                elif (casa == 4):
                    if (CorCasas(Solucao.getCorCasa()[casa-1]).value == 4):
                        individuo.addPonto()

        ## "O homem que fuma Blends tem um vizinho que bebe água."
        for cigarros in Solucao.getCigarro():
            if (Cigarro(cigarros).value == 3):
                casa = Solucao.getCigarro().index(cigarros)
                if (casa == 0):
                    if (CorCasas(Solucao.getBebida()[casa+1]).value == 1):
                        individuo.addPonto()
                elif (casa == 4):
                    if (CorCasas(Solucao.getBebida()[casa-1]).value == 1):
                        individuo.addPonto()

        ## "O homem que tem um gato vive ao lado da casa que fuma Dunhill."
        for animais in Solucao.getAnimal():
            if (Animais(animais).value == 3):
                casa = Solucao.getAnimal().index(animais)
                if (casa == 0):
                    if (Cigarro(Solucao.getCigarro()[casa+1]).value == 2):
                        individuo.addPonto()
                elif (casa == 4):
                    if (Cigarro(Solucao.getCigarro()[casa-1]).value == 2):
                        individuo.addPonto()

        ## "O homem que fuma Blue Master bebe cerveja."
        for cigarros in Solucao.getNacionalidade():
            if (Cigarro(cigarros).value == 5):
                casa = Solucao.getNacionalidade().index(cigarros)
                if (Cigarro(Solucao.getCigarro()[casa]).value == 4):
                    individuo.addPonto()

        # com base no método anterior, quero fazer um método capaz de identificar se as regras estão corretas, de acordo com as posicoes do vetor
        # e se estiverem corretas, adicionar um ponto ao individuo
    def newFitness(individuo: Individuo):
        cores = individuo.solucoes[0]
        nacionalidades = individuo.solucoes[1]
        bebidas = individuo.solucoes[2]
        cigarros = individuo.solucoes[3]
        animais = individuo.solucoes[4]

        
        for i in range (5):
            ## "O Norueguês vive na primeira casa."
            if nacionalidades[i] == 4 and i == 0:
                print("O Norueguês vive na primeira casa. ")
                individuo.pontuacao += 1
            
            ## "O Inglês mora na casa vermelha."
            if nacionalidades[i] == 1 and cores[i] == 1:
                print("O Inglês mora na casa vermelha. ")
                individuo.pontuacao += 1
            
            ## "O Sueco tem Cachorros como animais de estimação."
            if nacionalidades[i] == 2 and animais[i] == 2:
                print("O Sueco tem Cachorros como animais de estimação. ")
                individuo.pontuacao += 1

            ## "O Dinamarquês bebe chá."
            if nacionalidades[i] == 3 and bebidas[i] == 5:
                print("O Dinamarquês bebe chá. ")
                individuo.pontuacao += 1
            
            ## "A casa verde está imediatamente à esquerda da casa branca."
            if i < 4:
                if cores[i] == 2 and cores[i+1] == 5:
                    print("A casa verde está imediatamente à esquerda da casa branca. ")
                    individuo.pontuacao += 1
            
            ## "O dono da casa verde bebe café."
            if cores[i] == 2 and bebidas[i] == 2:
                print("O dono da casa verde bebe café. ")
                individuo.pontuacao += 1

            ## "A pessoa que fuma Pall Mall cria pássaros."
            if cigarros[i] == 1 and animais[i] == 1:
                print("A pessoa que fuma Pall Mall cria pássaros. ")
                individuo.pontuacao += 1

            ## "O dono da casa amarela fuma Dunhill."
            if cores[i] == 3 and cigarros[i] == 2:
                print("O dono da casa amarela fuma Dunhill. ")
                individuo.pontuacao += 1

            ## "O homem que vive na casa do meio bebe leite."
            if i == 2 and bebidas[i] == 3:
                print("O homem que vive na casa do meio bebe leite. ")
                individuo.pontuacao += 1

            ## "O alemão fuma Prince."
            if nacionalidades[i] == 5 and cigarros[i] == 4:
                print("O alemão fuma Prince. ")
                individuo.pontuacao += 1
        
            ## "O norueguês vive ao lado da casa azul."
            if i < 4:
                if nacionalidades[i] == 4 and cores[i+1] == 4:
                    print("O norueguês vive ao lado da casa azul. ")
                    individuo.pontuacao += 1

            ## "O homem que fuma Blends tem um vizinho que bebe água."
            if i < 4 and i > 0:
                if cigarros[i] == 3 and bebidas[i+1] == 1 or bebidas [i-1] == 1:
                    print("O homem que fuma Blends tem um vizinho que bebe água. ")
                    individuo.pontuacao += 1

            ## "O homem que tem um gato vive ao lado da casa que fuma Dunhill."
            if i < 4 and i > 0:
                if animais[i] == 3 and cigarros[i+1] == 2 or cigarros[i-1] == 2:
                    print("O homem que tem um gato vive ao lado da casa que fuma Dunhill. ")
                    individuo.pontuacao += 1

            ## "O homem que fuma Blue Master bebe cerveja."
            if cigarros[i] == 5 and bebidas[i] == 4:
                print("O homem que fuma Blue Master bebe cerveja. ")
                individuo.pontuacao += 1

            ## "O homem que vive na casa do centro bebe leite."
            if i == 2 and bebidas[i] == 3:
                print("O homem que vive na casa do centro bebe leite. ")
                individuo.pontuacao += 1

        print("O individuo pontuou: ", individuo.pontuacao)

        return individuo.pontuacao

''' 
            cor:[3,4,1,2,5],
            nacionalidade:[4,3,1,5,2],
            bebida:[1,5,3,2,4],
            cigarro: [2,3,1,4,5], 
            animal:[3,4,1,5,2]}

             Cor pode ser vermelho, verde, amarelo, azul, branco
class CorCasas(Enum):
    Vermelho = 1
    Verde = 2
    Amarelo = 3
    Azul = 4
    Branco = 5



# Nacionalidade pode ser ingles, sueco, dinamarquês, norueguês, alemão
class Nacionalidades(Enum):
    Ingles = 1
    Sueco = 2
    Dinamarquês = 3
    Norueguês = 4
    Alemão = 5



# Bebida pode ser água, café, leite, cerveja, chá
class Bebidas(Enum):
    Agua = 1
    Cafe = 2
    Leite = 3
    Cerveja = 4
    Cha = 5



# Cigarro pode ser pall mall, dunhill, blends, prince, blue master
class Cigarro(Enum):
    PallMall = 1
    Dunhill = 2
    Blends = 3
    Prince = 4
    BlueMaster = 5



# Animal pode ser pássaro, cachorro, gato, cavalo, peixe
class Animais(Enum):
    Passaro = 1
    Cachorro = 2
    Gato = 3
    Cavalo = 4
    Peixe = 5

'''
