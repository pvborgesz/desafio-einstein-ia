from Model.Solucao import Solucao
from Controllers.SolucaoController import SolucaoController
import time


class Main:
    def __init__(self):
        inicio = time.time()
        
        popInicial = 10000
        numGeracoes = 1000

        SolucaoController.run(popInicial, numGeracoes)
        
        fim = time.time()
        print(fim - inicio, "segundos")


if __name__ == "__main__":
    Main()
