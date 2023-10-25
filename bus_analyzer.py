#import serial

serial_data = 0

vel = serial_data[0]
rpm = serial_data[1]

if rpm > 700:
    #carro ligado
    print('Carro ligado')
    print('Velocidade: ', vel)
    print('RPM: ', rpm)
    print('')

    # make a switch for every rotation, and then analyze the speed if is ok

