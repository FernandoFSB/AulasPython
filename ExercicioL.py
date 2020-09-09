# Faça um programa que pergunte o preço de três produtos
# e informe qual produto você deve comprar, sabendo que a
# decisão é sempre pelo mais barato.


prod1 = float(input("Digite o primeiro preço: "))
prod2 = float(input("Digite o segundo preço: "))
prod3 = float(input("Digite o terceiro preço: "))

if prod1 < prod2 and prod1 < prod3:
	print(f'Você deve comprar o produto número 1 com o valor de R${prod1}')
elif prod2 < prod1 and prod2 < prod3:
	print(f'Você deve comprar o produto número 2 com o valor de R${prod2}')
else:
	print(f'Você deve comprar o produto número 3 com o valor de R${prod3}')