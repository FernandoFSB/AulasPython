
def produto(n1, n2):
	prod = (n1*2)*(n2/2)
	return prod

def soma(n1, n3):
	som = (n1*3) + n3
	return som

def cubo(n3):
	cub = n3**3
	return cub

def main():
	n1 = int(input('Digite um número: '))
	n2 = int(input('Digite um segundo número: '))
	n3 = float(input('Digite um terceiro número: '))
	produto(n1, n2)
	soma(n1,n3)
	cubo(n3)
	print(produto(n1, n2), soma(n1,n3), cubo(n3) )

main()

