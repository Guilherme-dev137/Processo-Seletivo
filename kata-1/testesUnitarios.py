import unittest
from ordenarFila import organizar_pacientes


class TestOrganizacaoPacientes(unittest.TestCase):

    def test_prioridade_critica(self):
        pacientes = [
            {"nome": "A", "idade": 30, "urgencia": "alta", "chegada": "10:00"},
            {"nome": "B", "idade": 30, "urgencia": "critica", "chegada": "11:00"},
        ]

        resultado = organizar_pacientes(pacientes)

        self.assertEqual(resultado[0]["nome"], "B")


    def test_idoso_media_vira_alta(self):
        pacientes = [
            {"nome": "A", "idade": 65, "urgencia": "media", "chegada": "10:00"},
        ]

        resultado = organizar_pacientes(pacientes)

        self.assertEqual(resultado[0]["urgencia"], "alta")


    def test_menor_sobe_prioridade(self):
        pacientes = [
            {"nome": "A", "idade": 15, "urgencia": "baixa", "chegada": "10:00"},
        ]

        resultado = organizar_pacientes(pacientes)

        self.assertEqual(resultado[0]["urgencia"], "media")


    def test_ordem_chegada_mesma_urgencia(self):
        pacientes = [
            {"nome": "A", "idade": 30, "urgencia": "alta", "chegada": "10:00"},
            {"nome": "B", "idade": 30, "urgencia": "alta", "chegada": "09:00"},
        ]

        resultado = organizar_pacientes(pacientes)

        self.assertEqual(resultado[0]["nome"], "B")


if __name__ == "__main__":
    unittest.main()