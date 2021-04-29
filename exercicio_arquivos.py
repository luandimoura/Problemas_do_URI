'''
arq = open("teste.txt", "r")
linha = arq.readline()
print(linha)

arq.close()
'''

arq = open("teste.txt", "r")

for linha in arq:
    print(linha)

arq.close()
