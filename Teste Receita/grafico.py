# Universidade de Brasília
# Departamento de Ciência da Computação
# TCC
# Rodrigo da Silva Navarro - 15/0147376
# Código da Simulação de Receita de um Jogo Gacha
#
#
#
import matplotlib.pyplot as plt
import numpy as np

import dados_basico as db
import dados_completo as dc

db.receita_total()
dc.receita_total()


def graph():
    w = 0.03
    x = ["3"]

    basico = db.f_media()/1000000
    completo = dc.f_media()/1000000

    yer1 = db.f_erro()/1000000
    yer2 = dc.f_erro()/1000000

    bar1 = np.arange(len(x))
    bar2 = [i + w for i in bar1]

    plt.bar(bar1, basico, width=w, color='green', edgecolor='black', yerr=yer1, capsize=7, label='Modelo Base')
    plt.bar(bar2, completo, width=w, color='blue', edgecolor='black', yerr=yer2, capsize=7, label='Modelo Híbrido')

    plt.xlabel("Valor de cada pCoin  (em reais)")
    plt.ylabel("Receita Total Gerada (em milhões de reais)")
    plt.title("Simulação de Receita com 10M de Jogadores")
    plt.xticks(bar1 + w / 2, x)
    plt.legend()
    plt.show()


graph()
# print(db.receita_total())
# print(dc.receita_total())
