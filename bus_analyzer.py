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
    

