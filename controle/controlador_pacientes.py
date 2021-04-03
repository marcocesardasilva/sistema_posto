from limite.tela_pacientes import TelaPacientes
from entidade.paciente import Paciente
from controle.controlador_agendamentos import ControladorAgendamentos


class ControladorPacientes():

    def __init__(self, controlador_sistema):
        self.__pacientes = []
        self.__tela_pacientes = TelaPacientes(self)
        self.__controlador_sistema = controlador_sistema
        try:
            self.__controlador_agendamentos = self.__controlador_sistema.controlador_agendamentos
        except AttributeError:
            self.__controlador_sistema.controlador_agendamentos = ControladorAgendamentos(self.__controlador_sistema)
            self.__controlador_agendamentos = self.__controlador_sistema.controlador_agendamentos
        self.__mantem_tela_aberta = True

    @property
<<<<<<< HEAD
    def controlador_sistema(self):
        return self.__controlador_sistema
=======
    def pacientes(self):
        return self.__pacientes
>>>>>>> 49ac2c44aefa23d7cba4e4e51e2366cc1fa319fe

    def cadastrar_paciente(self):
        dados_paciente = self.__tela_pacientes.pega_dados_paciente()
        paciente = Paciente(dados_paciente["nome"], dados_paciente["cpf"], dados_paciente["data_nascimento"])
        self.__pacientes.append(paciente)

    def editar_paciente(self):
        paciente_editar = self.get_paciente()
        dados_editar = self.__tela_pacientes.pega_dados_paciente_edicao()
        for paciente in self.__pacientes:
            if paciente_editar == paciente:
                paciente.nome = dados_editar["nome"]
                paciente.data_nascimento = dados_editar["data_nascimento"]

    def consultar_paciente(self):
        paciente_consultar = self.get_paciente()
        for paciente in self.__pacientes:
            if paciente_consultar == paciente:
                self.__tela_pacientes.mostrar_paciente(
                    {"nome": paciente.nome,
                     "cpf": paciente.cpf,
                     "data_nascimento": paciente.data_nascimento}
                )

    def get_paciente(self):
        cpf = self.__tela_pacientes.selecionar_paciente()
        for paciente in self.__pacientes:
            if cpf == paciente.cpf:
                return paciente

    def listar_pacientes(self):
        for paciente in self.__pacientes:
            self.__tela_pacientes.mostrar_paciente(
                {"nome": paciente.nome,
                 "cpf": paciente.cpf,
                 "data_nascimento": paciente.data_nascimento}
            )

    def listar_pacientes_nao_agendados(self):
        pacientes_agendados = []
        self.__controlador_agendamentos = self.__controlador_sistema.controlador_agendamentos
        for agendamento in self.__controlador_agendamentos.agendamentos:
            for paciente in self.__pacientes:
                if agendamento.paciente == paciente:
                    pacientes_agendados.append(paciente)
        for paciente in self.__pacientes:
            if paciente not in pacientes_agendados:
                self.__tela_pacientes.mostrar_paciente(
                    {"nome": paciente.nome,
                    "cpf": paciente.cpf,
                    "data_nascimento": paciente.data_nascimento
                    })

    def listar_pacientes_primeira_dose(self):
        #self.__controlador_agendamentos = self.__controlador_sistema.controlador_agendamentos
        for agendamento in self.__controlador_agendamentos.agendamentos:
            if agendamento.dose == 1:
                #if agendamento.aplicada == True:
                self.__tela_pacientes.mostrar_paciente(
                    {"nome": agendamento.paciente.nome,
                     "cpf": agendamento.paciente.cpf,
                     "data_nascimento": agendamento.paciente.data_nascimento
                     })
            # elif agendamento.dose == 2 and agendamento.aplicada == False:
            #     self.__tela_pacientes.mostrar_paciente(
            #         {"nome": agendamento.paciente.nome,
            #          "cpf": agendamento.paciente.cpf,
            #          "data_nascimento": agendamento.paciente.data_nascimento
            #          })

    
    def listar_pacientes_segunda_dose(self):
        self.__controlador_agendamentos = self.__controlador_sistema.controlador_agendamentos
        for agendamento in self.__controlador_agendamentos.agendamentos:
            if agendamento.dose == 2:
                # if agendamento.aplicada == True:
                self.__tela_pacientes.mostrar_paciente(
                    {"nome": agendamento.paciente.nome,
                     "cpf": agendamento.paciente.cpf,
                     "data_nascimento": agendamento.paciente.data_nascimento
                     }
                )

    def retorna_tela_principal(self):
        self.__mantem_tela_aberta = False

    def abre_tela(self):
        self.__mantem_tela_aberta = True
        lista_opcoes = {1: self.cadastrar_paciente,
                        2: self.editar_paciente,
                        3: self.consultar_paciente,
                        4: self.listar_pacientes,
                        5: self.listar_pacientes_nao_agendados,
                        6: self.listar_pacientes_primeira_dose,
                        7: self.listar_pacientes_segunda_dose(),
                        0: self.retorna_tela_principal}

        while self.__mantem_tela_aberta:
            lista_opcoes[self.__tela_pacientes.tela_opcoes()]()
