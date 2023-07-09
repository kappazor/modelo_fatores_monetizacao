# Universidade de Brasília
# Departamento de Ciência da Computação
# TCC
# Rodrigo da Silva Navarro - 15/0147376
# Código do Teste de Qtd. Níveis para Jogador Normal
#
#
#
import matplotlib.pyplot as plt
import numpy as np

# import dos arquivos.py do projeto
import basico5_normal as b5f2p
import completo5_normal as c5f2p
import basico10_normal as b10f2p
import completo10_normal as c10f2p
import basico25_normal as b25f2p
import completo25_normal as c25f2p
import basico50_normal as b50f2p
import completo50_normal as c50f2p

# chamada das funções que geram a lista para cada nível, do Modelo Básico e do Completo
b5f2p.basico5f2p_lista()
c5f2p.completo5f2p_lista()
b10f2p.basico10f2p_lista()
c10f2p.completo10f2p_lista()
b25f2p.basico25f2p_lista()
c25f2p.completo25f2p_lista()
b50f2p.basico50f2p_lista()
c50f2p.completo50f2p_lista()


def graph():
    # largura da barra
    w = 0.3
    # quantidade de niveis para cada conjunto de barras
    x = ["5", "10", "25", "50"]

    # valores das médias
    básico = [b5f2p.basico5f2p_media(), b10f2p.basico10f2p_media(), b25f2p.basico25f2p_media(), b50f2p.basico50f2p_media()]
    completo = [c5f2p.completo5f2p_media(), c10f2p.completo10f2p_media(), c25f2p.completo25f2p_media(), c50f2p.completo50f2p_media()]

    # intervalo de confiança para 99% de confiabilidade
    yer1 = [b5f2p.basico5f2p_erro(), b10f2p.basico10f2p_erro(), b25f2p.basico25f2p_erro(), b50f2p.basico50f2p_erro()]
    yer2 = [c5f2p.completo5f2p_erro(), c10f2p.completo10f2p_erro(), c25f2p.completo25f2p_erro(), c50f2p.completo50f2p_erro()]

    bar1 = np.arange(len(x))
    bar2 = [i + w for i in bar1]

    # configurações das barras
    plt.bar(bar1, básico, w, color='green', edgecolor='black', yerr=yer1, capsize=3, label="Modelo Base")
    plt.bar(bar2, completo, w, color='blue', edgecolor='black', yerr=yer2, capsize=3, label="Modelo Híbrido")

    plt.xlabel("Qtd Total de Níveis")
    plt.ylabel("Game Over")
    plt.title("Jogador Normal")
    plt.xticks(bar1 + w / 2, x)
    plt.legend()
    plt.show()


graph()
