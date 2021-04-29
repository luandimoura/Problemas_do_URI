#Programa Caixa Eletrônico

#Variaveis
cont1, cont2, cont3, cont4, cont5, cont6 = 0,0,0,0,0,0


print('CAIXA ELETRÔNICO')
saque = int(input('Informe o valor que deseja sacar: '))

if(saque>=10 and saque<=600):
    if(saque>=100):
        div = saque//100
        cont1 = div
        saque = saque%100

    if(saque>=50):
        div = saque//50
        cont2 = div
        saque = saque%50

    if(saque>=20):
        div = saque//20
        cont3 = div
        saque = saque%20

    if(saque>=10):
        div = saque//10
        cont4 = div
        saque = saque%10

    if(saque>=5):
        div = saque//5
        cont5 = div
        saque = saque%5

    if(saque>=1):
        div = saque//1
        cont6 = div
        saque = saque%1

    print('Notas de 100: %i' %cont1)
    print('Notas de 50: %i' %cont2)
    print('Notas de 20: %i'%cont3)
    print('Notas de 10: %i'%cont4)
    print('Notas de 5: %i'%cont5)
    print('Notas de 1: %i'%cont6)

else:
    print('Valor solicitado nao e compativel')   
        
