import RPi.GPIO as gpio
import motor_dc as dc
import time
import threading
from multiprocessing.pool import ThreadPool

dc.config_IO()
direct = int(raw_input('On/Off: '))
dc.direction(direct)
p = dc.config_PWM()

# Thread do sensor
def sensor():
    global counter
    counter = 0
    clk = 24
    dt = 26
    vcc = 23
    gpio.setmode(gpio.BOARD)
    gpio.setup(vcc, gpio.OUT)
    gpio.output(vcc, gpio.HIGH) # ativa VCC
    gpio.setup(clk, gpio.IN, pull_up_down=gpio.PUD_DOWN)
    gpio.setup(dt, gpio.IN, pull_up_down=gpio.PUD_DOWN)
    clkLastState=gpio.input(clk)
    while True:
        clkState=gpio.input(clk)
        dtState=gpio.input(dt)
        if clkState != clkLastState:
            if dtState != clkState:
                counter+=1
            else:
                counter-=1
        clkLastState = clkState
        time.sleep(.01)

t = threading.Thread(target=sensor)
t.start()

for i in range(0,25):
    p.ChangeDutyCycle(40) # Duty cicle de partida
    time.sleep(.5)
    p.ChangeDutyCycle(60) # Duty cicle de partida
    time.sleep(.2)        
    p.ChangeDutyCycle(0) # Duty cicle para o movimento
    time.sleep(2)
while 1:
    DC = int(raw_input('Duty Cycle: '))
    if DC != 0:
        p.ChangeDutyCycle(DC) # Duty cicle de partida
        time.sleep(.25)
        # pwm.ChangeDutyCycle(35) # Duty cicle para o movimento
        # time.sleep(.1)
        p.ChangeDutyCycle(0) # Duty cicle para o movimento
        time.sleep(9.75)
    else:
        break

print('Fim do programa.')
gpio.cleanup()