import bib_rasp
import RPi.GPIO as gpio
import time
#from datetime import datetime

bib_rasp.config_IO()
bib_rasp.config_dir_rele()
pwm = bib_rasp.config_PWM()

try:
    print('Inicio do movimento')

    # Teste

    pwm.ChangeDutyCycle(70) # Duty cicle de partida
    time.sleep(.5)
    pwm.ChangeDutyCycle(35) # Duty cicle para o movimento

    #datetime.now().time()
    #bib_rasp.mov_inicial(pwm, DC_partida = 70, DC_movimento = 35, verbose = True)
    #bib_rasp.mov_mid(pwm, DC_partida = 70, DC_movimento = 35,  tempo=5, verbose = True)
    #bib_rasp.mov_final(pwm, DC_partida = 70, DC_movimento = 35, tempo=5, verbose = True)

    print('Fim do programa.')
except KeyboardInterrupt:
    pwm.ChangeDutyCycle(0) # Para o motor
