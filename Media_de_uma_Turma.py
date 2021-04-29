#Programa - Registro - Media dos alunos

#Declaracoes
TAM = 8
class Taluno:
    rga = None
    nota1 = None
    nota2 = None
    nota3 = None
    nota4 = None

turma = [Taluno() for x in range(TAM)]
media = 0.0

#Leitura dos dados
for i in range(TAM):
    turma[i].rga = input('Informe o rga do aluno: '))
    turma[i].nota1 = float(input('Nota 1: '))
    turma[i].nota2 = float(input('Nota 2: '))
    turma[i].nota3 = float(input('Nota 3: '))
    turma[i].nota4 = float(input('Nota 4: '))

#Calculo da media
for i in range(TAM):
    media = ((turma[i].nota1*2) + (turma[i].nota2*3) + (turma[i].nota3*2) + (turma[i].nota4*3))/10.0
    
    if(media>=6):
        print('RGA ' + str(turma[i].rga)+' - Aprovado com media %.2f' %media)
    
    else:
        print('RGA ' + str(turma[i].rga)+' - Reprovado com media %.2f' %media)
        
        
