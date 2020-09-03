def salarioBruto(porHora, qtdHora):
	salarioBrut = porHora * qtdHora
	return salarioBrut

def Iprf(salarioBrut):
	impostoRenda = salarioBrut * 0.11
	return impostoRenda

def Inss(salarioBrut):
	resultInss = salarioBrut * 0.08
	return resultInss

def Sindicato(salarioBrut):
	resultSindi = salarioBrut * 0.05
	return resultSindi

def SalarioLiquido(salarioBrut, impostoRenda, resultInss, resultSindi):
	salaLiqui = salarioBrut - impostoRenda - resultInss - resultSindi
	return salaLiqui

def Descontos(impostoRenda, resultInss, resultSindi):
	resultDesc = impostoRenda + resultInss + resultSindi
	return resultDesc

def main():
	porHora = float(input('Digite quanto você ganha por hora: '))
	qtdHoras = int(input('Digite quantas horas você trabalha por mês: '))

	I = salarioBruto(porHora, qtdHoras)
	II = Iprf(salarioBruto(porHora, qtdHoras))
	III = Inss(salarioBruto(porHora, qtdHoras))
	IV = Sindicato(salarioBruto(porHora, qtdHoras))
	V = SalarioLiquido(salarioBruto(porHora, qtdHoras), Iprf(salarioBruto(porHora, qtdHoras)), Inss(salarioBruto(porHora, qtdHoras)), Sindicato(salarioBruto(porHora, qtdHoras)))
	VI = Descontos(Iprf(salarioBruto(porHora, qtdHoras)), Inss(salarioBruto(porHora, qtdHoras)), Sindicato(salarioBruto(porHora, qtdHoras)))
	print(I)
	print(II)
	print(III)
	print(IV)
	print(V)
	print(VI)

main()