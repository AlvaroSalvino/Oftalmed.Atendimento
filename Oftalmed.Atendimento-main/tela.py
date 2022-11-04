import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        #Layout
        layout = [
            [sg.Text('Nome',size=(5,0)),sg.Input(size=(15,0),key='nome')],
            [sg.Text('Qual o CONVENIO?')],
            [sg.Checkbox('SUS',key='sus'),sg.Checkbox('IAPEP',key='iapep'),sg.Checkbox('INTERMED',key='intermed'),sg.
            Checkbox('CAAPI',key='caapi'),sg.Checkbox('Sul-America',key='sulamerica'),sg.Checkbox('UNIMED',key='unimed'),sg.Checkbox('PARTICULAR',key=('particular')),sg.Checkbox('IPMT',key=('ipmt'))],
            [sg.Text('Qual o MEDICO?')],
            [sg.Checkbox('Dr.Samuel',key='samuel'),sg.Checkbox('Dra.Lorena',key='lorena'),sg.Checkbox('Dr.Fernando',key='fernando'),sg.Checkbox('Dra.Rossana',key='rossana'),sg.Checkbox('Dr.Daniel',key='daniel'),sg.Checkbox('Dra.Kassandra',key='kassandra'),sg.Checkbox('Dr.Helton',key='helton'),sg.Checkbox('Dra.Natalia',key='natalia'),sg.Checkbox('Dr.Eduardo',key='eduardo')],
            [sg.Text('Insira a data',size=(10,0)),sg.Input(size=(15,0),key='data')],
            [sg.Text('Qual HORARIO?')],
            [sg.Checkbox('Manhã',key='manha'),sg.Checkbox('Tarde',key='tarde')],
            [sg.Button('CONFIRMAR')],
            [sg.Output(size=(150,10))]
        ]
        #Janela
        janela = sg.Window("Oftalmed Atendimento").Layout(layout)
        #Dados da Tela
        self.button, self.values = janela.Read()

    def Iniciar(self):
        while True:
            if sg.WINDOW_CLOSED == True:
                break
            nome = self.values['nome']
            convenio_sus = self.values['sus']
            convenio_iapep = self.values['iapep']
            convenio_intermed = self.values['intermed']
            convenio_ipmt = self.values['ipmt']
            convenio_caapi = self.values['caapi']
            convenio_sulamerica = self.values['sulamerica']
            convenio_unimed = self.values['unimed']
            convenio_particular = self.values['particular']
            medico_samuel = self.values['samuel']
            medico_lorena = self.values['lorena']
            medico_fernando = self.values['fernando']
            medico_rossana = self.values['rossana']
            medico_daniel = self.values['daniel']
            medico_kassandra = self.values['kassandra']
            medico_helton = self.values['helton']
            medico_natalia = self.values['natalia']
            medico_eduardo = self.values['eduardo']
            horario_manha = self.values['manha']
            horario_tarde = self.values['tarde']
            data = self.values['data']
            if medico_samuel == True:
                medico = 'Samuel'
            elif medico_lorena == True:
                medico = 'Lorena'
            elif medico_fernando == True:
                medico = 'Fernando'
            elif medico_rossana == True:
                medico = 'Rossana'
            elif medico_daniel == True:
                medico = 'Daniel'
            elif medico_kassandra == True:
                medico = 'Kassandra'
            elif medico_helton == True:
                medico = 'Helton'
            elif medico_natalia == True:
                medico = 'Natalia'
            elif medico_eduardo == True:
                medico = 'Eduardo'
            if horario_manha == True:
                hora = '07:30'
            if horario_tarde == True:
                hora = '14:00'
            if convenio_sus == True:
                convenio = 'SUS'
            if convenio_caapi == True:
                convenio = 'CAAPI'
            if convenio_iapep == True:
                convenio = 'IAPEP'
            if convenio_intermed == True:
                convenio = 'INTERMED'
            if convenio_particular == True:
                convenio = 'PARTICULAR'
            if convenio_sulamerica == True:
                convenio = 'SUL-AMERICA'
            if convenio_ipmt == True:
                convenio = 'IPMT'

            print(f'''Sr(a) {nome}, a Clínica Oftalmed informa:
    Sua consulta está marcada para dia {data}/11/2022, às {hora}, com Dr(a) {medico}.
    *obs.*: Atendimento por ordem de chegada.
    Endereço: Rua Coelho de Resende, Nº248, Centro-Sul,
    Ponto de referência: Ao lado da panificadora *MODELO*.''')
            print(f'O convenio é {convenio}.')

tela = TelaPython()
tela.Iniciar()
