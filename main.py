from Model.Solucao import Solucao
from Controllers.SolucaoController import SolucaoController
class Main:
    def __init__(self):
        # SolucaoController.gerarSolucaoAleatoria();
        SolucaoController.criarGeracao(1000000); #o argumento é a quantidade de individuos que vai ter na geracao


if __name__ == "__main__":
    Main()
