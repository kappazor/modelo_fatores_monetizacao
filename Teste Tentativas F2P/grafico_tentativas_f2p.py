# Universidade de Brasília
# Departamento de Ciência da Computação
# TCC
# Rodrigo da Silva Navarro - 15/0147376
# Teste de Variadas Tentativas para o Jogador F2P
#
#
#
import matplotlib.pyplot as plt
import numpy as np

# import dos arquivos para o modelo base
import basico1tentativa_f2p as b1
import basico2tentativas_f2p as b2
import basico3tentativas_f2p as b3
import basico10tentativas_f2p as b10
import basico20tentativas_f2p as b20

# import dos arquivos para o modelo hibrido
import completo1tentativa_f2p as c1
import completo2tentativas_f2p as c2
import completo3tentativas_f2p as c3
import completo10tentativas_f2p as c10
import completo20tentativas_f2p as c20

# chamada das funções que geram a lista
b1.f_lista()
b2.f_lista()
b3.f_lista()
b10.f_lista()
b20.f_lista()

c1.f_lista()
c2.f_lista()
c3.f_lista()
c10.f_lista()
c20.f_lista()


def graph():
    # largura das barras
    w = 0.3
    # quantidade de tentativas por nível em cada valor do eixo X
    x = ["1", "2", "3", "10", "20"]

    # valores das médias de nível de Game Over
    basico = [b1.f_media(), b2.f_media(), b3.f_media(), b10.f_media(), b20.f_media()]
    completo = [c1.f_media(), c2.f_media(), c3.f_media(), c10.f_media(),
                c20.f_media()]

    # intervalo de confiança para 99% de confiabilidade
    yer1 = [b1.f_erro(), b2.f_erro(), b3.f_erro(), b10.f_erro(), b20.f_erro()]
    yer2 = [c1.f_erro(), c2.f_erro(), c3.f_erro(), c10.f_erro(), c20.f_erro()]

    bar1 = np.arange(len(x))
    bar2 = [i + w for i in bar1]

    plt.bar(bar1, basico, width=w, color='green', edgecolor='black', yerr=yer1, capsize=3, label="Modelo Base")
    plt.bar(bar2, completo, width=w, color='blue', edgecolor='black', yerr=yer2, capsize=3, label="Modelo Híbrido")

    plt.xlabel("Número de Tentativas por Nível")
    plt.ylabel("Game Over")
    plt.title("Jogador F2P")
    plt.xticks(bar1 + w / 2, x)
    plt.legend()
    plt.show()


# print(c1.f_erro())
# print(c1.f_media())
# print(c1.f_ic_inferior())
# print(c1.f_ic_superior())
graph()
