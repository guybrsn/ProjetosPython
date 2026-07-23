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

    return nome, dataNascimento, cargo


def listarPessoas(nome, dataNascimento, cargo):
    ...
