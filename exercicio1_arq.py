arq = open("teste.txt", "r")
arq2 = open("saida.txt", "w")

texto = arq.readlines()

cont = 0
for line in texto:
    for letra in line:
        arq2.write(letra)
        print (letra, end = "")
        cont+=1


print("\nO numero de caracteres e: %d" %cont)


arq.close()
arq2.close()

