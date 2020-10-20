# Crie um programa no qual o usuário digitará 5 nomes. Todos os cinco nomes serão salvos no vetor chamado "registros”. Em seguida:
# a) Mostre o que o usuário digitou na tela;
# b) O programa pedirá outro nome, que será adicionado no fim do vetor "registros”;
# c) O programa pedirá outro nome, que será adicionado na 2ª posição do vetor "registros”;
# d) Imprima o resultado na tela.

# iniciado o array registro
registro = []

#adicionando valores ao array
for i in range(5):
    registro.append(input('Digite o nome: '))

#imprimindo na tela para verificar
print(registro)

#adicionando um nome no final da fila
registro.append(input('Digite um outro nome: '))

#imprimindo na tela para verificar
print(registro)

#adicionando um nome na posição 2 do array
registro.insert(2, input('Digite um último nome: '))

#imprimindo na tela para verificar
print(registro)