import os
import time

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
        
        print(" 1 - Anotação fácil ")
        print(" 2 - Anotação completa ")
        opcao = int(input('Digite a opção: '))
        print('')
        if opcao == 1:
            data = input('Digite a data: ')
            KMTotal = input('Digite o KM total: ')
            KMrodado = input('Digite o KM rodado: ')
            litros = input('Digite a quantidade de litros: ')
            valorPLitro = input('Digite o valor por litro: ')
            localizacao = input('Digite a localização: ')
            print('')
            nova_info = data+'_'+KMTotal+'_'+KMrodado+'_'+litros+'_'+valorPLitro+'_'+localizacao
            with open(path, 'a') as arquivo:
                arquivo.write(nova_info+'\n')
            print('Info adicionada com sucesso!')
            print('')

        if opcao == 2:
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
        time.sleep(5)
        print('')
    if switch[opcao] == 'sair':
        break


