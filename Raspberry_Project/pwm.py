import RPi.GPIO as IO
import motor_dc as dc
import time

dc.config_IO()
direct = int(raw_input('On/Off: '))
dc.direction(direct)
p = dc.config_PWM()

while 1:
    DC = int(raw_input('Duty Cycle: '))
    if DC != 0:
        p.ChangeDutyCycle(DC) # Duty cicle de partida
        time.sleep(.5)
        # pwm.ChangeDutyCycle(35) # Duty cicle para o movimento
        # time.sleep(.1)
        p.ChangeDutyCycle(0) # Duty cicle para o movimento
    else:
        break

print('Fim do programa.')
IO.cleanup()