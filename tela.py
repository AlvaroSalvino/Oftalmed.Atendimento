import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        #Layout
        layout = [
            [sg.Text('Nome',size=(5,0)),sg.Input(size=(15,0),key='nome')],
            [sg.Text('Qual o CONVENIO?')],
            [sg.Checkbox('SUS',key='sus'),sg.Checkbox('IAPEP',key='iapep'),sg.Checkbox('INTERMED',key='intermed'),sg.
            Checkbox('CAAPI',key='caapi'),sg.Checkbox('Sul-America',key='sulamerica'),sg.Checkbox('UNIMED',key='unimed'),sg.Checkbox('PARTICULAR',key=('particular'))],
            [sg.Button('Enviar Dados')]
        ]
        #Janela
        janela = sg.Window("Oftalmed Atendimento").Layout(layout)
        #Dados da Tela
        self.button, self.values = janela.Read()

    def Iniciar(self):
        nome = self.values['nome']
        convenio_sus = self.values['sus']
        convenio_iapep = self.values['iapep']
        convenio_intermed = self.values['intermed']
        convenio_caapi = self.values['caapi']
        convenio_sulamerica = self.values['sulamerica']
        convenio_unimed = self.values['unimed']
        convenio_particular = self.values['particular']
        print(f'nome: {nome}')
        print(f'convenio sus: {convenio_sus}')
        print(f'convenio iapep: {convenio_iapep}')
        print(f'convenio intermed: {convenio_intermed}')
        print(f'convenio caapi: {convenio_caapi}')
        print(f'convenio sulamerica: {convenio_sulamerica}')
        print(f'convenio unimed: {convenio_unimed}')
        print(f'convenio particular: {convenio_particular}')

tela = TelaPython()
tela.Iniciar()