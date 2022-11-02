#Variaveis
#============================================================

print('=-=-=-=-=-=-=-=-=-= OFTALMED ATENDIMENTO =-=-=-=-=-=-=-=-=-=')
print('=-=' *20)
while True:
    opcao = str(input('''[1]NOME
[2]CONVENIOS
[3]HISTÓRICO
Opção: '''))
    if opcao == '1':
        NOME = str(input('INSIRA O 1º NOME DO PACIENTE: ')).upper()
        CONVENIO = str(input('''[1]SUS
[2]IAPEP
[3]INTERMED
[4]CAAPI
[5]SUL-AMERICA
[6]UNIMED
Opção: '''))
        if CONVENIO == '1':
            CONVENIO = 'SUS'
            DATA = str(input('Insira o dia: '))
            HORAS = str(input('''[1]MANHÃ
ou
[2]TARDE?
Opção: '''))
            if HORAS == '1':
                HORAS = '07:30'
            if HORAS == '2':
                HORAS = '14:00'
            MEDICO = str(input('''QUAL O MÉDICO?
[1]Dr.Samuel
[2]Dra.Lorena
[3]Dra.Rossana
[4]Dr.Fernando
[5]Dr.Daniel
Opção: '''))
            if MEDICO == '1':
                MEDICO = 'Samuel'
            if MEDICO == '2':
                MEDICO = 'Lorena'
            if MEDICO == '3':
                MEDICO = 'Rossana'
            if MEDICO == '4':
                MEDICO = 'Fernando'
            if MEDICO == '5':
                MEDICO = 'Daniel'
            print(f'''Sr(a) {NOME}, a Clínica Oftalmed informa:
Sua consulta está marcada para dia {DATA}/11/2022, às {HORAS}, com Dr(a). {MEDICO}.
*obs.*: Atendimento por ordem de chegada.
Endereço: Rua Coelho de Resende, Nº248, Centro-Sul,
Ponto de referência: Ao lado da panificadora *MODELO*.''')
            print('=-=' *20)
            print(f'ATENDIMENTO PELO {CONVENIO}')
            print('=-=' *20)
        if CONVENIO == '2':
            CONVENIO = 'IAPEP'
            DATA = str(input('Insira o dia: '))
            HORAS = str(input('''[1]MANHÃ
ou
[2]TARDE?
Opção: '''))
            if HORAS == '1':
                HORAS = '07:30'
            if HORAS == '2':
                HORAS = '14:00'
            MEDICO = str(input('''QUAL O MÉDICO?
[1]Dr.Samuel
[2]Dra.Lorena
[3]Dra.Rossana
[4]Dr.Fernando
[5]Dr.Daniel
Opção: '''))
            if MEDICO == '1':
                MEDICO = 'Samuel'
            if MEDICO == '2':
                MEDICO = 'Lorena'
            if MEDICO == '3':
                MEDICO = 'Rossana'
            if MEDICO == '4':
                MEDICO = 'Fernando'
            if MEDICO == '5':
                MEDICO = 'Daniel'
            print(f'''Sr(a) {NOME}, a Clínica Oftalmed informa:
Sua consulta está marcada para dia {DATA}/11/2022, às {HORAS}, com Dr(a). {MEDICO}.
*obs.*: Atendimento por ordem de chegada.
Endereço: Rua Coelho de Resende, Nº248, Centro-Sul,
Ponto de referência: Ao lado da panificadora *MODELO*.''')
            print('=-=' *20)
            print(f'ATENDIMENTO PELO {CONVENIO}')
            print('=-=' *20)
        if CONVENIO == '3':
            CONVENIO = 'INTERMED'
            DATA = str(input('Insira o dia: '))
            HORAS = str(input('''[1]MANHÃ
ou
[2]TARDE?
Opção: '''))
            if HORAS == '1':
                HORAS = '07:30'
            if HORAS == '2':
                HORAS = '14:00'
            MEDICO = str(input('''QUAL O MÉDICO?
[1]Dr.Samuel
[2]Dra.Lorena
[3]Dra.Rossana
[4]Dr.Fernando
[5]Dr.Daniel
Opção: '''))
            if MEDICO == '1':
                MEDICO = 'Samuel'
            if MEDICO == '2':
                MEDICO = 'Lorena'
            if MEDICO == '3':
                MEDICO = 'Rossana'
            if MEDICO == '4':
                MEDICO = 'Fernando'
            if MEDICO == '5':
                MEDICO = 'Daniel'
            print(f'''Sr(a) {NOME}, a Clínica Oftalmed informa:
Sua consulta está marcada para dia {DATA}/11/2022, às {HORAS}, com Dr(a). {MEDICO}.
*obs.*: Atendimento por ordem de chegada.
Endereço: Rua Coelho de Resende, Nº248, Centro-Sul,
Ponto de referência: Ao lado da panificadora *MODELO*.''')
            print('=-=' *20)
            print(f'ATENDIMENTO PELO {CONVENIO}')
            print('=-=' *20)
        if CONVENIO == '4':
            CONVENIO = 'CAAPI'
            DATA = str(input('Insira o dia: '))
            HORAS = str(input('''[1]MANHÃ
ou
[2]TARDE?
Opção: '''))
        if HORAS == '1':
            HORAS = '07:30'
        if HORAS == '2':
            HORAS = '14:00'
            MEDICO = str(input('''QUAL O MÉDICO?
[1]Dr.Samuel
[2]Dra.Lorena
[3]Dra.Rossana
[4]Dr.Fernando
[5]Dr.Daniel
Opção: '''))
            if MEDICO == '1':
                MEDICO = 'Samuel'
            if MEDICO == '2':
                MEDICO = 'Lorena'
            if MEDICO == '3':
                MEDICO = 'Rossana'
            if MEDICO == '4':
                MEDICO = 'Fernando'
            if MEDICO == '5':
                MEDICO = 'Daniel'
            print(f'''Sr(a) {NOME}, a Clínica Oftalmed informa:
Sua consulta está marcada para dia {DATA}/11/2022, às {HORAS}, com Dr(a). {MEDICO}.
*obs.*: Atendimento por ordem de chegada.
Endereço: Rua Coelho de Resende, Nº248, Centro-Sul,
Ponto de referência: Ao lado da panificadora *MODELO*.''')
            print('=-=' *20)
            print(f'ATENDIMENTO PELO {CONVENIO}')
            print('=-=' *20)
    if opcao == '2':
        CONVENIO = str(input('''[1]SUS
[2]IAPEP
[3]INTERMED
[4]CAAPI
[5]SUL-AMERICA
[6]UNIMED
TECLE 'ENTER' PARA "PARTICULAR"
Opção: '''))
        if CONVENIO == '1':
            CONVENIO = 'SUS'
            NOME = str(input('INSIRA O 1º NOME DO PACIENTE: ')).upper()
            DATA = str(input('Insira o dia: '))
            HORAS = str(input('''[1]MANHÃ
ou
[2]TARDE?
Opção: '''))
            if HORAS == '1':
                HORAS = '07:30'
            if HORAS == '2':
                HORAS = '14:00'
            MEDICO = str(input('''QUAL O MÉDICO?
[1]Dr.Samuel
[2]Dra.Lorena
[3]Dra.Rossana
[4]Dr.Fernando
[5]Dr.Daniel
Opção: '''))
            if MEDICO == '1':
                MEDICO = 'Samuel'
            if MEDICO == '2':
                MEDICO = 'Lorena'
            if MEDICO == '3':
                MEDICO = 'Rossana'
            if MEDICO == '4':
                MEDICO = 'Fernando'
            if MEDICO == '5':
                MEDICO = 'Daniel'
            print(f'''Sr(a) {NOME}, a Clínica Oftalmed informa:
Sua consulta está marcada para dia {DATA}/11/2022, às {HORAS}, com Dr(a). {MEDICO}.
*obs.*: Atendimento por ordem de chegada.
Endereço: Rua Coelho de Resende, Nº248, Centro-Sul,
Ponto de referência: Ao lado da panificadora *MODELO*.''')
            print('=-=' * 20)
            print(f'ATENDIMENTO PELO {CONVENIO}')
            print('=-=' * 20)
        if CONVENIO == '2':
            CONVENIO = 'IAPEP'
            NOME = str(input('INSIRA O 1º NOME DO PACIENTE: ')).upper()
            DATA = str(input('Insira o dia: '))
            HORAS = str(input('''[1]MANHÃ
ou
[2]TARDE?
Opção: '''))
            if HORAS == '1':
                HORAS = '07:30'
            if HORAS == '2':
                HORAS = '14:00'
            MEDICO = str(input('''QUAL O MÉDICO?
[1]Dr.Samuel
[2]Dra.Lorena
[3]Dra.Rossana
[4]Dr.Fernando
[5]Dr.Daniel
Opção: '''))
            if MEDICO == '1':
                MEDICO = 'Samuel'
            if MEDICO == '2':
                MEDICO = 'Lorena'
            if MEDICO == '3':
                MEDICO = 'Rossana'
            if MEDICO == '4':
                MEDICO = 'Fernando'
            if MEDICO == '5':
                MEDICO = 'Daniel'
            print(f'''Sr(a) {NOME}, a Clínica Oftalmed informa:
Sua consulta está marcada para dia {DATA}/11/2022, às {HORAS}, com Dr(a). {MEDICO}.
*obs.*: Atendimento por ordem de chegada.
Endereço: Rua Coelho de Resende, Nº248, Centro-Sul,
Ponto de referência: Ao lado da panificadora *MODELO*.''')
            print('=-=' * 20)
            print(f'ATENDIMENTO PELO {CONVENIO}')
            print('=-=' * 20)
        if CONVENIO == '3':
            CONVENIO = 'INTERMED'
            NOME = str(input('INSIRA O 1º NOME DO PACIENTE: ')).upper()
            DATA = str(input('Insira o dia: '))
            HORAS = str(input('''[1]MANHÃ
ou
[2]TARDE?
Opção: '''))
            if HORAS == '1':
                HORAS = '07:30'
            if HORAS == '2':
                HORAS = '14:00'
            MEDICO = str(input('''QUAL O MÉDICO?
[1]Dr.Samuel
[2]Dra.Lorena
[3]Dra.Rossana
[4]Dr.Fernando
[5]Dr.Daniel
Opção: '''))
            if MEDICO == '1':
                MEDICO = 'Samuel'
            if MEDICO == '2':
                MEDICO = 'Lorena'
            if MEDICO == '3':
                MEDICO = 'Rossana'
            if MEDICO == '4':
                MEDICO = 'Fernando'
            if MEDICO == '5':
                MEDICO = 'Daniel'
            print(f'''Sr(a) {NOME}, a Clínica Oftalmed informa:
Sua consulta está marcada para dia {DATA}/11/2022, às {HORAS}, com Dr(a). {MEDICO}.
*obs.*: Atendimento por ordem de chegada.
Endereço: Rua Coelho de Resende, Nº248, Centro-Sul,
Ponto de referência: Ao lado da panificadora *MODELO*.''')
            print('=-=' * 20)
            print(f'ATENDIMENTO PELO {CONVENIO}')
            print('=-=' * 20)
        if CONVENIO == '4':
            CONVENIO = 'CAAPI'
            NOME = str(input('INSIRA O 1º NOME DO PACIENTE: ')).upper()
            DATA = str(input('Insira o dia: '))
            HORAS = str(input('''[1]MANHÃ
ou
[2]TARDE?
Opção: '''))
            if HORAS == '1':
                HORAS = '07:30'
            if HORAS == '2':
                HORAS = '14:00'
            MEDICO = str(input('''QUAL O MÉDICO?
[1]Dr.Samuel
[2]Dra.Lorena
[3]Dra.Rossana
[4]Dr.Fernando
[5]Dr.Daniel
Opção: '''))
            if MEDICO == '1':
                MEDICO = 'Samuel'
            if MEDICO == '2':
                MEDICO = 'Lorena'
            if MEDICO == '3':
                MEDICO = 'Rossana'
            if MEDICO == '4':
                MEDICO = 'Fernando'
            if MEDICO == '5':
                MEDICO = 'Daniel'
            print(f'''Sr(a) {NOME}, a Clínica Oftalmed informa:
Sua consulta está marcada para dia {DATA}/11/2022, às {HORAS}, com Dr(a). {MEDICO}.
*obs.*: Atendimento por ordem de chegada.
Endereço: Rua Coelho de Resende, Nº248, Centro-Sul,
Ponto de referência: Ao lado da panificadora *MODELO*.''')
            print('=-=' * 20)
            print(f'ATENDIMENTO PELO {CONVENIO}')
            print('=-=' * 20)
        if CONVENIO == '5':
            CONVENIO = 'SUL-AMERICA'
            NOME = str(input('INSIRA O 1º NOME DO PACIENTE: ')).upper()
            DATA = str(input('Insira o dia: '))
            HORAS = str(input('''[1]MANHÃ
ou
[2]TARDE?
Opção: '''))
            if HORAS == '1':
                HORAS = '07:30'
            if HORAS == '2':
                HORAS = '14:00'
            MEDICO = str(input('''QUAL O MÉDICO?
[1]Dr.Samuel
[2]Dra.Lorena
[3]Dra.Rossana
[4]Dr.Fernando
[5]Dr.Daniel
Opção: '''))
            if MEDICO == '1':
                MEDICO = 'Samuel'
            if MEDICO == '2':
                MEDICO = 'Lorena'
            if MEDICO == '3':
                MEDICO = 'Rossana'
            if MEDICO == '4':
                MEDICO = 'Fernando'
            if MEDICO == '5':
                MEDICO = 'Daniel'
            print(f'''Sr(a) {NOME}, a Clínica Oftalmed informa:
Sua consulta está marcada para dia {DATA}/11/2022, às {HORAS}, com Dr(a). {MEDICO}.
*obs.*: Atendimento por ordem de chegada.
Endereço: Rua Coelho de Resende, Nº248, Centro-Sul,
Ponto de referência: Ao lado da panificadora *MODELO*.''')
            print('=-=' * 20)
            print(f'ATENDIMENTO PELO {CONVENIO}')
            print('=-=' * 20)
        if CONVENIO == '6':
            CONVENIO = 'UNIMED'
            NOME = str(input('INSIRA O 1º NOME DO PACIENTE: ')).upper()
            DATA = str(input('Insira o dia: '))
            HORAS = str(input('''[1]MANHÃ
ou
[2]TARDE?
Opção: '''))
            if HORAS == '1':
                HORAS = '07:30'
            if HORAS == '2':
                HORAS = '14:00'
            MEDICO = str(input('''QUAL O MÉDICO?
[1]Dr.Samuel
[2]Dra.Lorena
[3]Dra.Rossana
[4]Dr.Fernando
[5]Dr.Daniel
Opção: '''))
            if MEDICO == '1':
                MEDICO = 'Samuel'
            if MEDICO == '2':
                MEDICO = 'Lorena'
            if MEDICO == '3':
                MEDICO = 'Rossana'
            if MEDICO == '4':
                MEDICO = 'Fernando'
            if MEDICO == '5':
                MEDICO = 'Daniel'
            print(f'''Sr(a) {NOME}, a Clínica Oftalmed informa:
Sua consulta está marcada para dia {DATA}/11/2022, às {HORAS}, com Dr(a). {MEDICO}.
*obs.*: Atendimento por ordem de chegada.
Endereço: Rua Coelho de Resende, Nº248, Centro-Sul,
Ponto de referência: Ao lado da panificadora *MODELO*.''')
            print('=-=' * 20)
            print(f'ATENDIMENTO PELO {CONVENIO}')
            print('=-=' * 20)