from Model.Solucao import Solucao
from Controllers.SolucaoController import SolucaoController
import time


class Main:
    def __init__(self):
        inicio = time.time()
        # SolucaoController.gerarSolucaoAleatoria();
        # SolucaoController.criarGeracao(2000); #o argumento é a quantidade de individuos que vai ter na geracao
        SolucaoController.run(10000, 10000); #o argumento é a quantidade de individuos que vai ter na geracao
        fim = time.time()
        print(fim - inicio, "segundos")


if __name__ == "__main__":
    Main()
