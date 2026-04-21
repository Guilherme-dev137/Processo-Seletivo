import sqlite3


def criar_banco():
    conn = sqlite3.connect("pacientes.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            urgencia TEXT NOT NULL,
            chegada TEXT NOT NULL,
            atendimento TEXT
        )
        """
    )

    conn.commit()
    conn.close()


def salvar_pacientes(lista):
    conn = sqlite3.connect("pacientes.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM pacientes")

    for paciente in lista:
      cursor.execute(
          """
          INSERT INTO pacientes (nome, idade, urgencia, chegada, atendimento)
          VALUES (?, ?, ?, ?, ?)
          """,
          (
              paciente["nome"],
              paciente["idade"],
              paciente["urgencia"],
              paciente["chegada"],
              paciente.get("atendimento")
          )
      )

    conn.commit()
    conn.close()


def listar_pacientes():
    conn = sqlite3.connect("pacientes.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, nome, idade, urgencia, chegada, atendimento FROM pacientes"
    )

    linhas = cursor.fetchall()
    conn.close()

    pacientes = []

    for linha in linhas:
        pacientes.append(
            {
                "id": linha[0],
                "nome": linha[1],
                "idade": linha[2],
                "urgencia": linha[3],
                "chegada": linha[4],
                "atendimento": linha[5]
            }
        )

    return pacientes
