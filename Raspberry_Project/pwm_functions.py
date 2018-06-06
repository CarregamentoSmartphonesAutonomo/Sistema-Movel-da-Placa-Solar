import RPi.GPIO as IO
import time

def config_IO(pwm1 = 35, pwm2 = 36, fimcurso1 = 37, midtower = 38, fimcurso2 = 40, verbose = False):
    # Desabilitar os avisos
    IO.setwarnings(False)

    # Programando os GPIO pin por Board (Numero real do pino)
    IO.setmode(IO.BOARD)

    # Inicializa o pino 35 como pino de saida
    if verbose == True: print('Iniciando a configuração de pinagem:')
    IO.setup(pwm1, IO.OUT)
    IO.setup(pwm2, IO.OUT)
    IO.setup(fimcurso1, IO.IN, pull_up_down = IO.PUD_DOWN)
    IO.setup(midtower, IO.IN, pull_up_down = IO.PUD_DOWN)
    IO.setup(fimcurso2, IO.IN, pull_up_down = IO.PUD_DOWN)
    if verbose == True:
        print('\tPWM right: Pin {}' .format(pwm1))
        print('\tPWM left: Pin {}' .format(pwm2))
        print('\tFim de Curso: Pin {}' .format(fimcurso1))
        print('\tMid Tower: Pin {}' .format(midtower))
        print('\tFim de Curso 2: Pin {}' .format(fimcurso2))
        print('Configuração concluida\n')

def config_PWM(freq = 100, IO1 = 35, IO2 = 37, verbose=False):
    # GPIO 35, PWM de saida com frequência de 100Hz
    if verbose == True: print('Configurando o IO {} como PWM left e o IO {} como PWM rigth.' .format(IO1, IO2))
    l = IO.PWM(IO1, freq)
    r = IO.PWM(IO2, freq)

    # Gera o sinal do PWM com 0% de Duty Cycle
    if verbose == True: print('Iniciando os PWMs com Duty Cycle igual a 0 - Motor parado.\n')
    l.start(0)
    r.start(0)

def mov_inicial(DC=1, fimcurso1 = 37, midtower = 38, fimcurso2 = 40, verbose=False):
    if verbose == True: print('Iniciando cronometro.')
    time.sleep(1)
    if verbose == True: print('Iniciando o movimento.')
    while 1:
        l.ChangeDutyCycle(DC)

        if IO.input(fimcurso1) == IO.HIGH:
            if verbose == True: print('Fim do movimento.\n')
            l.ChangeDutyCycle(0)
            break

def mov_mid(DC=1, fimcurso1 = 37, midtower = 38, fimcurso2 = 40, tempo = 15, verbose=False):
    if verbose == True: print('Iniciando cronometro.')
    time.sleep(tempo)
    if verbose == True: print('Iniciando o movimento.')
    
    while 1:
        r.ChangeDutyCycle(DC)

        if IO.input(midtower) == IO.HIGH:
            if verbose == True: print('Fim do movimento.\n')
            r.ChangeDutyCycle(0)
            break

def mov_final(DC=1, fimcurso1 = 37, midtower = 38, fimcurso2 = 40, tempo = 15, verbose=False):
    if verbose == True: print('Iniciando cronometro.')
    time.sleep(tempo)
    if verbose == True: print('Iniciando o movimento.')    
    while 1:
        r.ChangeDutyCycle(DC)

        if IO.input(fimcurso2) == IO.HIGH:
            if verbose == True: print('Fim do movimento.\n')
            r.ChangeDutyCycle(0)
            break