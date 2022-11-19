from enum import Enum
from Model.Solucao import Solucao
from Model.Individuo import Individuo

class Regras(Enum):
    "O Norueguês vive na primeira casa."
    "O Inglês mora na casa vermelha."
    "O Sueco tem Cachorros como animais de estimação."
    "O Dinamarquês bebe chá."
    "A casa verde está imediatamente à esquerda da casa branca."
    "O dono da casa verde bebe café."
    "A pessoa que fuma Pall Mall cria pássaros."
    "O dono da casa amarela fuma Dunhill."
    "O homem que vive na casa do centro bebe leite."
    "O alemão fuma Prince."
    "O norueguês vive ao lado da casa azul."
    "O homem que fuma Blends tem um vizinho que bebe água."
    "O homem que tem um gato vive ao lado da casa que fuma Dunhill."
    "O homem que fuma Blue Master bebe cerveja."

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

# Cor pode ser vermelho, verde, amarelo, azul, branco
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

# deixar aqui por enquanto
def fitness():

    ## "O Norueguês vive na primeira casa."
    if (Nacionalidades(Solucao.getNacionalidade()[0]).value == 4):
        Individuo.addPonto()

    ## "O Inglês mora na casa vermelha."
    for nacionalidades in Solucao.getNacionalidade():
        if (Nacionalidades(nacionalidades).value == 1):
            casa = Solucao.getNacionalidade().index(nacionalidades)
            if (Nacionalidades(Solucao.getCorCasa()[casa]).value == 2):
                Individuo.addPonto()

    ## "O Sueco tem Cachorros como animais de estimação."
    for nacionalidades in Solucao.getNacionalidade():
        if (Nacionalidades(nacionalidades).value == 2):
            casa = Solucao.getNacionalidade().index(nacionalidades)
            if (Animais(Solucao.getCorCasa()[casa]).value == 2):
                Individuo.addPonto()                

    ## "O Dinamarquês bebe chá."
    for nacionalidades in Solucao.getNacionalidade():
        if (Nacionalidades(nacionalidades).value == 3):
            casa = Solucao.getNacionalidade().index(nacionalidades)
            if (Bebidas(Solucao.getCorCasa()[casa]).value == 5):
                Individuo.addPonto()

    ## "A casa verde está imediatamente à esquerda da casa branca."
    for cores in Solucao.getCorCasa():
        if (CorCasas(cores).value == 2):
            casa = Solucao.getCorCasa().index(cores)
            if (casa != 4):
                if (CorCasas(casa+1).value == 5):
                    Individuo.addPonto()

    ## "O dono da casa verde bebe café."
    for cores in Solucao.getCorCasa():
        if (CorCasas(cores).value == 2):
            casa = Solucao.getCorCasa().index(cores)
            if (Bebidas(Solucao.getCorCasa()[casa]).value == 2):
                Individuo.addPonto()

    ## "A pessoa que fuma Pall Mall cria pássaros."
    for cigarros in Solucao.getCigarro():
        if (Cigarro(cigarros).value == 1):
            casa = Solucao.getCigarro().index(cigarros)
            if (Animais(Solucao.getBebida()[casa]).value == 1):
                Individuo.addPonto()
    ## "O dono da casa amarela fuma Dunhill."
    for cores in Solucao.getCigarro():
        if (CorCasas(cores).value == 3):
            casa = Solucao.getCorCasa().index(cores)
            if (Cigarro(Solucao.getCigarro()[casa]).value == 2):
                Individuo.addPonto()

    ## "O homem que vive na casa do centro bebe leite."
    if (Bebidas(Solucao.getBebida()[2]).value == 3):
        Individuo.addPonto()

    ## "O alemão fuma Prince."
    for nacionalidades in Solucao.getNacionalidade():
        if (Nacionalidades(nacionalidades).value == 5):
            casa = Solucao.getNacionalidade().index(nacionalidades)
            if (Cigarro(Solucao.getCigarro()[casa]).value == 4):
                Individuo.addPonto()

    ## "O norueguês vive ao lado da casa azul."
    for nacionalidades in Solucao.getNacionalidade():
        if (Nacionalidades(nacionalidades).value == 4):
            casa = Solucao.getNacionalidade().index(cigarros)
            if (casa == 0):
                if (CorCasas(Solucao.getCorCasa()[casa+1]).value == 4):
                    Individuo.addPonto()
            elif (casa == 4):
                if (CorCasas(Solucao.getCorCasa()[casa-1]).value == 4):
                    Individuo.addPonto()

    ## "O homem que fuma Blends tem um vizinho que bebe água."
    for cigarros in Solucao.getCigarro():
        if (Cigarro(cigarros).value == 3):
            casa = Solucao.getCigarro().index(cigarros)
            if (casa == 0):
                if (CorCasas(Solucao.getBebida()[casa+1]).value == 1):
                    Individuo.addPonto()
            elif (casa == 4):
                if (CorCasas(Solucao.getBebida()[casa-1]).value == 1):
                    Individuo.addPonto()

    ## "O homem que tem um gato vive ao lado da casa que fuma Dunhill."
    for animais in Solucao.getAnimal():
        if (Animais(animais).value == 3):
            casa = Solucao.getAnimal().index(animais)
            if (casa == 0):
                if (Cigarro(Solucao.getCigarro()[casa+1]).value == 2):
                    Individuo.addPonto()
            elif (casa == 4):
                if (Cigarro(Solucao.getCigarro()[casa-1]).value == 2):
                    Individuo.addPonto()

    ## "O homem que fuma Blue Master bebe cerveja."
    for cigarros in Solucao.getNacionalidade():
        if (Cigarro(cigarros).value == 5):
            casa = Solucao.getNacionalidade().index(cigarros)
            if (Cigarro(Solucao.getCigarro()[casa]).value == 4):
                Individuo.addPonto()