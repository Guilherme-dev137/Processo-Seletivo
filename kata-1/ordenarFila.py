# Importação do datetime para trabalhar com o campo "chegada"
from datetime import datetime

# Informações dos pacientes cadastrados no dia para atendimento
pacientes = [
    {"nome": "Ana", "idade": 25, "urgencia": "media", "chegada": "12:30"},
    {"nome": "Lucas", "idade": 20, "urgencia": "alta", "chegada": "13:00"},
    {"nome": "João", "idade": 50, "urgencia": "critica", "chegada": "15:00"},
    {"nome": "Maria", "idade": 30, "urgencia": "baixa", "chegada": "14:00"},
    {"nome": "Antonio", "idade": 23, "urgencia": "alta", "chegada": "12:20"},
    {"nome": "Jose", "idade": 63, "urgencia": "media", "chegada": "15:20"},
    {"nome": "Eduardo", "idade": 15, "urgencia": "baixa", "chegada": "16:40"},
];

for p in pacientes:
    p["chegada"] = datetime.strptime(p["chegada"], "%H:%M")

# Função para realizar a organização a ordem dos pacientes
def organizar_pacientes(lista):
    prioridade = {
        "critica": 0,
        "alta": 1,
        "media": 2,
        "baixa": 3
    }

    def ajustar_prioridade(p):
        urgencia_original = p["urgencia"]

        # Regra 4: idoso com média vira alta
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
