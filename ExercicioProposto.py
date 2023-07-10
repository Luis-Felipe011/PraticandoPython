''' Considere as seguintes listas:

Curso=[{"Codigo":123,"Nome":"Sistemas de Informação","Duracao":4},
{"Codigo":213,"Nome":"Ciência de Dados e IA","Duracao":4},
{"Codigo":321,"Nome":"Engenharia Biomédica","Duracao":5},
...]

Curriculo=[{"Id":123654,"CodigoCurso":123, "AnoImplantacao":2020,"SemestreImplantacao":1},
{"Id":123655,"CodigoCurso":213, "AnoImplantacao":2021,"SemestreImplantacao":1},
{"Id":123656,"CodigoCurso":321, "AnoImplantacao":2022,"SemestreImplantacao":1},
...]
Disciplina=[{"Codigo":12345,"Nome":"Calculo I","Creditos":6},
{"Codigo":12121,"Nome":"Álgebra Linear","Creditos":4},
{"Codigo":11211,"Nome":"Engenharia de Software","Creditos":2},
...]
Componente=[{"IdCurriculo":123656,"CodigoDisciplina":[11211,...]},
...
{"IdCurriculo":123655,"CodigoDisciplina":[11211,...]},
{"IdCurriculo":123654,"CodigoDisciplina":[12121,...]},
...]
Aluno=[{"RA":22334455,"Nome":"José da Silva", "Telefone":19991919191},
{"RA":21918171,"Nome":"Maria da Silva", "Telefone":11991223344},
{"RA":20202020,"Nome":"João de Souza", "Telefone":21993456789},
...]
Ingresso=[{"IdCurriculo":123654,"Semestre":2,"Ano":2022,"RaAluno":[22334455
,...]},
{"IdCurriculo":123655,"Semestre":2,"Ano":2022,"RaAluno":[21918171,...]},
{"IdCurriculo":123656,"Semestre":1,"Ano":2023,"RaAluno":[20202020,...]},
...]
Professor=[{"Matrícula":94949494,"Nome":"André Carvalho"},
{"Matrícula":99123321,"Nome":"Mário Lima"},
{"Matrícula":98765432,"Nome":"Daniele Almeida"},
...]

Turma=[{"Id":123123,"Ano":2022,"Semestre":2,"Letra":"A", "CodigoDisciplina":12345,"MatriculaProfessor":99123321},
{"Id":123124,"Ano":2022,"Semestre":1,"Letra":"B",
"CodigoDisciplina":12345,"MatriculaProfessor":98765432},
{"Id":123125,"Ano":2022,"Semestre":1,"Letra":"A",
"CodigoDisciplina":11211,"MatriculaProfessor":99123321},
...
{"Id":123456,"Ano":2023,"Semestre":1,"Letra":"A",
"CodigoDisciplina":12345,"MatriculaProfessor":99123321},
{"Id":123457,"Ano":2023,"Semestre":1,"Letra":"B",
"CodigoDisciplina":12345,"MatriculaProfessor":98765432},
{"Id":123458,"Ano":2023,"Semestre":1,"Letra":"A",
"CodigoDisciplina":11211,"MatriculaProfessor":99123321},
...]
Matricula=[{"IdTurma":123456,"RaAluno":[22334455,...]},
{"IdTurma":123458,"RaAluno":[22334455,...]},
{"IdTurma":123456,"RaAluno":[21918171,...]},
...]
 

Resultado=[{"RaAluno":20202020,"IdTurma":123123,"Nota":7.5,"Frequencia":8},
{"RaAluno":22334455,"IdTurma":123125,"Nota":3.5,"Frequencia":65},
{"RaAluno":21918171,"IdTurma":123123,"Nota":6.0,"Frequencia":32},
...]
 

Exercícios Básicos:


1.	Escreva uma função em Python que, dado o código de um curso, bem como a lista de cursos, resulte a duração dele, caso esteja cadastrado, ou None, caso contrário. Faça um programa para testar sua função.
2.	Escreva uma função em Python que, dado o id de um currículo, bem como a lista de currículos, resulte uma tupla com dois valores, o ano de implantação dele e o semestre de implantação dele, caso esteja cadastrado, ou None, caso contrário. Faça um programa para testar sua função.
3.	Escreva uma função em Python que, dado o código de uma disciplina, bem como a lista de disciplinas, resulte sua quantidade de créditos, caso esteja cadastrada, ou None, caso contrário. Faça um programa para testar sua função.
4.	Escreva uma função em Python que, dado o id de um currículo e o código de uma disciplina, bem como a lista de componentes, resulte True, caso o código dado seja de uma das disciplinas do currículo, cujo código também foi dado, ou False, caso contrário. Faça um programa para testar sua função.
5.	Escreva uma função em Python que, dado o RA de um aluno, bem como a lista de alunos, resulte o telefone dele, caso esteja cadastrado, ou None, caso contrário. Faça um programa para testar sua função.
6.	Escreva uma função em Python que, dado o id de um currículo, um semestre e ano de ingresso, bem como a lista de ingressos, resulte o nome dos alunos ingressantes, caso haja ingresso naquele semestre e ano naquele currículo, ou None, caso contrário. Faça um programa para testar sua função.
7.	Escreva uma função em Python que, dada a matrícula de um professor, bem como a lista de professores, resulte o nome dele, caso esteja cadastrado, ou None, caso contrário. Faça um programa para testar sua função.
8.	Escreva uma função em Python que, dado o id de uma turma, bem como a lista de turmas, resulte o nome do professor que ministrará as aulas daquela turma, caso esteja cadastrado, ou None, caso contrário. Faça um programa para testar sua função.
9.	Escreva uma função em Python que, dado o id de uma turma, bem como a lista de matrículas, resulte uma lista com os nomes dos alunos matriculados naquela turma, caso esteja cadastrado, ou None, caso contrário. Faça um programa para testar sua função.
10.	Escreva uma função em Python que, dado o id de uma turma e o RA de um aluno, bem como a lista de resultados, resulte uma tupla com a nota e a frequência obtidas, caso haja um resultado naquela turma, daquele aluno, ou None, caso contrário. Faça um programa para testar sua função.
 

Exercícios mais Elaborados:
Em todos os exercícios abaixo, faz parte do exercício pensar em que parâmetros fornecer para a função para que ela apresentar um bom funcionamento e não acesse diretamente variáveis globais e nem que processar dados hardcoded na função, o que deve ser visto como algo execrável.

11.	Escreva uma função em Python que resulte a quantidade de vezes que um aluno com RA dado reprovou. Faça um programa para testar sua função.
12.	Escreva uma função em Python que resulte uma lista com os RAs dos alunos que nunca reprovaram. Faça um programa para testar sua função.
13.	Escreva uma função em Python que resulta uma lista com os nomes dos Professores que nunca reprovaram um aluno. Faça um programa para testar sua função.
14.	Escreva uma função em Python que, dada a matrícula de um professor, resulte a quantidade de alunos que ele já reprovou em sua carreira de professor. Faça um programa para testar sua função.
15.	Escreva uma função em Python que resulte uma lista com os RAs dos alunos que não têm matrícula em um ano e semestre dados. Faça um programa para testar sua função.
16.	Escreva uma função em Python que resulte uma lista com os RAs dos alunos que têm ingresso em mais de um curso. Faça um programa para testar sua função.
17.	Escreva uma função em Python que resulte a quantidade de alunos de um curso. Faça um programa para testar sua função.
18.	Escreva uma função em Python que resulte uma lista com os RAs dos aluno que estão sem matrícula no semestre atual. Faça um programa para testar sua função.
19.	Escreva uma função em Python que resulte uma lista com os códigos das disciplinas de um curso cursadas e aprovadas por um aluno. Faça um programa para testar sua função.
20.	Escreva uma função em Python que resulte uma lista com os códigos das disciplinas de um curso que ainda precisam ser cursadas por um aluno. Faça um programa para testar sua função.
'''