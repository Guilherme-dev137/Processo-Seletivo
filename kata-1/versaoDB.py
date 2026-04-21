from datetime import datetime

from criarDB import criar_banco
from criarDB import listar_pacientes
from criarDB import salvar_pacientes


criar_banco()

pacientes = [
    {
        "nome": "Ana",
        "idade": 25,
        "urgencia": "media",
        "chegada": "12:30",
        "atendimento": None
    },
    {
        "nome": "Lucas",
        "idade": 20,
        "urgencia": "alta",
        "chegada": "13:00",
        "atendimento": None
    },
    {
        "nome": "Joao",
        "idade": 50,
        "urgencia": "critica",
        "chegada": "15:00",
        "atendimento": None
    },
    {
        "nome": "Maria",
        "idade": 30,
        "urgencia": "baixa",
        "chegada": "14:00",
        "atendimento": None
    },
    {
        "nome": "Antonio",
        "idade": 23,
        "urgencia": "alta",
        "chegada": "12:20",
        "atendimento": None
    },
    {
        "nome": "Jose",
        "idade": 63,
        "urgencia": "media",
        "chegada": "15:20",
        "atendimento": None
    },
    {
        "nome": "Eduardo",
        "idade": 15,
        "urgencia": "baixa",
        "chegada": "16:40",
        "atendimento": None
    }
]

for paciente in pacientes:
    paciente["chegada"] = datetime.strptime(paciente["chegada"], "%H:%M")


def organizar_pacientes(lista):
    prioridade = {
        "critica": 0,
        "alta": 1,
        "media": 2,
        "baixa": 3
    }

    def ajustar_prioridade(paciente):
        urgencia_original = paciente["urgencia"]

        if paciente.get("idade", 0) >= 60 and urgencia_original == "media":
            paciente["urgencia"] = "alta"
        elif paciente.get("idade", 0) < 18:
            if urgencia_original == "baixa":
                paciente["urgencia"] = "media"
            elif urgencia_original == "media":
                paciente["urgencia"] = "alta"
            elif urgencia_original == "alta":
                paciente["urgencia"] = "critica"

        return prioridade.get(paciente["urgencia"], 99)

    return sorted(lista, key=lambda paciente: (ajustar_prioridade(paciente), paciente["chegada"]))


resultado = organizar_pacientes(pacientes)

pacientes_para_banco = []
for paciente in resultado:
    pacientes_para_banco.append(
        {
            "nome": paciente["nome"],
            "idade": paciente["idade"],
            "urgencia": paciente["urgencia"],
            "chegada": paciente["chegada"].strftime("%H:%M"),
            "atendimento": paciente["atendimento"]
        }
    )

salvar_pacientes(pacientes_para_banco)

pacientes_salvos = listar_pacientes()

print(f"{'ID':<4} {'Nome':<10} {'Idade':<6} {'Urgencia':<10} {'Chegada':<8}")
print("-" * 46)

for paciente in pacientes_salvos:
    print(
        f"{paciente['id']:<4} "
        f"{paciente['nome']:<10} "
        f"{paciente['idade']:<6} "
        f"{paciente['urgencia']:<10} "
        f"{paciente['chegada']:<8}"
    )
