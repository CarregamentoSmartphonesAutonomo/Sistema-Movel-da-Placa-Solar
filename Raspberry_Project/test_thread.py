import RPi.GPIO as gpio
import time
import threading
from multiprocessing.pool import ThreadPool

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

while True:
    print "Program: ", counter