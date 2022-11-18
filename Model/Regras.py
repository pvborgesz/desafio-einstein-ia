from enum import Enum
from Model.Solucao import Solucao
from Model.Individuo import Individuo

class Regras(Enum):
    "O Norueguês vive na primeira casa."
    "O Inglês mora na casa vermelha."
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

def fitness():
    
    ## deixar aqui por enquanto
    ## 1 noruegues na casa 1

    if (Nacionalidades(Solucao.getNacionalidade()[0]).name == 4):
        Individuo.addPonto()

    ## inglês na casa vermelha
    if 