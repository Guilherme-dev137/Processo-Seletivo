# Importação do script para criar o banco de dados
from criarDB import criar_banco

# Importação da função para salvar os valores no banco de dados
from criarDB import salvar_pacientes

# Importação da função para coletar as informações do banco de dados
from criarDB import listar_pacientes

# Importação do datetime para trabalhar com o campo "chegada"
from datetime import datetime

# Criação do banco de dados
criar_banco();

# Informações dos pacientes cadastrados no dia para atendimento
pacientes = [
    {"nome": "Ana", "idade": 25, "urgencia": "media", "chegada": "12:30", "atendimento": "null"},
    {"nome": "Lucas", "idade": 20, "urgencia": "alta", "chegada": "13:00", "atendimento": "null"},
    {"nome": "João", "idade": 50, "urgencia": "critica", "chegada": "15:00", "atendimento": "null"},
    {"nome": "Maria", "idade": 30, "urgencia": "baixa", "chegada": "14:00", "atendimento": "null"},
    {"nome": "Antonio", "idade": 23, "urgencia": "alta", "chegada": "12:20", "atendimento": "null"},
    {"nome": "Jose", "idade": 63, "urgencia": "media", "chegada": "15:20", "atendimento": "null"},
    {"nome": "Eduardo", "idade": 15, "urgencia": "baixa", "chegada": "16:40", "atendimento": "null"},
];

for p in pacientes:
    p["chegada"] = datetime.strptime(p["chegada"], "%H:%M")

# Função para realizar a organização dos pacientes
def organizar_pacientes(lista):
    prioridade = {
        "critica": 0,
        "alta": 1,
        "media": 2,
        "baixa": 3
    }

    def ajustar_prioridade(p):
        urgencia_original = p["urgencia"]

        # Regra 4: idoso(+60) com média vira alta
        if p.get("idade", 0) >= 60 and urgencia_original == "media":
            p["urgencia"] = "alta"

        # Regra 5: menor de 18 sobe um nível
        elif p.get("idade", 0) < 18:
            if urgencia_original == "baixa":
                p["urgencia"] = "media"
            elif urgencia_original == "media":
                p["urgencia"] = "alta"
            elif urgencia_original == "alta":
                p["urgencia"] = "critica"

        return prioridade.get(p["urgencia"], 99)
    


    return sorted(
        lista,
        key=lambda p: (ajustar_prioridade(p), p["chegada"])
    )

# Chamada da função, valores do filtro serão armazenadas em outra variável para depois ser impresso na tela
resultado = organizar_pacientes(pacientes);

# Execução da função para salvar os valores dos pacientes no banco
salvar_pacientes(resultado);

# Impressão dos resultados sem tratamento
# for paciente in resultado:
#     paciente_exibicao = paciente.copy()
#     paciente_exibicao["chegada"] = paciente["chegada"].strftime("%H:%M")
#     print(paciente_exibicao);

# Impressão dos resultados mais organizados
# for p in resultado:
#     print(f"Nome: {p['nome']} | Idade: {p['idade']} | Urgência: {p['urgencia']} | Chegada: {p['chegada'].strftime('%H:%M')}");

# Impressão dos resultados em forma de tabelas
print(f"{'Nome': <10} {'Idade': <6} {'Urgência':<10} {'Chegada':<8}")
print("-" * 40)

for p in resultado:
    print(f"{p['nome']:<10} {p['idade']:<6} {p['urgencia']:<10} {p['chegada'].strftime('%H:%M'):<8}")
