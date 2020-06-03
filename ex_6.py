# 6. Faça um programa que converta da notação de
# 24 horas para a notação de 12 horas. Por exemplo
# , o programa deve converter 14:25 em 2:25 P.M.
# A entrada é dada em dois inteiros. Deve haver
# pelo menos duas funções: uma para fazer a
# conversão e uma para a saída. Registre a
# informação A.M./P.M. como um valor ‘A’ para
# A.M. e ‘P’ para P.M. Assim, a função para
# efetuar as conversões terá um parâmetro formal
# para registrar se é A.M. ou P.M. Inclua um
# loop que permita que o usuário repita esse
# cálculo para novos valores de entrada todas
# as vezes que desejar.


def converte_hora (hora):
    doze = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    vinte_e_quatro = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 0]
    if hora != 0 and hora >= 1 and hora <= 12:
        hora_final = hora
    else:
        hora_final = doze[vinte_e_quatro.index(hora)]
    return (hora_final)

def am_pm (hora):
    if hora == 0 or hora >= 1 and hora <= 11:
        tempo = "AM"
    else:
        tempo = "PM"
    return (tempo)


while True:
    print()
    hora = int(input("Digite a hora: "))
    while hora > 23 or hora < 0:
        hora = int(input("Digite o valor da hora correto: "))
        continue

    minuto = int(input(("Digite os minutos: ")))
    while minuto > 59 or minuto < 0:
        minuto = int(input("Digite o valor de minutos correto: "))
        continue


    print()
    print("{}:{} {}".format(converte_hora(hora),minuto,am_pm(hora)))
