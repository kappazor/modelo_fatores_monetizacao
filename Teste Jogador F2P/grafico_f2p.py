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

from padrao5_f2p import padrao5f2p
from proposto5_f2p import proposto5f2p
from padrao10_f2p import padrao10f2p
from proposto10_f2p import proposto10f2p
from padrao25_f2p import padrao25f2p
from proposto25_f2p import proposto25f2p
from padrao50_f2p import padrao50f2p
from proposto50_f2p import proposto50f2p


def graph():
    w = 0.3
    x = ["5", "10", "25", "50"]
    padrão = [padrao5f2p(), padrao10f2p(), padrao25f2p(), padrao50f2p()]
    proposto = [proposto5f2p(), proposto10f2p(), proposto25f2p(), proposto50f2p()]

    bar1 = np.arange(len(x))
    bar2 = [i + w for i in bar1]

    plt.bar(bar1, padrão, w, label="Modelo Padrão")
    plt.bar(bar2, proposto, w, label="Modelo Proposto")

    plt.xlabel("Qtd Total de Níveis")
    plt.ylabel("Game Over")
    plt.title("Jogadores F2P")
    plt.xticks(bar1 + w / 2, x)
    plt.legend()
    plt.show()


graph()
