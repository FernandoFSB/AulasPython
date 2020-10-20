# Crie um array que o conteúdo seja nomes das cores.
# Em seguida remova apenas a cor "vermelho”, se houver.


cores = []
remover = 'vermelho'

#Implementando o for para adicionar 5 valores
for i in range(5):

    #Adicionando valores ao array
    cores.append(input('Digite uma cor: '))

#imprimindo para testar
print(cores)

#Implementando o While para verificar se tem o 'vermelho'
while remover in cores:

    #Removendo o vermelho do array
    cores.remove(remover)

#imprimindo na tela o valor final
print(cores)
