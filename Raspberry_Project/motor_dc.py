import RPi.GPIO as gpio

def config_IO(pwm = 35, rele_1 = 37, rele_2 = 38, vcc = 36):
    # Desabilitar os avisos
    gpio.setwarnings(False)

    # Programando os GPIO pin por Board (Numero real do pino)
    gpio.setmode(gpio.BOARD)

    # Inicializa o pino 35 como pino de saida
    gpio.setup(rele_1, gpio.OUT)
    gpio.setup(rele_2, gpio.OUT)
    gpio.setup(pwm, gpio.OUT)
    gpio.setup(vcc, gpio.OUT)
    gpio.output(vcc,gpio.HIGH)
    print('Configurando os pinos')

def direction(direct = 0, rele_1 = 37, rele_2 = 38):
    if(direct == 0):
        gpio.output(rele_1, gpio.HIGH)
        gpio.output(rele_2, gpio.HIGH)
    else:
        gpio.output(rele_1, gpio.LOW)
        gpio.output(rele_2, gpio.LOW)

def config_PWM(freq = 100, pwm = 35, verbose=False):
    # GPIO 35, PWM de saida com frequencia de 100Hz
    if verbose == True: print('Configurando o gpio {} como PWM left e o gpio {} como PWM rigth.' .format(IO1, IO2))
    p = gpio.PWM(pwm, freq)

    # Gera o sinal do PWM com 0% de Duty Cycle
    if verbose == True: print('Iniciando os PWMs com Duty Cycle igual a 0 - Motor parado.\n')
    p.start(0)

    return p