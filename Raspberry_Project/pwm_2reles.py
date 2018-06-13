import bib_rasp
import RPi.GPIO as gpio
import time


bib_rasp.config_IO()
bib_rasp.config_dir_rele()
pwm = bib_rasp.config_PWM()

print('Inicio do movimento')

dc = input('Duty Cicle: ')
pwm.ChangeDutyCycle(70) # Duty cicle de partida
time.sleep(.1)
# pwm.ChangeDutyCycle(35) # Duty cicle para o movimento
# time.sleep(.1)
pwm.ChangeDutyCycle(0) # Duty cicle para o movimento

print('Fim do programa.')
gpio.cleanup()
