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

from padrao5_normal import padrao5normal
from proposto5_normal import proposto5normal
from padrao10_normal import padrao10normal
from proposto10_normal import proposto10normal
from padrao25_normal import padrao25normal
from proposto25_normal import proposto25normal
from padrao50_normal import padrao50normal
from proposto50_normal import proposto50normal


def graph():
    w = 0.3
    x = ["5", "10", "25", "50"]
    padrão = [padrao5normal(), padrao10normal(), padrao25normal(), padrao50normal()]
    proposto = [proposto5normal(), proposto10normal(), proposto25normal(), proposto50normal()]

    bar1 = np.arange(len(x))
    bar2 = [i + w for i in bar1]

    plt.bar(bar1, padrão, w, label="Modelo Padrão")
    plt.bar(bar2, proposto, w, label="Modelo Proposto")

    plt.xlabel("Qtd Total de Níveis")
    plt.ylabel("Game Over")
    plt.title("Jogadores Normais")
    plt.xticks(bar1 + w / 2, x)
    plt.legend()
    plt.show()


graph()
