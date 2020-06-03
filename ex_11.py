# 11. Data com mês por extenso. Construa uma
# função que receba uma data no formato
# DD/MM/AAAA e devolva uma string no formato
# D de mesPorExtenso de AAAA. Opcionalmente,
# valide a data e retorne NULL caso a data
# seja inválida.


dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

print()
#print("{}/{}/{}".format(dia, mes, ano))

def mes_por_extenso (dia, mes, ano):
    mes1 = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    mes2 = mes1[mes-1]
    print("{} de {} de {}".format(dia, mes2, ano))

mes_por_extenso(dia, mes, ano)