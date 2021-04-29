#Programa_Loja_de_Tintas

area = int(input("Informe o tamanho em metros quadrados: "))

quantidade_latas = area/54.0
valor = quantidade_latas*80.0

print("Quantidade de latas necessarias: %.1f" %quantidade_latas)
print("Valor total: %.2f" %valor)
