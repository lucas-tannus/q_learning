RECOMPENSAS = {
    "caminho": 0,
    "lava": -3,
    "monstro": -1,
    "portal": 1
}

CAMINHO = "caminho"
LAVA = "lava"
MONSTRO = "monstro"
PAREDE = "parede"
PORTAL = "portal"

TABELA_ACOES = {
    "cima": 0,
    "baixo": 1,
    "esquerda": 2,
    "direita": 3
}

ACOES_MOVIMENTOS = {
    "cima": -5,
    "baixo": 5,
    "esquerda": -1,
    "direita": 1,
}

ACOES = [
    "cima",
    "baixo",
    "esquerda",
    "direita"
]

PAREDES = []
MONSTROS = [7, 8, 11, 18, 19, 21]
LAVAS = []
ESTADOS_FINAIS = [24]
TAXA_APRENDIZADO = 0.2
FATOR_DESCONTO = 0.9
ESTADO_MAX = 25
QUANTIDADE_EPOCAS = 100000
E_NUMBER = 0.8
POSICAO_INICIAL = 6
