from Constants import QUANTIDADE_EPOCAS, E_NUMBER
from random import random
from time import time


class QLearning(object):

    def __init__(self, agente, taxa):
        self.agente = agente
        self.taxa = taxa

    def jogar(self):
        print("Play...")
        movimentos = []
        self.agente.set_inicio()
        movimentos.append(str(self.agente.get_estado_atual()))
        while True:
            self.agente.andar()
            movimentos.append(str(self.agente.get_estado_atual()))
            if self.agente.estado_final():
                break

        print(' -> '.join(movimentos))

    def aprender(self):
        tempos = []
        inicio = time()
        for epoca in range(QUANTIDADE_EPOCAS):
            while True:
                estado_anterior = self.agente.get_estado_atual()
                acao = self.epsilon_greedy(self.taxa)
                self.agente.atualiza_estado_atual(acao)
                self.agente.atualiza_tabela(estado_anterior, acao)
                if self.agente.estado_final():
                    fim = time()
                    tempos.append(round((fim - inicio), 3))
                    break
        print('({taxa},{media})'.format(taxa=self.taxa, media=sum(tempos)/len(tempos)))

    def epsilon_greedy(self, number):
        numero_aleatorio = random()
        if numero_aleatorio < number:
            acao = self.agente.get_acao_aleatoria()
        else:
            acao = self.agente.get_acao_maxima()
        return acao
