import time
from RPi import GPIO
from time import sleep

clkLastState = 0

def config_IO(clk = 17, dt = 18):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def clkLastState_init(clk = 17):
    return GPIO.input(clk)

def mesure(aux_clkLastState, aux_counter, clk = 17, dt = 18):
    counter = aux_counter
    clkLastState = aux_clkLastState

    while True:
        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)
        if clkState != clkLastState:
            if dtState != clkState:
                counter += 1
            else:
                counter -= 1
        clkLastState = clkState
        return counter, clkLastState

if __name__ == "__main__":
    print('Iniciando')
    counter = 0

    config_IO()
    clkLastState = clkLastState_init()
    print(clkLastState)
    print(counter)

    while (counter != 5):
        print(counter)
        counter, clkLastState = mesure(clkLastState, counter)
        print(counter)