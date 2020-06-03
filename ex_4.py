# 4. Faça um programa, com uma função que necessite
# de um argumento. A função retorna o valor de
# caractere ‘P’, se seu argumento for positivo,
# e ‘N’, se seu argumento for zero ou negativo.


def positivo_negativo (x):
    if x > 0:
        print("P")
    elif x <= 0:
        print("N")

numero = int(input("Digite um número: "))
positivo_negativo(numero)