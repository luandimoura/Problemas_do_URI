arquivo = open('entrada.txt', 'r')
arquivo2 = open('saida_2.txt', 'w')

for line in arquivo:
    cont_abre = 0
    condicao_de_Erro = 0
    for letra in line:
        if(letra == '('):
            cont_abre = cont_abre + 1
        if(letra == ')'):
            cont_abre = cont_abre - 1
            if(cont_abre < 0):
                condicao_de_Erro = 1

    if(cont_abre == 0 and condicao_de_Erro == 0):
        print('correct')
        arquivo2.write('correct\n')
    else:
        print('incorrect')
        arquivo2.write('incorrect\n')


arquivo.close
arquivo2.close
