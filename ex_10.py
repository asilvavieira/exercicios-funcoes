# 10. Jogo de Craps. Faça um programa de
# implemente um jogo de Craps. O jogador
# lança um par de dados, obtendo um valor
# entre 2 e 12. Se, na primeira jogada,
# você tirar 7 ou 11, você um "natural"
# e ganhou. Se você tirar 2, 3 ou 12 na
# primeira jogada, isto é chamado de "craps"
# e você perdeu. Se, na primeira jogada,
# você fez um 4, 5, 6, 8, 9 ou 10,este é
# seu "Ponto". Seu objetivo agora é continuar
# jogando os dados até tirar este número
# novamente. Você perde, no entanto, se tirar
# um 7 antes de tirar este Ponto novamente.


import random

def jogador_dados():
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    valor = dado1 + dado2
    return[dado1, dado2, valor]

dados = jogador_dados()
print("\nDado 1: {} \ Dado 2: {} \ Valor: {}".format(dados[0], dados[1], dados[2]))

if dados[2] in [7, 11]:
    print("---Natural---")
    print("---Você venceu!---")

elif dados[2] in [2, 3, 12]:
    print("---Craps---")
    print("---Você perdeu!---")

elif dados[2] in [4, 5, 6, 8, 9, 10]:
    ponto = dados[2]
    print("{} - Marcado".format(ponto))

    continuar = 1
    while continuar:
        dados = jogador_dados()
        print("\nDado 1: {} \ Dado 2: {} \ Valor: {}".format(dados[0], dados[1], dados[2]))

        if dados[2] == 7:
            print("---Você perdeu!---")
            break

        if dados[2] == ponto:
            print("{} = {}".format(dados[2], ponto))
            print("---Você venceu!---")
            break

        if dados[2] in [2, 3, 11, 12]:
            print("Marcação: {}, Nada acontece!".format(ponto))

        if dados[2] in [4, 5, 6, 8, 9, 10] and dados[2] != ponto:
            print("Marcação: {}".format(ponto))

        continuar = int(input("\nJogar novamente?\n1.Sim\n0.Não\n"))
