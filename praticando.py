from signal import raise_signal
import telnetlib


Curso=[{"Codigo":123,"Nome":"Sistemas de Informação","Duracao":4},
{"Codigo":213,"Nome":"Ciência de Dados e IA","Duracao":4},
{"Codigo":321,"Nome":"Engenharia Biomédica","Duracao":5},
]

Curriculo=[{"Id":123654,"CodigoCurso":123, "AnoImplantacao":2020,"SemestreImplantacao":1},
{"Id":123655,"CodigoCurso":213, "AnoImplantacao":2021,"SemestreImplantacao":1},
{"Id":123656,"CodigoCurso":321, "AnoImplantacao":2022,"SemestreImplantacao":1},
]
Disciplina=[{"Codigo":12345,"Nome":"Calculo I","Creditos":6},
{"Codigo":12121,"Nome":"Álgebra Linear","Creditos":4},
{"Codigo":11211,"Nome":"Engenharia de Software","Creditos":2},
]
Componente=[{"IdCurriculo":123656,"CodigoDisciplina":[11211]},

{"IdCurriculo":123655,"CodigoDisciplina":[11211]},
{"IdCurriculo":123654,"CodigoDisciplina":[12121]},
]
Aluno=[{"RA":22334455,"Nome":"José da Silva", "Telefone":19991919191},
{"RA":21918171,"Nome":"Maria da Silva", "Telefone":11991223344},
{"RA":20202020,"Nome":"João de Souza", "Telefone":21993456789}]
Ingresso=[{"IdCurriculo":123654,"Semestre":2,"Ano":2022,"RaAluno":[22334455
]},
{"IdCurriculo":123655,"Semestre":2,"Ano":2022,"RaAluno":[21918171]},
{"IdCurriculo":123656,"Semestre":1,"Ano":2023,"RaAluno":[20202020]},
]
Professores=[{"Matrícula":94949494,"Nome":"André Carvalho"},
{"Matrícula":99123321,"Nome":"Mário Lima"},
{"Matrícula":98765432,"Nome":"Daniele Almeida"},
]

Turma=[{"Id":123123,"Ano":2022,"Semestre":2,"Letra":"A", "CodigoDisciplina":12345,"MatriculaProfessor":99123321},
{"Id":123124,"Ano":2022,"Semestre":1,"Letra":"B",
"CodigoDisciplina":12345,"MatriculaProfessor":98765432},
{"Id":123125,"Ano":2022,"Semestre":1,"Letra":"A",
"CodigoDisciplina":11211,"MatriculaProfessor":99123321},

{"Id":123456,"Ano":2023,"Semestre":1,"Letra":"A",
"CodigoDisciplina":12345,"MatriculaProfessor":99123321},
{"Id":123457,"Ano":2023,"Semestre":1,"Letra":"B",
"CodigoDisciplina":12345,"MatriculaProfessor":98765432},
{"Id":123458,"Ano":2023,"Semestre":1,"Letra":"A",
"CodigoDisciplina":11211,"MatriculaProfessor":99123321},
]
Matriculas=[{"IdTurma":123456,"RaAluno":[22334455]},
{"IdTurma":123458,"RaAluno":[22334455]},
{"IdTurma":123456,"RaAluno":[21918171]},
]
 

Resultado=[{"RaAluno":20202020,"IdTurma":123123,"Nota":7.5,"Frequencia":8},
{"RaAluno":22334455,"IdTurma":123125,"Nota":3.5,"Frequencia":65},
{"RaAluno":21918171,"IdTurma":123123,"Nota":6.0,"Frequencia":32},
]



       
    
