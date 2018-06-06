import RPi.GPIO as IO
import time

# Desabilitar os avisos
IO.setwarnings(False)

# Programando os GPIO pin por Board (Numero real do pino)
IO.setmode(IO.BOARD)

# Inicializa o pino 35 como pino de saida
IO.setup(35, IO.OUT)
IO.setup(36, IO.OUT)
IO.setup(37, IO.IN, pull_up_down = IO.PUD_DOWN)
IO.setup(38, IO.IN, pull_up_down = IO.PUD_DOWN)
IO.setup(40, IO.IN, pull_up_down = IO.PUD_DOWN)

# GPIO 35, PWM de saida com frequência de 100Hz
l = IO.PWM(35, 4096)
r = IO.PWM(36, 4096)

# Gera o sinal do PWM com 0% de Duty Cycle
l.start(0)
r.start(0)

# # Modifica o Duty Cycle
a = int(raw_input('PWM Duty Cycle: '))
print('Inicio do movimento')

while 1:
    l.ChangeDutyCycle(a)

    if IO.input(37) == IO.LOW:
        print('Fim do movimento.')
        l.ChangeDutyCycle(0)
        break

print('Fim do programa.')