import os
from util import *

# Ensure directory exists
os.makedirs('./cars/fox', exist_ok=True)

def main():
    path = "./cars/fox/abastecimento_log.txt"
    temp_path = "./cars/fox/temp_abastecimento_log.txt"

    while True:
        print('-=' * 20)
        print('Anotação de Abastecimento - FOX')
        print('-=' * 20)
        print('1 - Anotar info de abastecimento')
        print('2 - Ler info')
        print('3 - Processar arquivo temporário')
        print('4 - Ordenar log por data')
        print('5 - Sair')
        option = int(input('Digite a opção: '))
        print('')

        if option == 1:
            anotar_info(path, temp_path)
        elif option == 2:
            ler_info(path)
        elif option == 3:
            processar_arquivo_temporario(temp_path, path)
        elif option == 4:
            ordenar_log(path)
        elif option == 5:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
