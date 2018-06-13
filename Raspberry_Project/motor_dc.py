import RPi.GPIO as IO

def config_IO(pwm = 35, rele_1 = 37, rele_2 = 38):
    # Desabilitar os avisos
    IO.setwarnings(False)

    # Programando os GPIO pin por Board (Numero real do pino)
    IO.setmode(IO.BOARD)

    # Inicializa o pino 35 como pino de saida
    IO.setup(rele_1, IO.OUT)
    IO.setup(rele_2, IO.OUT)
    IO.setup(pwm, IO.OUT)
    print('Configurando os pinos')


def direction(direct = 0, rele_1 = 37, rele_2 = 38):
    if(direct == 0):
        IO.output(rele_1, IO.HIGH)
        IO.output(rele_2, IO.HIGH)
    else:
        IO.output(rele_1, IO.LOW)
        IO.output(rele_2, IO.LOW)

def config_PWM(freq = 100, pwm = 35, verbose=False):
    # GPIO 35, PWM de saida com frequencia de 100Hz
    if verbose == True: print('Configurando o IO {} como PWM left e o IO {} como PWM rigth.' .format(IO1, IO2))
    p = IO.PWM(pwm, freq)

    # Gera o sinal do PWM com 0% de Duty Cycle
    if verbose == True: print('Iniciando os PWMs com Duty Cycle igual a 0 - Motor parado.\n')
    p.start(0)

    return p