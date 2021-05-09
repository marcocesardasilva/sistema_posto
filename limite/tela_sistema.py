import PySimpleGUI as sg

class TelaSistema:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema

    def tela_opcoes(self):
        sg.theme('Default')
        layout = [
            [sg.Text('Selecione a opção desejada', size=(30, 1))],
            [sg.Button('Enfermeiros', size=(30, 2), key='1')],
            [sg.Button('Pacientes', size=(30, 2), key='2')],
            [sg.Button('Vacinas', size=(30, 2), key='3')],
            [sg.Button('Agendamentos', size=(30, 2), key='4')],
            [sg.Button('Encerrar Sistema', size=(30, 2), key='0')]
        ]
        window = sg.Window(
            'Sistema de agendamento de vacinações',
            size=(800, 480),
            #element_justification="center"
            ).Layout(layout)
        botao, _ = window.Read()
        if botao == sg.WIN_CLOSED:
            window.close()
            return 0
        opcao = int(botao)
        window.close()
        return opcao
