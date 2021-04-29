#Programa - Soma de duas matrizes quadradas

TAM = 4

#Declaracao das matrizes
matriz1 = [[None for i in range(TAM)] for j in range(TAM)]
matriz2 = [[None for i in range(TAM)] for j in range(TAM)]
matriz3 = [[None for i in range(TAM)] for j in range(TAM)]

#Leitura da matriz 1
print('Matriz 1')
for i in range(TAM):
    for j in range(TAM):
        matriz1[i][j] = input('Informe o valor na posicao [%i %i]: ' %(i, j))
#Leitura da matriz 2
print('Matriz 2')
for i in range(TAM):
    for j in range(TAM):
        matriz2[i][j] = input('Informe o valor na posicao [%i %i]: ' %(i,j))

#Soma das matriz 1 com a matriz 2        
for i in range(TAM):
    for j in range(TAM):
        matriz3[i][j] = int(matriz1[i][j])+int(matriz2[i][j])


print ('\nSoma das matrizes')      
#Imprimindo o resultado final
for i in range(TAM):
    for j in range(TAM):
        print (str(matriz3[i][j]), end = ' ')
    print('')

#Imprimindo a matriz 1
print('\nMatriz 1')
for i in range(TAM):
    for j in range(TAM):
        print(str(matriz1[i][j]), end = ' ')
    print('')

#Imprimindo a matriz 2
print('\nMatriz 2')
for i in range(TAM):
    for j in range(TAM):
        print(str(matriz2[i][j]), end = ' ')
    print('')
    
