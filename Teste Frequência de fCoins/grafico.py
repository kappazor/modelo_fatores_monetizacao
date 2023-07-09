# Universidade de Brasília
# Departamento de Ciência da Computação
# TCC
# Rodrigo da Silva Navarro - 15/0147376
# Código do Modelo Completo de um Jogo Gacha
# Teste Frequência fCoins
#
#
import matplotlib.pyplot as plt
import numpy as np

# import dos arquivos python deste projeto
import c1fcoin as c1
import c2fcoin as c2
import c3fcoin as c3
import c5fcoin as c5
import c10fcoin as c10


c1.f_lista()
c2.f_lista()
c3.f_lista()
c5.f_lista()
c10.f_lista()


def graph():
    # largura das barras
    w = 0.3
    # número de fcoin por nível para cada barra no eixo X
    x = ["1", "2", "3", "5", "10"]

    yer1 = [c1.f_erro(), c2.f_erro(), c3.f_erro(), c5.f_erro(), c10.f_erro()]

    completo = [c1.f_media(), c2.f_media(), c3.f_media(), c5.f_media(), c10.f_media()]

    bar1 = np.arange(len(x))

    plt.bar(bar1, completo, w, color='blue', edgecolor='black', yerr=yer1, capsize=3, label="Modelo Híbrido")

    plt.xlabel("Intervalo de níveis entre recompensa de fCoins")
    plt.ylabel("Game Over")
    plt.title("Jogador F2P")
    plt.xticks(bar1, x)
    plt.legend()
    plt.show()


graph()
