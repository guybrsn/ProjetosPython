import sqlite3
from datetime import datetime

def conetar():
    conexao = sqlite3.connect("dados.db")
    return conexao

def criarTabela():
    conexao = conetar()
    cursor = conexao.cursor()
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS pessoas(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    dataNascimento DATE NOT NULL,
                    cargo TEXT NOT NULL
                    )
                """)

    conexao.commit()
    conexao.close()


def cadastrarPessoas(nome='', dataNascimento='', cargo=''):
    nome = str(input("Qual o nome da pessoa: "))
    dataNascimento = input("Qual a data de nascimento (DD/MM/AAAA) --> ")
    cargo =str(input("Qual e o cargo: "))

    try:
        dataFormatada = datetime.strptime(dataNascimento, "%d/%m/%Y")
        dataNascimento = datetime.strftime(dataFormatada, "%d/%m/%Y")
    except ValueError:
        print("Valor digitado incorreto tente (DD/MM/AAAA)")

    conexao = conetar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO pessoas (nome, dataNascimento, cargo) VALUES(?, ?, ?)", 
                    (nome, dataNascimento, cargo)
                   )
    conexao.commit()
    conexao.close()

    print("Cadastro realizado com sucesso !")
    return nome, dataNascimento, cargo


def listarPessoas():
    conexao = conetar()
    cursor = conexao.cursor()
    cursor.execute("""
                    SELECT nome, dataNascimento, cargo FROM pessoas
                """)
    registros = cursor.fetchall()

    print("Todos os registro de pessoas \n")
    for registro in registros:
        print(registro[0], registro[1], registro[2])

    conexao.close()

    return registros


def buscarPessoa(nome):
    conexao = conetar()
    cursor = conexao.cursor()
    cursor.execute("""
                    SELECT nome, dataNascimento, cargo FROM pessoas
                """)
    resultados = cursor.fetchall()

    conexao.close()

    validacao = False

    for resultado in resultados:
        if resultado[0] == nome:
            print()
            print("-" * 50)
            print("                 DADOS CADASTRADOS")
            print("-" * 50)
            print(f"""Nome: {resultado[0]}
Data Nascimento: {resultado[1]}
Cargo Empresa: {resultado[2]}
        """)
            validacao = True
            break

    for resultado in resultados:
        if resultado[0] != nome and validacao == False:
            print()
            print("Pessoa não cadastrada !")
        break

    return nome