#coding = utf-8
#Codigo Prova 1

TAM = 3
matriz = [[None for i in range(TAM)] for j  in range(TAM) ]
soma = 0
media = 0
aux = 0

op = input('Informe a operacao (S-SOMA ou M-MEDIA): ')

for i in range(TAM):
    for j in range(TAM):
        matriz[i][j] = input()

for i in range(0,TAM, 2):
    for j in range(0,TAM, 2):
        if(int(matriz[i][j]) % 2 == 0):
            aux = aux +1
            soma = soma + int(matriz[i][j])

#if(op.upper() == 'S'):
if(op == 'S' or op =='s'):
    print ('Soma: ', soma)

if(op=='m' or op=='M'):
    media=(soma/float(aux))
    print('Media: %.2f' % media)

for i in range(TAM):
    for j in range(TAM):
        print (str(matriz[i][j]), end=' ')
    print('')


