"""
    Definindo alguns conceitos:
        - estado: é um número de 0 à 24, descrevendo o mapa (matriz) de forma linear.
        - acao: é definida como baixo, cima, direita e esquerda. Uma ação está restrita ao limite
        do mapa, ou seja, qualquer valar fora de [0, 24] não é uma ação permitida. Além disso,
        as paredes não permitem a execução de uma ação apesar do estado estar dentro do limite
        do mapa.
        - tabela_q: é uma matriz (estado x acao) que armazena os valores da função Q(s,a), tal
        que 's' é o estado atual e 'a' é uma ação. Para movimentos que não são possíveis para um
        estado 's' qualquer definiremos Q(s,a) como None. Matriz dos valores da função ação-valor
        para cada estado e ação.
        - posicao_atual: é um número de 0 à 24 que diz em qual local do mapa o agente está no
        momento atual.
"""
from Constants import *
from random import randint
import numpy as np


class Agente(object):

    def __init__(self, mapa):
        self.tabela_q = np.zeros([ESTADO_MAX, len(ACOES)], dtype=np.float64)
        self.mapa = mapa
        self.posicao_atual = POSICAO_INICIAL
        self.set_acoes_indisponiveis()

    def set_inicio(self):
        self.posicao_atual = POSICAO_INICIAL

    def andar(self):
        acao = self.get_acao_maxima()
        self.posicao_atual += ACOES_MOVIMENTOS.get(acao)

    def print_tabela_q(self):
        print("TABELA Q: \n{0}".format(self.tabela_q))

    def get_estado_atual(self):
        return self.posicao_atual

    def busca_valor(self, estado, acao):
        q = self.tabela_q[estado][TABELA_ACOES[acao]]
        return q

    def busca_valor_maximo(self, estado):
        return np.amax(self.tabela_q, axis=1)[estado]

    def atualiza_tabela(self, estado_anterior, acao):
        self.tabela_q[estado_anterior][TABELA_ACOES[acao]] = round(self.tabela_q[estado_anterior][TABELA_ACOES[acao]] + TAXA_APRENDIZADO * (self.busca_recompensa(self.posicao_atual) + FATOR_DESCONTO * self.busca_valor_maximo(self.posicao_atual) - self.tabela_q[estado_anterior][TABELA_ACOES[acao]]), 4)

    def atualiza_estado_atual(self, acao):
        self.posicao_atual += ACOES_MOVIMENTOS[acao]
        return self.posicao_atual

    def busca_recompensa(self, estado):
        return self.mapa.get_recompensa(estado)

    def get_acao_aleatoria(self):
        while True:
            acao_aleatoria = randint(0, len(ACOES) - 1)
            acoes = self.mapa.buscar_acoes(self.posicao_atual)
            if ACOES[acao_aleatoria] in acoes:
                break
        return ACOES[acao_aleatoria]

    def get_acao_maxima(self):
        acao = np.argmax(self.tabela_q, axis=1)[self.posicao_atual]
        return ACOES[acao]

    def set_acoes_indisponiveis(self):
        for estado in range(ESTADO_MAX):
            acoes = self.mapa.buscar_acoes(estado)
            for acao in range(len(ACOES)):
                if ACOES[acao] not in acoes:
                    self.tabela_q[estado][acao] = -float("inf")

    def estado_final(self):
        return self.mapa.eh_final(self.posicao_atual)
