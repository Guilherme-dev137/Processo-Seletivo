import sqlite3;

# Função para realizar a criação do banco de dados
def criar_banco():
    conn = sqlite3.connect("pacientes.db");
    cursor = conn.cursor();

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pacientes (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT,
                   idade INTEGER
                   urgencia TEXT
                   chegada TEXT
                   atendimento TEXT
                   )
    """);

    conn.commit();
    conn.closed();

# Função para realizar o salvamento dos dados no banco de dados
def salvar_pacientes(lista):
    conn = sqlite3.connect("pacientes.db");
    cursor = conn.cursor();

    # Comando para limpar o banco de dados e salvar as novas informações
    cursor.execute("DELETE FROM pacientes");

    for p in lista:
        cursor.execute("""
            INSERT INTO pacientes (nome, idade, urgencia, chegada, atendimento)
            VALUES(?, ?, ?, ?, ?, ?)
        """, (p["nome"], p["idade"], p["urgencia"], p["chegada"]))
    
    conn.commit();
    conn.close();

# Função coletar os dados já existentes no banco de dados
def listar_pacientes():
    conn = sqlite3.connect("pacientes.db");
    cursor = conn.cursor();

    cursor.execute("SELECT id, nome, idade, urgencia, chegada, atendimento FROM pacientes");

    linhas = cursor.fetchall();

    pacientes = [];

    for linha in linhas:
        paciente = {
            "id": linha[0],
            "nome": linha[1],
            "idade": linha[2],
            "urgencia": linha[3],
            "chegada": linha[4],
            "atendimento": linha[5]
        }
        pacientes.append(paciente);

    conn.close()

    return pacientes;

