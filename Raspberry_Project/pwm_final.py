import RPi.GPIO as gpio
import motor_dc as dc
import time
import threading
from multiprocessing.pool import ThreadPool
from datetime import datetime

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

# Main
dc.config_IO()
dc.direction(0) # 0 ou 1 para trocar direcao
p = dc.config_PWM()
pos = 0
while True:

    h = datetime.time(datetime.now()).hour - 3 # hora considerando fuso horario
    pos = h-8 # posicao de acordo com horario
    if pos < 0:
        pos = 0

    if pos < 8:
        while counter != pos:
            p.ChangeDutyCycle(40) # Duty cicle de pre-partida
            time.sleep(.5)
            p.ChangeDutyCycle(60) # Duty cicle de partida
            time.sleep(.2)        
            p.ChangeDutyCycle(0) # Para movimento
            time.sleep(2)
        time.sleep(60)
    else:
        pos = 0
        dc.direction(1) 
        while counter != pos:
            p.ChangeDutyCycle(15) # Duty cicle de pre-partida
            time.sleep(.5)
            p.ChangeDutyCycle(30) # Duty cicle de partida
            time.sleep(.2)        
            p.ChangeDutyCycle(0) # Para movimento
            time.sleep(2)
        dc.direction(0)
        while h < 8 or h > 16: # loop enquato estiver em um horário que a placa não se mexe
            h = datetime.time(datetime.now()).hour - 3


gpio.cleanup()