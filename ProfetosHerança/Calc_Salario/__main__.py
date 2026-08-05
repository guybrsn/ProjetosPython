from Funcionarios import * 

def main():
    fun = FuncionarioHorista("Guilherme Da Silva", 45)
    fun.Calc_Sal()
    fun.Analisar_Sal()

    fun02 = FuncionarioMensalista("Maria Eduarda", 1900)
    fun02.Calc_Sal()
    fun02.Analisar_Sal()

if __name__ == "__main__":
    main()