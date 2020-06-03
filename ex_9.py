# 9. Reverso do número. Faça uma função que
# retorne o reverso de um número inteiro
# informado. Por exemplo: 127 -> 721.


numero = int(input("Digite um número: "))

def reverte_numero (numero):
    palavra = str(numero)
    reverso = palavra[::-1]
    return (reverso)

print("O reverso do número {} é {}".format(numero,reverte_numero(numero)))
