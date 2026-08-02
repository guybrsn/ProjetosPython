from rich import print, inspect
from classes import Pessoa, Aluno, Professor, Funcionario

def main():
    alu1 = Aluno("Maria Eduarda", 19, "Contabilidade", "Segundo Semestre")
    alu1.fazer_aniversario()
    alu1.fazer_matricula()
    alu1.estudar()
    inspect(alu1, methods=True)

    prof1 = Professor("João Carlos", 56, "Quimica", "Doutor")
    prof1.fazer_aniversario()
    #prof1.estudar()
    #inspect(prof1, methods=True)


    fun1 = Funcionario("Guilherme", 26, "Analista Finaceiro", "Financeiro")
    #fun1.bater_ponto()
    #fun1.estudar()
    #inspect(fun1)

# tem que ser o __name__ 
if __name__ == "__main__":
    main()