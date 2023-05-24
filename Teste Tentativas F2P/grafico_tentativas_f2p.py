# Universidade de Brasília
# Departamento de Ciência da Computação
# TCC
# Rodrigo da Silva Navarro - 15/0147376
# Código do Modelo Padrão de um Jogo Gacha
#
#
#
import matplotlib.pyplot as plt
import numpy as np

from padrao1tentativa_f2p import padrao1f2p
from proposto1tentativa_f2p import proposto1f2p
from padrao2tentativas_f2p import padrao2f2p
from proposto2tentativas_f2p import proposto2f2p
from padrao3tentativas_f2p import padrao3f2p
from proposto3tentativas_f2p import proposto3f2p
from padrao10tentativas_f2p import padrao10tentativasf2p
from proposto10tentativas_f2p import proposto10tentativasf2p
from padrao20tentativas_f2p import padrao20tentativasf2p
from proposto20tentativas_f2p import proposto20tentativasf2p


def graph():
    w = 0.3
    x = ["1", "2", "3", "...", "10", "...", "20"]
    padrão = [padrao1f2p(), padrao2f2p(), padrao3f2p(), 0, padrao10tentativasf2p(), 0, padrao20tentativasf2p()]
    proposto = [proposto1f2p(), proposto2f2p(), proposto3f2p(), 0, proposto10tentativasf2p(), 0, proposto20tentativasf2p()]

    bar1 = np.arange(len(x))
    bar2 = [i + w for i in bar1]

    plt.bar(bar1, padrão, w, label="Modelo Padrão")
    plt.bar(bar2, proposto, w, label="Modelo Proposto")

    plt.xlabel("Número de Tentativas por Nível")
    plt.ylabel("Game Over")
    plt.title("Jogador Normal")
    plt.xticks(bar1 + w / 2, x)
    plt.legend()
    plt.show()

graph()
