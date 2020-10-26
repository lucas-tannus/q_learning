from Constants import *


class Estado(object):

    def __init__(self, posicao, final=False, tipo=CAMINHO):
        self.tipo = tipo
        self.posicao = posicao
        self.final = final

    def get_recompensa(self):
        return RECOMPENSAS.get(self.tipo)

    def set_estado_final(self):
        self.final = True

    def get_tipo(self):
        return self.tipo

    def get_final(self):
        return self.final
