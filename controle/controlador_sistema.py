from limite.tela_sistema import TelaSistema
from controle.controlador_pacientes import ControladorPacientes
from controle.controlador_enfermeiros import ControladorEnfermeiros
from controle.controlador_vacinas import ControladorVacinas
from controlador_agendamentos import ControladorAgendamentos


class ControladorSistema:

  def __init__(self):
    self.__controlador_pacientes = ControladorPacientes(self)
    self.__controlador_enfermeiros = ControladorEnfermeiros(self)
    self.__controlador_vacinas = ControladorVacinas(self)
    self.__controlador_agendamentos = ControladorAgendamentos(self)
    self.__tela_sistema = TelaSistema()
  
  def inicializa_sistema(self):
    self.abre_tela()
  
  def cadastra_livros(self):
    pass
    # Chama o controlador de Livros

  def cadastra_amigos(self):
    # Chama o controlador de Amigos
    self.__controlador_amigos.abre_tela()

  def cadastra_emprestimos(self):
    pass
    # Chama o controlador de Emprestimos

  def encerra_sistema(self):
    exit(0)


  def abre_tela(self):

    lista_opcoes = {1: self.cadastra_livros, 2: self.cadastra_amigos, 3: self.cadastra_emprestimos, 0: self.encerra_sistema}

    while True:

      opcao_escolhida = self.__tela_sistema.tela_opcoes()

      funcao_escolhida = lista_opcoes[opcao_escolhida]

      funcao_escolhida()
    
    