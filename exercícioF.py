# Crie um programa no qual o usuário digitará 5 nomes num vetor (OBRIGATÓRIO TER SEU NOME INCLUÍDO NO VETOR). Em seguida:
# a) Mostre os valores na tela.
# b) Adicione seu sobrenome na posição do seu nome no array.
# c) Imprima o resultado na tela.


nomes = []
meuNome = 'Fernando'

#Implementando o for para adicionar 5 valores
for i in range(5):

    #Pedindo e adicionando valores para o array
    nomes.append(input('Digite um nome: '))

#Imprimindo na tela para verificar
print(nomes)

#Implementando outro for para mudar um valor do array
for j in range(len(nomes)):

      #Quando J encontrar o valor Fernando será substituido por Fernando Figueiredo
      if nomes[j] in ['Fernando']:
        nomes[j] = 'Fernando Figueiredo'

#Imprimindo o valor final
print(nomes)
