# Universidade de Brasília
# Departamento de Ciência da Computação
# TCC
# Rodrigo da Silva Navarro - 15/0147376
# Código da Simulação de Receita de um Jogo Gacha
#
#
# Divisão da população:
# - 95% são jogadores F2P
# - 4.5% são jogadores Normais (dolphins/willows)
# - 0.5% são jogadores P2W (whales)

import random
import statistics

# para o cálculo de receita, ignoramos TODOS os jogadores F2P (95% da playerbase)
#
# número total de jogadores (playerbase)
pb = 10000000

# valor, em reais, do serviço comprado com hard currency (pCoins)
v = 3

# lista que guardará a quantidade de pCoins usada por um Jogador P2W em cada run
r_total = []

# lista do desvio padrão
r_total_dp = []

# constante de 99% confiabilidade
z = 2.58


def receita_normal():
    # número total de jogadores dolhpins (Perfil Normal) (4,5% da playerbase)
    n_normal = pb * 0.045

    # número de pCoins adquiridas pelo Jogador Normal
    pCoin_normal = 10

    # receita do Jogador Normal é igual ao número de jogadores normais vezes a quantidade de pCoins consumidas
    # vezes o valor de cada pCoin
    r_normal = n_normal * pCoin_normal * v
    # print("Receita dos dolphins: R$ " + str(r_normal))

    return r_normal


def receita_total():
    # número total de jogadores P2W (0,5% da playerbase)
    n_p2w = int(pb * 0.005)

    # número de pCoins adquiridas pelo Jogador P2W
    pCoin_p2w = 0

    # a função retornará uma média de 50 execuções só para garantir que o valor gerado não é incomum
    for y in range(50):
        total_pCoin_p2w = 0
        for x in range(n_p2w):
            # quantidade de pCoins adquiridas na run x
            quant = random.randint(15, 23)
            # valor pago por pCoins na run x
            pCoin_p2w = v * quant
            total_pCoin_p2w = total_pCoin_p2w + pCoin_p2w

        # receita total de um jogador P2W na run x
        r_total.append(total_pCoin_p2w + receita_normal())

        # print("Receita dos whales: R$ " + str(r_total))

    return r_total


def f_media():
    media = round(statistics.mean(r_total), 2)
    return media


def f_dp():
    for r in r_total:
        r_total_dp.append((r - f_media()) ** 2)

    media_dp = round(statistics.mean(r_total_dp), 2)
    dp = round((media_dp ** (1/2)), 2)
    return dp


def f_ic_superior():
    x = f_media()
    o = f_dp()
    n = len(r_total)
    lim_superior = round(x + z * (o / (n ** (1/2))), 2)
    return lim_superior


def f_ic_inferior():
    x = f_media()
    o = f_dp()
    n = len(r_total)
    lim_inferior = round(x - z * (o / (n ** (1/2))), 2)
    return lim_inferior


def f_erro():
    erro = round(f_ic_superior() - f_media())
    return erro