'''def recuperaNomeV3 (Alu,RA):
    for aluno in Alu:
        if aluno["RA"]==RA: return aluno["Nome"]
    return None
        
    
print(recuperaNomeV3(Aluno,20202020))
print(recuperaNomeV3(Aluno,22222222))


##############################################################################################

def NomeDoProfessor(id_turma, lisTurma): 
    for Turma in lisTurma:
        if Turma["Id"]==id_turma:
            cod_professor=Turma["MatriculaProfessor"]
            for professor in Professores: 
                if professor["Matricula"] == cod_professor:
                    return Professores["Nome"]
    return None

print(NomeDoProfessor(Turma,123123))


##############################################################################################


def NomedoProfessor(Professor, MatriculaProfessor):
	for p in Professor:
		if p["MatriculaProfessor"]== MatriculaProfessor: return p["Nome"]
	return None 


print(NomedoProfessor(Professores,94949494))


##############################################################################################


def NomesDosBenignos(Resultado, Turma, Resultado): #def para descobrir os professores que reprovaram alunos
	malignos=[]
	for r in Resultado: 
		if r["Notas"]<5 or r["Frequencia"]<75:
			for t in Turma:
				if t["Id"] ==r["IdTurma"]:
					if t["MatriculaProfessor"] not in malignos:
						malignos.append(t["MatriculaProfessor"])
	benignos=[]
	for p in Professor:
		if p["Matricula"] not in malignos:
			benignos.append(p["Nome"])
	return benignos	
	


##############################################################################################

def RAsComMaisDeUmIngresso(Aluno, Ingresso):			
	RAs=[]
	for a in Aluno:
	    contagemDeIngressos=0
		for i in Ingresso:
			if a["RA"] in i["RaAluno]:
				contagemDeIngressos+=1
				if contagemDeIngressos==2:
					RAs.append(a["RAs"])	
					break
	return RAs

def DuracaoDoCurso (Curso, Codigo): # exercicio 1 lista 8 
    for c in Curso: 
        if c["Codigo"] == Codigo: return c["Duracao"] 
    return None

print(DuracaoDoCurso(Curso,321))
#codigo do curso
#verificar se o codigo existe
#demonstrar duração 


##############################################################################################

# codigo do da disciplina 
# vberificar se o codigo existe 
# mostrar os creditos 

def QuantidadeDeCreditos(Disciplina, Codigo): # exercicio 3 lista 8 
    for d in Disciplina:
        if d["Codigo"] == Codigo: return d["Creditos"]
    return None 

print(QuantidadeDeCreditos(Disciplina,12345))


##############################################################################################

# codigo do da disciplina 
# vberificar se o codigo existe 
# mostrar os creditos 

def TelefoneDoAluno(Aluno,RA): #funcionou exercicio 5 lista 8 
    for a in Aluno:
        if a["RA"] == RA: return a["Telefone"]
    return None

print(TelefoneDoAluno(Aluno,22334455))


##############################################################################################

def NomedoProfessor(Professor, MatriculaDoProfessor):  # exercicio 7 lista 8 
    for p in Professor:
        if p["Matrícula"] == MatriculaDoProfessor:  return p["Nome"]
    return None

print(NomedoProfessor(Professores,94949494))


##############################################################################################

def ProfessorQueMinistraraAula(Turmas, Id, Professores): # exercicio 8 
    for Turma in Turmas:
        if Turma["Id"] == Id: 
           for professor in Professores:
                if professor["Matrícula"] == Turma["MatriculaProfessor"]:
                    return professor["Nome"]
    return None
print(ProfessorQueMinistraraAula(Turma,123123))



##############################################################################################

# 3 for 
## usar lista professor pra saber o nome do professor
# usar lista turma para 

def NomeDosAlunosMatriculados(Matriculas, Id_Turma, Aluno): #exercicio 9 lista 8 na sei o pq nao ta funcionando. 
    matriculado=[]
    for Matricula in Matriculas: 
        if Matricula["IdTurma"] == Id_Turma:
            for ra in Aluno:
                if ra["RA"] in Matricula["RaAluno"]:
                    matriculado.append(ra["Nome"])
    return matriculado
          
    
print(NomeDosAlunosMatriculados(Turma, 123123))  


##############################################################################################

 Exercicio 11

def QuantidaDeDeReprova(Aluno, Resultado):
    for a in Aluno: 
        contagemdereprova=0
        for r in Resultado:
            if r["Nota"]<5 or r["Frequencia"]<75:
                for ra in Resultado:
                    if a["RA"] in ra["RaAluno"]:
                        contagemdereprova+=1
    return contagemdereprova

print(QuantidaDeDeReprova(Resultado, 22334455))  '''


# Exercicio 16

def MaisDeUmCurso(Aluno, Ingresso):
    RAs=[]
    for a in Aluno:
        contador=0
        for i in Ingresso:
            if a["RA"] in i["RaAluno"]:
                contador+=1
                if contador==2:
                    RAs.append(a["RA"])
                    break
    return RAs

