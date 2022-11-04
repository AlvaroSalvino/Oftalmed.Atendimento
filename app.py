#Variaveis
cad = {
}
pacientes=[]
#============================================================

print('=-=-=-=-=-=-=-=-=-= OFTALMED ATENDIMENTO =-=-=-=-=-=-=-=-=-=')
while True:
    print('=-=' * 20)
    opcao = str(input('''[1]NOME
[2]CONVENIOS
[3]AGENDA MEDICA
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
            cad['nome']=NOME
            cad['convenio']=CONVENIO
            cad['data']=DATA
            cad['horas']=HORAS
            cad['medico']=MEDICO
            pacientes.append(cad.copy())
            with open('Pacientes.xlsx', 'w') as arquivo:
                for pac in pacientes:
                    arquivo.write(str(pac) + '\n')
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
            cad['nome']=NOME
            cad['convenio']=CONVENIO
            cad['data']=DATA
            cad['horas']=HORAS
            cad['medico']=MEDICO
            pacientes.append(cad.copy())
            with open('Pacientes.xlsx', 'w') as arquivo:
                for pac in pacientes:
                    arquivo.write(str(pac) + '\n')
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
            cad['nome']=NOME
            cad['convenio']=CONVENIO
            cad['data']=DATA
            cad['horas']=HORAS
            cad['medico']=MEDICO
            pacientes.append(cad.copy())
            with open('Pacientes.xlsx', 'w') as arquivo:
                for pac in pacientes:
                    arquivo.write(str(pac) + '\n')
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
            cad['nome']=NOME
            cad['convenio']=CONVENIO
            cad['data']=DATA
            cad['horas']=HORAS
            cad['medico']=MEDICO
            pacientes.append(cad.copy())
            with open('Pacientes.xlsx', 'w') as arquivo:
                for pac in pacientes:
                    arquivo.write(str(pac) + '\n')
        if CONVENIO == '5':
            CONVENIO = 'SUL-AMERICA'
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
            cad['nome'] = NOME
            cad['convenio'] = CONVENIO
            cad['data'] = DATA
            cad['horas'] = HORAS
            cad['medico'] = MEDICO
            pacientes.append(cad.copy())
            with open('Pacientes.xlsx', 'w') as arquivo:
                for pac in pacientes:
                    arquivo.write(str(pac) + '\n')
        if CONVENIO == '6':
            CONVENIO = 'UNIMED'
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
            cad['nome'] = NOME
            cad['convenio'] = CONVENIO
            cad['data'] = DATA
            cad['horas'] = HORAS
            cad['medico'] = MEDICO
            pacientes.append(cad.copy())
            with open('Pacientes.xlsx', 'w') as arquivo:
                for pac in pacientes:
                    arquivo.write(str(pac) + '\n')
    if opcao == '2':
        CONVENIO = str(input('''[1]SUS
[2]IAPEP
[3]INTERMED
[4]CAAPI
[5]SUL-AMERICA
[6]UNIMED
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
            cad['nome']=NOME
            cad['convenio']=CONVENIO
            cad['data']=DATA
            cad['horas']=HORAS
            cad['medico']=MEDICO
            pacientes.append(cad.copy())
            with open('Pacientes.xlsx', 'w') as arquivo:
                for pac in pacientes:
                    arquivo.write(str(pac) + '\n')
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
            cad['nome']=NOME
            cad['convenio']=CONVENIO
            cad['data']=DATA
            cad['horas']=HORAS
            cad['medico']=MEDICO
            pacientes.append(cad.copy())
            with open('Pacientes.xlsx', 'w') as arquivo:
                for pac in pacientes:
                    arquivo.write(str(pac) + '\n')
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
            cad['nome']=NOME
            cad['convenio']=CONVENIO
            cad['data']=DATA
            cad['horas']=HORAS
            cad['medico']=MEDICO
            pacientes.append(cad.copy())
            with open('Pacientes.xlsx', 'w') as arquivo:
                for pac in pacientes:
                    arquivo.write(str(pac) + '\n')
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
            cad['nome']=NOME
            cad['convenio']=CONVENIO
            cad['data']=DATA
            cad['horas']=HORAS
            cad['medico']=MEDICO
            pacientes.append(cad.copy())
            with open('Pacientes.xlsx', 'w') as arquivo:
                for pac in pacientes:
                    arquivo.write(str(pac) + '\n')
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
            cad['nome']=NOME
            cad['convenio']=CONVENIO
            cad['data']=DATA
            cad['horas']=HORAS
            cad['medico']=MEDICO
            pacientes.append(cad.copy())
            with open('Pacientes.xlsx', 'w') as arquivo:
                for pac in pacientes:
                    arquivo.write(str(pac) + '\n')
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
            cad['nome']=NOME
            cad['convenio']=CONVENIO
            cad['data']=DATA
            cad['horas']=HORAS
            cad['medico']=MEDICO
            pacientes.append(cad.copy())
            with open('Pacientes.xlsx', 'w') as arquivo:
                for pac in pacientes:
                    arquivo.write(str(pac) + '\n')
    if opcao == '3':
        opcaoUnidade = str(input('''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=
[1]COELHO DE RESENDE
[2]SÃO PEDRO
[3]JOCKEY
Opção: '''))
        if opcaoUnidade == '1':
            print('''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=
SEGUNDA     -        TERÇA     -      QUARTA       -       QUINTA     -     SEXTA
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=
                                  MANHÃ:            
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=
DR. SAMUEL    -    DR. SAMUEL   -   DR. SAMUEL     -    DR. SAMUEL     -   DR. SAMUEL
    &                   &                &                    &                 &
DRa. LORENA   -    DR. SAMUEL   -   DRa. LORENA    -    DR. SAMUEL     -   DR. SAMUEL
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=
                                  TARDE:            
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=
DR. SAMUEL    -    DR. SAMUEL   -   DR. SAMUEL     -    DR. SAMUEL
     &                  &                &                  &
DR. SAMUEL    -    DRa. ROSSANA -   DR. FERNANDO   -    DR. SAMUEL
''')
        if opcaoUnidade == '2':
            print('''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=
SEGUNDA     -        TERÇA     -      QUARTA       -       QUINTA     -     SEXTA
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=
                                  MANHÃ:            
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=
DR. SAMUEL    -    DRa. ROSSANA -   DR. SAMUEL     -    DR. SAMUEL     -   DR. SAMUEL
    &                   &                &                    &                 &
DR. SAMUEL    -    DRa. ROSSANA -   DR. FERNANDO   -    DRa. NATALIA   -   DR. SAMUEL
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=
                                  TARDE:            
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=
DR. DANIEL    -    DRa. KASSANDRA -  DR. SAMUEL     -    DR. HELTON
     &                  &                &                  &
DR. DANIEL    -    DRa. KASSANDRA -  DR. DANIEL     -    DR. HELTON
''')
        if opcaoUnidade == '3':
            print('''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-JOCKEY=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=
SEGUNDA     -        TERÇA     -      QUARTA       -       QUINTA     -     SEXTA
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=
                                  TARDE:            
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=
DRa. KASSANDRA                          -                                DRa. LORENA
     &                 
DR. SAMUEL = 16:30 -DR. SAMUEL          -                 DR. SAMUEL
OBS: DRa. KASSANDRA, ATENDE APENAS DE 15 EM 15 DIAS. -  DRa. LORENA, ATENDE SOMENTE PARTICULAR SOBRE AVISO.
''')