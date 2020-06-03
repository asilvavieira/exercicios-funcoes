# 5. Faça um programa com uma função chamada
# somaImposto. A função possui dois parâmetros
# formais: taxaImposto, que é a quantia de
# imposto sobre vendas expressa em porcentagem
# e custo, que é o custo de um item antes do
# imposto. A função “altera” o valor de custo
# para incluir o imposto sobre vendas.


def soma_imposto (taxa_imposto, preco_custo):
    porcentagem = (preco_custo * taxa_imposto) / 100
    soma = porcentagem + preco_custo
    return (soma)

numero = float(input("Digite o valor(R$): "))
imposto = float(input("Digite o imposto(%): "))
print()
print("Valor final do produto: R$ {}".format(soma_imposto(imposto,numero)))

