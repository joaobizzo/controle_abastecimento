import os
from datetime import datetime



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
        
        # data/litros/valorPorLitro
        
        print("Formato: ddmmYYYY/xxx.xx/yy.yy/z.zz (data/KMrodado/litros/valorPLitro)")

        nova_info = input('Digite a info de abastecimento: ')
        
        with open('info.txt', 'a') as arquivo:
            arquivo.write(nova_info+'\n')
        print('Info adicionada com sucesso!')
        print('')

    if switch[opcao] == 'ler':
        with open('info.txt', 'r') as arquivo:
            for linha in arquivo:
                print(linha)
        print('')
    if switch[opcao] == 'sair':
        break


