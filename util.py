def anotar_info(path, temp_path):
    """
    Handles the input of refueling information, allowing the user to choose between a simple or detailed entry.
    Stores new entries temporarily before moving them to the main log file.
    """
    print("1 - Anotação fácil")
    print("2 - Anotação completa")
    option = int(input('Digite a opção: '))
    print('')
    
    if option == 1:
        # Simple entry mode
        data = input('Digite a data (ddmmYYYY): ')
        km_total = input('Digite o KM total: ')
        km_rodado = input('Digite o KM rodado: ')
        litros = input('Digite a quantidade de litros: ')
        valor_p_litro = input('Digite o valor por litro: ')
        localizacao = input('Digite a localização: ')
        print('')
        
        new_entry = f"{data}_{km_total}_{km_rodado}_{litros}_{valor_p_litro}_{localizacao}\n"
    elif option == 2:
        # Detailed entry mode
        print("Formato: ddmmYYYY_aaaaa.aa_xxx.xx_yy.yy_z.zz_'br-araucarias'")
        new_entry = input('Digite a info de abastecimento: ') + '\n'

    # Write to temporary path
    with open(temp_path, 'a') as file:
        file.write(new_entry)
    print('Informação adicionada com sucesso ao arquivo temporário!\n')

def ler_info(path):
    """
    Reads the refueling information from the log file and prints each entry.
    """
    try:
        with open(path, 'r') as file:
            print("Informações de abastecimento:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Arquivo de log não encontrado.")

def processar_arquivo_temporario(temp_path, path):
    """
    Processes the temporary file: checks for new entries not in the main log,
    adds them if they are not duplicates, and clears the temporary file afterward.
    """
    try:
        with open(temp_path, 'r') as temp_file:
            new_entries = temp_file.readlines()
    except FileNotFoundError:
        print("Não há arquivo temporário para processar.")
        return

    unique_entries = []
    try:
        with open(path, 'r+') as file:
            existing_entries = file.readlines()
            existing_set = set(existing_entries)
            
            for entry in new_entries:
                if entry not in existing_set:
                    unique_entries.append(entry)
                    file.write(entry)
                    
        if unique_entries:
            print(f"{len(unique_entries)} novas entradas adicionadas ao arquivo de log.")
        else:
            print("Nenhuma nova entrada encontrada para adicionar.")
    finally:
        # Clear the temporary file
        with open(temp_path, 'w') as temp_file:
            pass

def ordenar_log(path):
    """
    Sorts the log file entries chronologically by date.
    """
    try:
        with open(path, 'r+') as file:
            entries = file.readlines()
            # Assuming entries are of the format 'ddmmYYYY_...', sort by the date field
            entries.sort(key=lambda x: x.split('_')[0])
            file.seek(0)
            file.writelines(entries)
            print("Log ordenado com sucesso.")
    except FileNotFoundError:
        print("Arquivo de log para ordenar não encontrado.")
