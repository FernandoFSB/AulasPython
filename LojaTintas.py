def main():
	tamanho = float(input('Tamanho em metros quadrados: '))
	if tamanho % 54 == 0:
		latas = tamanho / 2
	else:
		latas = int(tamanho / 54) + 1
	preco = latas * 80
	print ('%d latas' %latas)
	print ('R$ %.2f' %preco)
main()

