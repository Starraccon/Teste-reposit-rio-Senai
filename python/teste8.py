notaA=float(input("Informe a primeira nota: "))
notaB=float(input("Informe a segunda nota: "))

#calcular media
mediafinal = (notaA + notaB) / 2

#verificação
if mediafinal >=7.0:
    print("A média: %.lf - Aprovado "% mediafinal)
else:
    print("A média: %.lf - Reprovado "% mediafinal)