# Elabore um programa que cria um array de nomes de países e outro array com nomes de cidades.
# Cada uma das criações devem ser feitas com métodos diferentes.


#Iniciando os arrays
paises = []
cidades = []

            # metodo 1

# adicionando valores ao array paises
for i in range(5):
    paises.append(input('Digite 5 paises: '))

# imprimindo na tela para verificar
print(paises)

            #metodo 2
            
#adicionando valores ao array cidades
cont = 0
while cont < 5:
    cidades.insert(cont,input('Digite o nome de 5 cidades: '))
    cont+=1

#imprimindo na tela para verificar
print(cidades)