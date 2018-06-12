import RPi.GPIO as gpio
import time

# PWM -> 35
# RELE 1 -> 31
# RELE 2 -> 32
# FIM DE CURSO 1 -> 37
# SENSOR DO MEIO -> 38
# FIM DE CURSO 2 -> 40

def config_gpio(pwm_pin = 35, rele_1 = 31, rele_2 = 32, fimcurso1 = 37, midtower = 38, fimcurso2 = 40, verbose = False):

    # Configuring GPIO
    gpio.setmode(gpio.BOARD)

    # Inicializa o pino 35 como pino de saida
    if verbose == True: print('Iniciando a configuracao de pinagem:')
    gpio.setup(pwm_pin, gpio.OUT)
    gpio.setup(rele_1, gpio.OUT)
    gpio.setup(rele_2, gpio.OUT)
    gpio.setup(fimcurso1, gpio.IN, pull_up_down = gpio.PUD_DOWN)
    gpio.setup(midtower, gpio.IN, pull_up_down = gpio.PUD_DOWN)
    gpio.setup(fimcurso2, gpio.IN, pull_up_down = gpio.PUD_DOWN)
    if verbose == True:
        print('\tPWM: Pin {}' .format(pwm))
        print('\tFim de Curso: Pin {}' .format(fimcurso1))
        print('\tMid Tower: Pin {}' .format(midtower))
        print('\tFim de Curso 2: Pin {}' .format(fimcurso2))
        print('Configuracao concluida\n')

def config_dir_rele(dir = 0, rele_1=31, rele_2=32):
    if(dir == 0):
        gpio.output(rele_1, gpio.HIGH)
        gpio.output(rele_2, gpio.HIGH)
    else:
        gpio.output(rele_1, gpio.LOW)
        gpio.output(rele_2, gpio.LOW)

def config_PWM(freq = 100, pwm_pin = 35, verbose = False):
    # GPIO 35, PWM de saida com frequencia de 100Hz
    if verbose == True: print('Configurando o GPIO {} como PWM.' .format(pwm))
    pwm = gpio.PWM(pwm_pin, freq)

    # Gera o sinal do PWM com 0% de Duty Cycle
    if verbose == True: print('Iniciando o PWM com Duty Cycle igual a 0 - Motor parado.\n')
    pwm.start(0)

    return pwm 

def mov_inicial(pwm, DC_partida=70, DC_movimento=35, fimcurso1 = 37, midtower = 38, fimcurso2 = 40, verbose = False):
    if verbose == True: print('Iniciando cronometro.')
    time.sleep(1) para teste
    if verbose == True: print('Iniciando o movimento.')

    pwm.ChangeDutyCycle(DC_partida) # Duty cicle de partida
    time.sleep(.5)
    pwm.ChangeDutyCycle(DC_movimento) # Duty cicle para o movimento

    while 1:
        if gpio.input(fimcurso1) == gpio.HIGH:
            if verbose == True: print('Fim do movimento.\n')
            pwm.ChangeDutyCycle(0)
            break

def mov_mid(pwm, DC_partida=70, DC_movimento=35, tempo = 5, fimcurso1 = 37, midtower = 38, fimcurso2 = 40, verbose = False):
    if verbose == True: print('Iniciando cronometro.')
    time.sleep(tempo) #para teste
    if verbose == True: print('Iniciando o movimento.')

    pwm.ChangeDutyCycle(DC_partida) # Duty cicle de partida
    time.sleep(.5)
    pwm.ChangeDutyCycle(DC_movimento) # Duty cicle para o movimento

    while 1:
        if gpio.input(midtower) == gpio.HIGH:
            if verbose == True: print('Fim do movimento.\n')
            pwm.ChangeDutyCycle(0)
            break

def mov_final(pwm, DC_partida=70, DC_movimento=35, tempo = 5, fimcurso1 = 37, midtower = 38, fimcurso2 = 40, verbose = False):
    if verbose == True: print('Iniciando cronometro.')
    time.sleep(tempo) # para teste
    if verbose == True: print('Iniciando o movimento.')

    pwm.ChangeDutyCycle(DC_partida) # Duty cicle de partida
    time.sleep(.5)
    pwm.ChangeDutyCycle(DC_movimento) # Duty cicle para o movimento

    while 1:
        if gpio.input(fimcurso2) == gpio.HIGH:
            if verbose == True: print('Fim do movimento.\n')
            pwm.ChangeDutyCycle(0)
            break