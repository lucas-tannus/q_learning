from Constants import *
from Estado import Estado
from Utils import calcula_coluna, calcula_linha
from math import sqrt


def pode_ir_para_direita(posicao):
    if posicao is 0:
        return True
    qtd_colunas = int(sqrt(ESTADO_MAX))
    linha = calcula_linha(posicao, qtd_colunas)
    coluna = calcula_coluna(linha, posicao, qtd_colunas)
    return not(coluna is qtd_colunas - 1) if linha is 0 else not((linha + 1) * (coluna + 1) % posicao is 1)


def pode_ir_para_esquerda(posicao):
    return not(posicao % int(sqrt(ESTADO_MAX)) is 0)


class Mapa(object):

    def __init__(self):
        self.mapa = []
        for index in range(ESTADO_MAX):
            if index in PAREDES:
                self.mapa.append(Estado(posicao=index, tipo=PAREDE))
            elif index in MONSTROS:
                self.mapa.append(Estado(posicao=index, tipo=MONSTRO))
            elif index in LAVAS:
                self.mapa.append(Estado(posicao=index, tipo=LAVA))
            elif index in ESTADOS_FINAIS:
                self.mapa.append(Estado(posicao=index, tipo=PORTAL))
            else:
                self.mapa.append(Estado(posicao=index))
        self.set_estados_finais()

    def print_map(self):
        print("{0} {1} \n {2} {3}\n".format(self.mapa[0].get_tipo(), self.mapa[1].get_tipo(), self.mapa[2].get_tipo(), self.mapa[3].get_tipo()))
        print("{0} {1} \n {2} {3}\n".format(self.mapa[0].get_final(), self.mapa[1].get_final(), self.mapa[2].get_final(), self.mapa[3].get_final()))
        print("{0} {1} \n {2} {3}\n".format(self.mapa[0].get_recompensa(), self.mapa[1].get_recompensa(), self.mapa[2].get_recompensa(), self.mapa[3].get_recompensa()))
        
    def eh_parede(self, estado):
        return self.mapa[estado].get_tipo() is PAREDE

    def eh_estado_permitido(self, posicao):
        return (0 <= posicao < ESTADO_MAX) and not self.eh_parede(posicao)

    def get_recompensa(self, estado):
        return self.mapa[estado].get_recompensa()

    def buscar_acoes(self, posicao):
        acoes = []
        if self.eh_estado_permitido(posicao + ACOES_MOVIMENTOS.get("cima")):
            acoes.append("cima")
        if self.eh_estado_permitido(posicao + ACOES_MOVIMENTOS.get("baixo")):
            acoes.append("baixo")
        if self.eh_estado_permitido(posicao + ACOES_MOVIMENTOS.get("direita")) and pode_ir_para_direita(posicao):
            acoes.append("direita")
        if self.eh_estado_permitido(posicao + ACOES_MOVIMENTOS.get("esquerda")) and pode_ir_para_esquerda(posicao):
            acoes.append("esquerda")

        return acoes

    def eh_final(self, posicao):
        return self.mapa[posicao].get_final()

    def set_estados_finais(self):
        for estado in ESTADOS_FINAIS:
            self.mapa[estado].set_estado_final()
