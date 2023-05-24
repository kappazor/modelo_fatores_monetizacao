# Universidade de Brasília
# Departamento de Ciência da Computação
# TCC
# Rodrigo da Silva Navarro - 15/0147376
# Código do Modelo Padrão de um Jogo Gacha
#
#
#
# usaremos apenas estas duas bibliotecas:
#     - random para gerar uma variável aleatória uniforme com a função 'uniform';
#     - statistics para calcular a média dos elementos presentes no array 'mortes'
import random
import statistics


def padrao1f2p():
    mortes = []

    # número de simulações (runs)
    for x in range(5000):
        # a cada run, o jogo é resetado, ou seja, o nivel volta para 1 e a quantidade de
        # soft e hard currency volta ao padrão do tipo de jogador que está sendo simulado
        nivel = 1
        pCoins = 0
        fCoins = 0
        if nivel == 1:
            # cada nível terá 2 tentativas para pular para o próximo nível
            # usamos a função uniform da biblioteca random para gerar um número entre 0 e 1
            # upar2 limita esse número a duas casas decimais
            # upar3 transforma esse número para o tipo float
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)

            # se upar3 for menor que a chance de pular para o próximo nivel, incrementa nível e quebra o loop
            if upar3 < 0.98:
                nivel = nivel + 1
            # se a carteira de soft currency (fCoins) for maior que zero, decrementa a carteira e aumenta
            # 25% de chance à variável upar3, que foi gerada no início da tentativa
            #
            # caso essa nova chance aumentada (free_chance) satisfaça o requisito para pular para o próximo
            # nível, incrementa o nível e quebra o loop
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.98:
                    nivel = nivel + 1
            # se a carteira de hard currency (pCoins) for maior que zero, decrementa a carteira e aumenta
            # 70% de chance à variável upar3, que foi gerada no início da tentativa
            #
            # caso essa nova chance aumentada (paid_chance) satisfaça o requisito para pular para o próximo
            # nível, incrementa o nível e quebra o loop
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.98:
                    nivel = nivel + 1
            # para entrar neste if, as carteiras de soft e hard currency precisam estar vazias e precisa ter
            # falhado o pulo de nível pela segunda vez. caso isso aconteça, anexa o nível atual no array 'mortes'
            # para indicar em qual nível esta run terminou.
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 2:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.96:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.96:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.96:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 3:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.94:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.94:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.94:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 4:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.92:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.92:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.92:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 5:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.9:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.9:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.9:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 6:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.88:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.88:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.88:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 7:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.86:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.86:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.86:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 8:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.84:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.84:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.84:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 9:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.82:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.82:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.82:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 10:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.8:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.8:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.8:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 11:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.78:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.78:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.78:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 12:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.76:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.76:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.76:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 13:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.74:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.74:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.74:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 14:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.72:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.72:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.72:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 15:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.7:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.7:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.7:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 16:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.68:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.68:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.68:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 17:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.66:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.66:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.66:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 18:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.64:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.64:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.64:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 19:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.62:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.62:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.62:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 20:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.6:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.6:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.6:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 21:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.58:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.58:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.58:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 22:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.56:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.56:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.56:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 23:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.54:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.54:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.54:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 24:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.52:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.52:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.52:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 25:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.5:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.5:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.5:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 26:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.48:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.48:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.48:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 27:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.46:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.46:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.46:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 28:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.44:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.44:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.44:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 29:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.42:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.42:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.42:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 30:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.4:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.4:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.4:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 31:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.38:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.38:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.38:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 32:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.36:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.36:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.36:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 33:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.34:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.34:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.34:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 34:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.32:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.32:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.32:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 35:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.3:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.3:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.3:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 36:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.28:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.28:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.28:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 37:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.26:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.26:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.26:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 38:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.24:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.24:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.24:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 39:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.22:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.22:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.22:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 40:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.2:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.2:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.2:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 41:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.18:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.18:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.18:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 42:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.16:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.16:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.16:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 43:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.14:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.14:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.14:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 44:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.12:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.12:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.12:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 45:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.1:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.1:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.1:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 46:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.08:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.08:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.08:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 47:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.06:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.06:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.06:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 48:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.04:
                nivel = nivel + 1
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.04:
                    nivel = nivel + 1
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.04:
                    nivel = nivel + 1
            else:
                # print("game over")
                mortes.append(nivel)

        if nivel == 49:
            upar = random.uniform(0, 1)
            upar2 = "{:.2f}".format(upar)
            upar3 = float(upar2)
            if upar3 < 0.02:
                # print("parabéns, o jogador venceu!")
                mortes.append(nivel + 1)
            elif fCoins > 0:
                fCoins = fCoins - 1
                free_chance = upar3 - 0.25
                if free_chance < 0.02:
                    mortes.append(nivel + 1)
                    break
            elif pCoins > 0:
                pCoins = pCoins - 1
                paid_chance = upar3 - 0.7
                if paid_chance < 0.02:
                    # print("parabéns, o jogador venceu!")
                    # print("GG!")
                    mortes.append(nivel + 1)
            else:
                # print("game over")
                mortes.append(nivel)

    y = float("{:.2f}".format(statistics.mean(mortes)))
    print(y)
    return y
