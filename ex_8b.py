# 8. Faça uma função que informe a quantidade
# de dígitos de um determinado número inteiro
# informado.


numero = int(input("Digite um número: "))

def conta_digitos (numero):
    palavra = str(numero)
    conta = len(palavra)
    return (conta)

print("O número {} tem {} digito(s)".format(numero, conta_digitos(numero)))
