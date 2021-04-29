#Programa_Calculo_do_Salario

salario = 0.0

print("Calculo do salario")
hora = int(input("Informe o numero de horas trabalhadas: "))
valor = float(input("Informe o valor que voce recebe por hora trabalhada: "))

salario = hora*valor

print("Salario: R$ %.2f" %salario)
