from Mapa import Mapa
from Agente import Agente
from QLearning import QLearning
from numpy import arange


def main():
    mapa = Mapa()
    for taxa in arange(0.03, 1, 0.03):
        agente = Agente(mapa)
        QLearning(agente, taxa).aprender()


if __name__ == "__main__":
    main()
