import os
from datetime import datetime

path = "ABS_log.txt"

while True:
    print('-='*20)
    print('Anotação abastecimento Fox')
    print('-='*20)
    print('')

    print('FOX SELECIONADO')
    print('1 - Anotar info de abastecimento')
    print('2 - Ler info')
    print('3 - Sair')
    opcao = int(input('Digite a opção: '))
    print('')

    switch = {
        1: 'anotar',
        2: 'ler',
        3: 'sair'
    }

    if switch[opcao] == 'anotar':
        
        # data = str / KMTotal = float / KMrodado = float /litros=float/ valorPLitro= float/ localização = str
        
        print("Formato: ddmmYYYY_aaaaa.aa_xxx.xx_yy.yy_z.zz_'br-araucarias' (data_KMTotal_KMrodado_litros_valorPLitro_localização)")

        nova_info = input('Digite a info de abastecimento: ')
        
        with open(path, 'a') as arquivo:
            arquivo.write(nova_info+'\n')
        print('Info adicionada com sucesso!')
        print('')

    if switch[opcao] == 'ler':
        with open(path, 'r') as arquivo:
            for linha in arquivo:
                print(linha)
        datetime.time.sleep(5)
        print('')
    if switch[opcao] == 'sair':
        break


