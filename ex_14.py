# 14. Quadrado mágico. Um quadrado mágico é
# aquele dividido em linhas e colunas,
# com um número em cada posição e no qual
# a soma das linhas, colunas e diagonais
# é a mesma. Por exemplo, veja um quadrado
# mágico de lado 3, com números de 1 a 9:
#
# 8  3  4
# 1  5  9
# 6  7  2
#
# Elabore uma função que identifica e mostra
# na tela todos os quadrados mágicos com as
# características acima. Dica: produza todas
# as combinações possíveis e verifique a soma
# quando completar cada quadrado. Usar um vetor
# de 1 a 9 parece ser mais simples que usar
# uma matriz 3x3.

"""
from random import randint

def gera_lista ():
    lista = []
    cont = 0

    while True:
        num = randint(1,9)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 9:
            break
    return (lista)

def gera_matriz():
    lista_temporaria = gera_lista()
    matriz = [[0,0,0],[0,0,0],[0,0,0]]
    contador = 0

    for linha in range(3):
        for coluna in range(3):
            matriz[linha][coluna] = lista_temporaria[contador]
            contador += 1
    print()
    for linha in range(3):
        for coluna in range(3):
            print(f'[{matriz[linha][coluna]}]', end="")
        print()
    return (matriz)

matriz_temporararia = gera_matriz()


#matriz_temporararia = [[8, 3, 4],[1, 5, 9],[6, 7, 2]]

linhas = [0, 0, 0]
colunas = [0, 0, 0]
diagonais = [0, 0]

print()

def testa_matriz ():
    for i in range(3):
        linhas[i] = sum(matriz_temporararia[i])
#    print("Linhas = {}".format(linhas))

    for i in range(3):
        for j in range(3):
            colunas[i] += matriz_temporararia[j][i]
#    print("Colunas = {}".format(colunas))

    cont = 2
    for i in range(3):
        diagonais[0] += matriz_temporararia[i][i]
        diagonais[1] += matriz_temporararia[i][cont]
        cont -= 1
#    print("Diagonais = {}".format(diagonais))

#    print()
    if linhas[0] == linhas[1] == linhas[2] == colunas[0] == colunas[1] == colunas[2] == diagonais[0] == diagonais[1]:
#        print("Quadrado perfeito!")
        return (True)
    else:
#        print("Não é um quadrado perfeito!")
        return (False)

print(testa_matriz())

"""

def gera_combinacoes(lista, n):
     #  gera tupla com todas as combinações possíveis da soma de três números da lista
     #  que seja iguais a 15.
     for i in lista:
         for j in lista:
             if n + i + j == 15 and (n != i and n != j and i != j):
                 combinacoes.append((n, i, j))


def gera_quadro(comb, L1):
    linha1 = L1
    for i in range(len(comb)):
        linha2 = comb[i]
        for j in range(len(comb)):
            linha3 = comb[j]


            if (linha1[0] + linha2[0] + linha3[0] == 15) and\
                (linha1[1] + linha2[1] + linha3[1] == 15) and\
                (linha1[2] + linha2[2] + linha3[2] == 15) and\
                (linha1[0] + linha2[1] + linha3[2] == 15) and\
                (linha1[2] + linha2[1] + linha3[0] == 15):

                 if (linha1[0] not in linha2) and\
                    (linha1[1] not in linha2) and\
                    (linha1[2] not in linha2):

                     print(linha1)
                     print(linha2)
                     print(linha3)
                     print()


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
combinacoes = []

for n in range(1,10):
    gera_combinacoes(lista, n)

print()

for L1 in combinacoes:
    gera_quadro(combinacoes, L1)