# Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

def main():
	n1 = float(input('Digite a primeira nota: '))
	n2 = float(input('Digite a segunda nota: '))

	media = (n1+n2)/2

	while n1 > 10 or n1 < 0:
		print('A primeira nota está errada, por favor digite novamente as notas!')
		n1 = float(input('Digite a primeira nota: '))
		n2 = float(input('Digite a segunda nota: '))

	while n2 > 10 or n2 < 0:
		print('A segunda nota está errada, por favor digite novamente as notas!')
		n1 = float(input('Digite a primeira nota: '))
		n2 = float(input('Digite a segunda nota: '))

	if media == 10:
		print('Aprovado com Distinção')
	elif 7 <= media <= 9.9:
		print('Aprovado')
	else:
		print('Reprovado')
main()



