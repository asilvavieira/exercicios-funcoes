# 2. Faça um programa para imprimir:
#
#    1
#    1   2
#    1   2   3
#    .....
#    1   2   3   ...  n
#
# para um n informado pelo usuário. Use uma função
# que receba um valor n inteiro imprima até
# a n-ésima linha.


def imprime_numero(n):
    for i in range(1, n+1):
        for j in range(i):
            print(j+1,end=" ")
        print()

numero = int(input("Digite um número: "))
print()
imprime_numero(numero)