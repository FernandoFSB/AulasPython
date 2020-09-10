# Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

def main():
	numero = float(input('Digite um número para saber se é positivo ou negativo: '))

	while numero == 0:
		print('O número 0 não pode ser positivo nem negativo')
		numero = float(input('Digite um número para saber se é positivo ou negativo: '))
	if numero < 0:
		print(f'O número {numero} é Negativo')
	else:
		print(f'O número {numero} é Positivo')

main()



