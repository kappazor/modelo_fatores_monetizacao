# Universidade de Brasília
# Departamento de Ciência da Computação
# TCC
# Rodrigo da Silva Navarro - 15/0147376
# Código do Modelo Base de um Jogo Gacha
#
#
#
# usaremos apenas estas duas bibliotecas:
#     - random para gerar uma variável aleatória uniforme com a função 'uniform';
#     - statistics para calcular a média dos elementos presentes no array 'mortes'
import random
import statistics

# lista que guardará o nível de game over em cada run, ou seja,
# para  5000 runs, teremos uma lista de 5000 elementos
mortes = []

# lista para o cálculo do desvio padrão
mortes_dp = []

# constante de confiabilidade (90% = 1.645; 95% = 1.96)
z = 2.58


def basico25f2p_lista():

    # número de simulações (runs)
    for x in range(5000):
        # a cada run, o jogo é resetado, ou seja, o nivel volta para 1 e a quantidade de
        # soft e hard currency volta ao padrão do tipo de jogador que está sendo simulado
        nivel = 1
        pCoins = 5
        fCoins = 0
        if nivel == 1:
            # cada nível terá 2 tentativas para pular para o próximo nível
            for tentativa in range(2):
                # usamos a função uniform da biblioteca random para gerar um número entre 0 e 1
                # upar2 limita esse número a duas casas decimais
                # upar3 transforma esse número para o tipo float
                upar = random.uniform(0, 1)
                upar2 = "{:.2f}".format(upar)
                upar3 = float(upar2)

                # se upar3 for menor que a chance de pular para o próximo nivel, incrementa nível e quebra o loop
                if upar3 < 0.96:
                    nivel = nivel + 1
                    break
                # se a carteira de soft currency (fCoins) for maior que zero, decrementa a carteira e aumenta
                # 25% de chance à variável upar3, que foi gerada no início da tentativa
                #
                # caso essa nova chance aumentada (free_chance) satisfaça o requisito para pular para o próximo
                # nível, incrementa o nível e quebra o loop
                elif fCoins > 0:
                    fCoins = fCoins - 1
                    free_chance = upar3 - 0.25
                    if free_chance < 0.96:
                        nivel = nivel + 1
                        break
                # se a carteira de hard currency (pCoins) for maior que zero, decrementa a carteira e aumenta
                # 70% de chance à variável upar3, que foi gerada no início da tentativa
                #
                # caso essa nova chance aumentada (paid_chance) satisfaça o requisito para pular para o próximo
                # nível, incrementa o nível e quebra o loop
                elif pCoins > 0:
                    pCoins = pCoins - 1
                    paid_chance = upar3 - 0.7
                    if paid_chance < 0.96:
                        nivel = nivel + 1
                        break
                # para entrar neste if, as carteiras de soft e hard currency precisam estar vazias e precisa ter
                # falhado o pulo de nível pela segunda vez. caso isso aconteça, anexa o nível atual no array 'mortes'
                # para indicar em qual nível esta run terminou.
                elif tentativa == 1:
                    # print("game over")
                    mortes.append(nivel)

        if nivel == 2:
            for tentativa in range(2):
                upar = random.uniform(0, 1)
                upar2 = "{:.2f}".format(upar)
                upar3 = float(upar2)
                if upar3 < 0.92:
                    nivel = nivel + 1
                    break
                elif fCoins > 0:
                    fCoins = fCoins - 1
                    free_chance = upar3 - 0.25
                    if free_chance < 0.92:
                        nivel = nivel + 1
                        break
                elif pCoins > 0:
                    pCoins = pCoins - 1
                    paid_chance = upar3 - 0.7
                    if paid_chance < 0.92:
                        nivel = nivel + 1
                        break
                elif tentativa == 1:
                    # print("game over")
                    mortes.append(nivel)

        if nivel == 3:
            for tentativa in range(2):
                upar = random.uniform(0, 1)
                upar2 = "{:.2f}".format(upar)
                upar3 = float(upar2)
                if upar3 < 0.88:
                    nivel = nivel + 1
                    break
                elif fCoins > 0:
                    fCoins = fCoins - 1
                    free_chance = upar3 - 0.25
                    if free_chance < 0.88:
                        nivel = nivel + 1
                        break
                elif pCoins > 0:
                    pCoins = pCoins - 1
                    paid_chance = upar3 - 0.7
                    if paid_chance < 0.88:
                        nivel = nivel + 1
                        break
                elif tentativa == 1:
                    # print("game over")
                    mortes.append(nivel)

        if nivel == 4:
            for tentativa in range(2):
                upar = random.uniform(0, 1)
                upar2 = "{:.2f}".format(upar)
                upar3 = float(upar2)
                if upar3 < 0.84:
                    nivel = nivel + 1
                    break
                elif fCoins > 0:
                    fCoins = fCoins - 1
                    free_chance = upar3 - 0.25
                    if free_chance < 0.84:
                        nivel = nivel + 1
                        break
                elif pCoins > 0:
                    pCoins = pCoins - 1
                    paid_chance = upar3 - 0.7
                    if paid_chance < 0.84:
                        nivel = nivel + 1
                        break
                elif tentativa == 1:
                    # print("game over")
                    mortes.append(nivel)

        if nivel == 5:
            for tentativa in range(2):
                upar = random.uniform(0, 1)
                upar2 = "{:.2f}".format(upar)
                upar3 = float(upar2)
                if upar3 < 0.8:
                    nivel = nivel + 1
                    break
                elif fCoins > 0:
                    fCoins = fCoins - 1
                    free_chance = upar3 - 0.25
                    if free_chance < 0.8:
                        nivel = nivel + 1
                        break
                elif pCoins > 0:
                    pCoins = pCoins - 1
                    paid_chance = upar3 - 0.7
                    if paid_chance < 0.8:
                        nivel = nivel + 1
                        break
                elif tentativa == 1:
                    # print("game over")
                    mortes.append(nivel)

        if nivel == 6:
            for tentativa in range(2):
                upar = random.uniform(0, 1)
                upar2 = "{:.2f}".format(upar)
                upar3 = float(upar2)
                if upar3 < 0.76:
                    nivel = nivel + 1
                    break
                elif fCoins > 0:
                    fCoins = fCoins - 1
                    free_chance = upar3 - 0.25
                    if free_chance < 0.76:
                        nivel = nivel + 1
                        break
                elif pCoins > 0:
                    pCoins = pCoins - 1
                    paid_chance = upar3 - 0.7
                    if paid_chance < 0.76:
                        nivel = nivel + 1
                        break
                elif tentativa == 1:
                    # print("game over")
                    mortes.append(nivel)

        if nivel == 7:
            for tentativa in range(2):
                upar = random.uniform(0, 1)
                upar2 = "{:.2f}".format(upar)
                upar3 = float(upar2)
                if upar3 < 0.72:
                    nivel = nivel + 1
                    break
                elif fCoins > 0:
                    fCoins = fCoins - 1
                    free_chance = upar3 - 0.25
                    if free_chance < 0.72:
                        nivel = nivel + 1
                        break
                elif pCoins > 0:
                    pCoins = pCoins - 1
                    paid_chance = upar3 - 0.7
                    if paid_chance < 0.72:
                        nivel = nivel + 1
                        break
                elif tentativa == 1:
                    # print("game over")
                    mortes.append(nivel)

        if nivel == 8:
            for tentativa in range(2):
                upar = random.uniform(0, 1)
                upar2 = "{:.2f}".format(upar)
                upar3 = float(upar2)
                if upar3 < 0.68:
                    nivel = nivel + 1
                    break
                elif fCoins > 0:
                    fCoins = fCoins - 1
                    free_chance = upar3 - 0.25
                    if free_chance < 0.68:
                        nivel = nivel + 1
                        break
                elif pCoins > 0:
                    pCoins = pCoins - 1
                    paid_chance = upar3 - 0.7
                    if paid_chance < 0.68:
                        nivel = nivel + 1
                        break
                elif tentativa == 1:
                    # print("game over")
                    mortes.append(nivel)

        if nivel == 9:
            for tentativa in range(2):
                upar = random.uniform(0, 1)
                upar2 = "{:.2f}".format(upar)
                upar3 = float(upar2)
                if upar3 < 0.64:
                    nivel = nivel + 1
                    break
                elif fCoins > 0:
                    fCoins = fCoins - 1
                    free_chance = upar3 - 0.25
                    if free_chance < 0.64:
                        nivel = nivel + 1
                        break
                elif pCoins > 0:
                    pCoins = pCoins - 1
                    paid_chance = upar3 - 0.7
                    if paid_chance < 0.64:
                        nivel = nivel + 1
                        break
                elif tentativa == 1:
                    # print("game over")
                    mortes.append(nivel)

        if nivel == 10:
            for tentativa in range(2):
                upar = random.uniform(0, 1)
                upar2 = "{:.2f}".format(upar)
                upar3 = float(upar2)
                if upar3 < 0.6:
                    nivel = nivel + 1
                    break
                elif fCoins > 0:
                    fCoins = fCoins - 1
                    free_chance = upar3 - 0.25
                    if free_chance < 0.6:
                        nivel = nivel + 1
                        break
                elif pCoins > 0:
                    pCoins = pCoins - 1
                    paid_chance = upar3 - 0.7
                    if paid_chance < 0.6:
                        nivel = nivel + 1
                        break
                elif tentativa == 1:
                    # print("game over")
                    mortes.append(nivel)

        if nivel == 11:
            for tentativa in range(2):
                upar = random.uniform(0, 1)
                upar2 = "{:.2f}".format(upar)
                upar3 = float(upar2)
                if upar3 < 0.56:
                    nivel = nivel + 1
                    break
                elif fCoins > 0:
                    fCoins = fCoins - 1
                    free_chance = upar3 - 0.25
                    if free_chance < 0.56:
                        nivel = nivel + 1
                        break
                elif pCoins > 0:
                    pCoins = pCoins - 1
                    paid_chance = upar3 - 0.7
                    if paid_chance < 0.56:
                        nivel = nivel + 1
                        break
                elif tentativa == 1:
                    # print("game over")
                    mortes.append(nivel)

        if nivel == 12:
            for tentativa in range(2):
                upar = random.uniform(0, 1)
                upar2 = "{:.2f}".format(upar)
                upar3 = float(upar2)
                if upar3 < 0.52:
                    nivel = nivel + 1
                    break
                elif fCoins > 0:
                    fCoins = fCoins - 1
                    free_chance = upar3 - 0.25
                    if free_chance < 0.52:
                        nivel = nivel + 1
                        break
                elif pCoins > 0:
                    pCoins = pCoins - 1
                    paid_chance = upar3 - 0.7
                    if paid_chance < 0.52:
                        nivel = nivel + 1
                        break
                elif tentativa == 1:
                    # print("game over")
                    mortes.append(nivel)

        if nivel == 13:
            for tentativa in range(2):
                upar = random.uniform(0, 1)
                upar2 = "{:.2f}".format(upar)
                upar3 = float(upar2)
                if upar3 < 0.48:
                    nivel = nivel + 1
                    break
                elif fCoins > 0:
                    fCoins = fCoins - 1
                    free_chance = upar3 - 0.25
                    if free_chance < 0.48:
                        nivel = nivel + 1
                        break
                elif pCoins > 0:
                    pCoins = pCoins - 1
                    paid_chance = upar3 - 0.7
                    if paid_chance < 0.48:
                        nivel = nivel + 1
                        break
                elif tentativa == 1:
                    # print("game over")
                    mortes.append(nivel)

        if nivel == 14:
            for tentativa in range(2):
                upar = random.uniform(0, 1)
                upar2 = "{:.2f}".format(upar)
                upar3 = float(upar2)
                if upar3 < 0.44:
                    nivel = nivel + 1
                    break
                elif fCoins > 0:
                    fCoins = fCoins - 1
                    free_chance = upar3 - 0.25
                    if free_chance < 0.44:
                        nivel = nivel + 1
                        break
                elif pCoins > 0:
                    pCoins = pCoins - 1
                    paid_chance = upar3 - 0.7
                    if paid_chance < 0.44:
                        nivel = nivel + 1
                        break
                elif tentativa == 1:
                    # print("game over")
                    mortes.append(nivel)

        if nivel == 15:
            for tentativa in range(2):
                upar = random.uniform(0, 1)
                upar2 = "{:.2f}".format(upar)
                upar3 = float(upar2)
                if upar3 < 0.4:
                    nivel = nivel + 1
                    break
                elif fCoins > 0:
                    fCoins = fCoins - 1
                    free_chance = upar3 - 0.25
                    if free_chance < 0.4:
                        nivel = nivel + 1
                        break
                elif pCoins > 0:
                    pCoins = pCoins - 1
                    paid_chance = upar3 - 0.7
                    if paid_chance < 0.4:
                        nivel = nivel + 1
                        break
                elif tentativa == 1:
                    # print("game over")
                    mortes.append(nivel)

        if nivel == 16:
            for tentativa in range(2):
                upar = random.uniform(0, 1)
                upar2 = "{:.2f}".format(upar)
                upar3 = float(upar2)
                if upar3 < 0.36:
                    nivel = nivel + 1
                    break
                elif fCoins > 0:
                    fCoins = fCoins - 1
                    free_chance = upar3 - 0.25
                    if free_chance < 0.36:
                        nivel = nivel + 1
                        break
                elif pCoins > 0:
                    pCoins = pCoins - 1
                    paid_chance = upar3 - 0.7
                    if paid_chance < 0.36:
                        nivel = nivel + 1
                        break
                elif tentativa == 1:
                    # print("game over")
                    mortes.append(nivel)

        if nivel == 17:
            for tentativa in range(2):
                upar = random.uniform(0, 1)
                upar2 = "{:.2f}".format(upar)
                upar3 = float(upar2)
                if upar3 < 0.32:
                    nivel = nivel + 1
                    break
                elif fCoins > 0:
                    fCoins = fCoins - 1
                    free_chance = upar3 - 0.25
                    if free_chance < 0.32:
                        nivel = nivel + 1
                        break
                elif pCoins > 0:
                    pCoins = pCoins - 1
                    paid_chance = upar3 - 0.7
                    if paid_chance < 0.32:
                        nivel = nivel + 1
                        break
                elif tentativa == 1:
                    # print("game over")
                    mortes.append(nivel)

        if nivel == 18:
            for tentativa in range(2):
                upar = random.uniform(0, 1)
                upar2 = "{:.2f}".format(upar)
                upar3 = float(upar2)
                if upar3 < 0.28:
                    nivel = nivel + 1
                    break
                elif fCoins > 0:
                    fCoins = fCoins - 1
                    free_chance = upar3 - 0.25
                    if free_chance < 0.28:
                        nivel = nivel + 1
                        break
                elif pCoins > 0:
                    pCoins = pCoins - 1
                    paid_chance = upar3 - 0.7
                    if paid_chance < 0.28:
                        nivel = nivel + 1
                        break
                elif tentativa == 1:
                    # print("game over")
                    mortes.append(nivel)

        if nivel == 19:
            for tentativa in range(2):
                upar = random.uniform(0, 1)
                upar2 = "{:.2f}".format(upar)
                upar3 = float(upar2)
                if upar3 < 0.24:
                    nivel = nivel + 1
                    break
                elif fCoins > 0:
                    fCoins = fCoins - 1
                    free_chance = upar3 - 0.25
                    if free_chance < 0.24:
                        nivel = nivel + 1
                        break
                elif pCoins > 0:
                    pCoins = pCoins - 1
                    paid_chance = upar3 - 0.7
                    if paid_chance < 0.24:
                        nivel = nivel + 1
                        break
                elif tentativa == 1:
                    # print("game over")
                    mortes.append(nivel)

        if nivel == 20:
            for tentativa in range(2):
                upar = random.uniform(0, 1)
                upar2 = "{:.2f}".format(upar)
                upar3 = float(upar2)
                if upar3 < 0.2:
                    nivel = nivel + 1
                    break
                elif fCoins > 0:
                    fCoins = fCoins - 1
                    free_chance = upar3 - 0.25
                    if free_chance < 0.2:
                        nivel = nivel + 1
                        break
                elif pCoins > 0:
                    pCoins = pCoins - 1
                    paid_chance = upar3 - 0.7
                    if paid_chance < 0.2:
                        nivel = nivel + 1
                        break
                elif tentativa == 1:
                    # print("game over")
                    mortes.append(nivel)

        if nivel == 21:
            for tentativa in range(2):
                upar = random.uniform(0, 1)
                upar2 = "{:.2f}".format(upar)
                upar3 = float(upar2)
                if upar3 < 0.16:
                    nivel = nivel + 1
                    break
                elif fCoins > 0:
                    fCoins = fCoins - 1
                    free_chance = upar3 - 0.25
                    if free_chance < 0.16:
                        nivel = nivel + 1
                        break
                elif pCoins > 0:
                    pCoins = pCoins - 1
                    paid_chance = upar3 - 0.7
                    if paid_chance < 0.16:
                        nivel = nivel + 1
                        break
                elif tentativa == 1:
                    # print("game over")
                    mortes.append(nivel)

        if nivel == 22:
            for tentativa in range(2):
                upar = random.uniform(0, 1)
                upar2 = "{:.2f}".format(upar)
                upar3 = float(upar2)
                if upar3 < 0.12:
                    nivel = nivel + 1
                    break
                elif fCoins > 0:
                    fCoins = fCoins - 1
                    free_chance = upar3 - 0.25
                    if free_chance < 0.12:
                        nivel = nivel + 1
                        break
                elif pCoins > 0:
                    pCoins = pCoins - 1
                    paid_chance = upar3 - 0.7
                    if paid_chance < 0.12:
                        nivel = nivel + 1
                        break
                elif tentativa == 1:
                    # print("game over")
                    mortes.append(nivel)

        if nivel == 23:
            for tentativa in range(2):
                upar = random.uniform(0, 1)
                upar2 = "{:.2f}".format(upar)
                upar3 = float(upar2)
                if upar3 < 0.08:
                    nivel = nivel + 1
                    break
                elif fCoins > 0:
                    fCoins = fCoins - 1
                    free_chance = upar3 - 0.25
                    if free_chance < 0.08:
                        nivel = nivel + 1
                        break
                elif pCoins > 0:
                    pCoins = pCoins - 1
                    paid_chance = upar3 - 0.7
                    if paid_chance < 0.08:
                        nivel = nivel + 1
                        break
                elif tentativa == 1:
                    # print("game over")
                    mortes.append(nivel)

        if nivel == 24:
            for tentativa in range(2):
                upar = random.uniform(0, 1)
                upar2 = "{:.2f}".format(upar)
                upar3 = float(upar2)
                if upar3 < 0.04:
                    # print("parabéns, o jogador venceu!")
                    # print("GG!")
                    mortes.append(nivel + 1)
                    break
                elif fCoins > 0:
                    fCoins = fCoins - 1
                    free_chance = upar3 - 0.25
                    if free_chance < 0.04:
                        mortes.append(nivel + 1)
                        break
                elif pCoins > 0:
                    pCoins = pCoins - 1
                    paid_chance = upar3 - 0.7
                    if paid_chance < 0.04:
                        # print("parabéns, o jogador venceu!")
                        # print("GG!")
                        mortes.append(nivel + 1)
                        break
                elif tentativa == 1:
                    # print("game over")
                    mortes.append(nivel)

    return mortes


def basico25f2p_media():
    media = round(statistics.mean(mortes), 2)
    return media


def basico25f2p_dp():
    for morte in mortes:
        mortes_dp.append((morte - basico25f2p_media()) ** 2)

    media_dp = round(statistics.mean(mortes_dp), 2)
    dp = round((media_dp ** (1 / 2)), 2)
    return dp


def basico25f2p_ic_superior():
    x = basico25f2p_media()
    o = basico25f2p_dp()
    n = len(mortes)
    basico25f2p_lim_superior = round(x + z * (o / (n ** (1 / 2))), 2)
    return basico25f2p_lim_superior


def basico25f2p_ic_inferior():
    x = basico25f2p_media()
    o = basico25f2p_dp()
    n = len(mortes)
    basico25f2p_lim_inferior = round(x - z * (o / (n ** (1 / 2))), 2)
    return basico25f2p_lim_inferior


def basico25f2p_erro():
    basico25f2p_yerr = round(basico25f2p_ic_superior() - basico25f2p_media(), 2)
    return basico25f2p_yerr
