import RPi.GPIO as IO
import time

# Desabilitar os avisos
IO.setwarnings(False)

# Programando os GPIO pin por Board (Numero real do pino)
IO.setmode(IO.BOARD)

# Inicializa o pino 35 como pino de saida
IO.setup(35, IO.OUT)

# GPIO 35, PWM de saida com frequência de 100Hz
p = IO.PWM(35,100)

# Gera o sinal do PWM com 0% de Duty Cycle
p.start(0)

# # Modifica o Duty Cycle
# p.ChangeDutyCycle(x)
while 1:
    a = int(raw_input('PWM Duty Cycle: '))
    p.ChangeDutyCycle(a)
