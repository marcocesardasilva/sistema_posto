from limite.tela_agendamentos import TelaAgendamentos
from entidade.agendamento import Agendamento
from datetime import datetime as datetime


class ControladorAgendamentos():

    def __init__(self, controlador_sistema):
        self.__agendamentos = []
        self.__tela_agendamentos = TelaAgendamentos(self)
        self.__controlador_sistema = controlador_sistema
        self.__controlador_enfermeiros = self.__controlador_sistema.controlador_enfermeiros
        self.__controlador_pacientes = self.__controlador_sistema.controlador_pacientes
        self.__controlador_vacinas = self.__controlador_sistema.controlador_vacinas
        self.__mantem_tela_aberta = True

    def cadastrar_agendamento(self):
        dados_agendamento = self.__tela_agendamentos.pegar_dados_cadastrar()
        while True:
            enfermeiro = self.__controlador_enfermeiros.get_enfermeiro()
            if enfermeiro is None:
                break
            if enfermeiro.status == "Inativo":
                self.__controlador_enfermeiros.enfermeiro_inativo()
                break
            paciente = self.__controlador_pacientes.get_paciente()
            if paciente is None:
                break
            vacina = self.__controlador_vacinas.get_vacina()
            if vacina is None:
                break
            data_hora_agendamento = datetime.strptime(
                dados_agendamento["data_hora_agendamento"],
                "%d/%m/%Y %H:%M"
            )

            agendamento = Agendamento(
                enfermeiro,
                paciente,
                vacina,
                data_hora_agendamento,
                dados_agendamento["dose"]
            )
            self.__agendamentos.append(agendamento)
            self.__tela_agendamentos.agendamento_cadastrado()
            break

    @property
    def agendamentos(self):
        return self.__agendamentos

    def get_agendamento(self):
        dose = self.__tela_agendamentos.selecionar_agendamento()
        paciente = self.__controlador_pacientes.get_paciente()
        if paciente is None:
            return None
        for agendamento in self.__agendamentos:
            if dose == agendamento.dose and paciente.cpf == agendamento.paciente.cpf:
                return agendamento
    
    def consultar_agendamento(self):
        agendamento = self.get_agendamento()
        if agendamento is None:
            return None
        status = "Aguardando aplicação"
        if agendamento.aplicada is True:
            status = "Vacina já aplicada"
        self.__tela_agendamentos.mostrar_agendamento({
            "enfermeiro": agendamento.enfermeiro.nome,
            "paciente": agendamento.paciente.nome,
            "vacina": agendamento.vacina.fabricante,
            "data_hora_agendamento": agendamento.data_hora_agendamento,
            "dose": agendamento.dose,
            "status": status
        })

    def editar_agendamento(self):
        agendamento = self.get_agendamento()
        if agendamento is None:
            return None
        dados_agendamento = self.__tela_agendamentos.pegar_dados_editar()
        agendamento.enfermeiro = self.__controlador_enfermeiros.get_enfermeiro()
        agendamento.paciente = self.__controlador_pacientes.get_paciente()
        agendamento.vacina = self.__controlador_vacinas.get_vacina()
        agendamento.data_hora_agendamento = datetime.strptime(
            dados_agendamento["data_hora_agendamento"],
            "%d/%m/%Y %H:%M"
        )
        agendamento.dose = dados_agendamento["dose"]
        agendamento.aplicada = dados_agendamento["aplicada"]
        self.__tela_agendamentos.agendamento_editado()

    def aplicar_vacina(self):
        agendamento = self.get_agendamento()
        agendamento.aplicada = True
        self.__tela_agendamentos.vacina_aplicada()

    def remover_agendamento(self):
        agendamento = self.get_agendamento()
        del(self.__agendamentos[agendamento])
        self.__tela_agendamentos.agendamento_removido()

    def listar_agendamentos_abertos(self):
        for agendamento in self.__agendamentos:
            if agendamento.aplicada == True:
                self.__tela_agendamentos.mostrar_lista_agendamentos({
                    "enfermeiro": agendamento.enfermeiro.nome,
                    "paciente": agendamento.paciente.nome,
                    "vacina": agendamento.vacina.fabricante,
                    "data_hora_agendamento": agendamento.data_hora_agendamento,
                    "dose": agendamento.dose
                })

    def listar_aplicacoes_efetivadas(self):
        for agendamento in self.__agendamentos:
            if agendamento.aplicada == False:
                self.__tela_agendamentos.mostrar_lista_agendamentos({
                    "enfermeiro": agendamento.enfermeiro.nome,
                    "paciente": agendamento.paciente.nome,
                    "vacina": agendamento.vacina.fabricante,
                    "data_hora_agendamento": agendamento.data_hora_agendamento,
                    "dose": agendamento.dose
                })

    def retorna_tela_principal(self):
        self.__mantem_tela_aberta = False

    def abre_tela(self):
        self.__mantem_tela_aberta = True
        lista_opcoes = {
            1: self.cadastrar_agendamento,
            2: self.consultar_agendamento,
            3: self.editar_agendamento,
            4: self.aplicar_vacina,
            5: self.remover_agendamento,
            6: self.listar_agendamentos_abertos,
            7: self.listar_aplicacoes_efetivadas,
            0: self.retorna_tela_principal
        }

        while self.__mantem_tela_aberta:
            lista_opcoes[self.__tela_agendamentos.tela_opcoes()]()
