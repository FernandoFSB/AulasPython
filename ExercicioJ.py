# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Gênero Inválido.

def main():
	genero = input('Digite F - Feminino ou M - Masculino: ')

	while genero =='':
		print('Está em branco, por favor digite algo para saber seu genero')
		genero = input('Digite F - Feminino ou M - Masculino: ')
	while genero != 'F' and genero != "M" and genero != 'm' and genero !='f':
		print('Genero errado, Digite novamente')
		genero = input('Digite F - Feminino ou M - Masculino: ')
	if genero == 'F' or genero =='f':
		print('Genero Feminino')
	elif genero == 'M' or genero == 'm':
		print('Genero Masculino')

main()



