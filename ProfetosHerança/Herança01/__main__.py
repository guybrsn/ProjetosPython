from rich import print, inspect
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario

def main():
    alu1 = Aluno("Maria Eduarda", 19, "Contabilidade", "Segundo Semestre")
    alu1.fazer_aniversario()
    inspect(alu1)

    prof1 = Professor("João Carlos", 56, "Quimica", "Doutor")
    prof1.fazer_aniversario()
    prof1.fazer_aniversario()
    prof1.fazer_aniversario()
    inspect(prof1, methods=True)


    fun1 = Funcionario("Guilherme", 26, "Analista Finaceiro", "Financeiro")
    fun1.bater_ponto()
    inspect(fun1)
# tem que ser o __name__ 
if __name__ == "__main__":
    main()