import RPi.GPIO as IO
import time

# Desabilitar os avisos
IO.setwarnings(False)

# Programando os GPIO pin por Board (Numero real do pino)
IO.setmode(IO.BOARD)

# Inicializa o pino 35 como pino de saida
IO.setup(35, IO.OUT)
IO.setup(36, IO.OUT)

# GPIO 35, PWM de saida com frequencia de 100Hz
l = IO.PWM(35, 100)
r = IO.PWM(36, 100)

# Gera o sinal do PWM com 0% de Duty Cycle
l.start(0)
r.start(0)

# # Modifica o Duty Cycle
# p.ChangeDutyCycle(x)
while 1:
    a = int(raw_input('PWM Duty Cycle: '))
    if a>0:
        r.ChangeDutyCycle(0)
        l.ChangeDutyCycle(a)
    if a<0:
        l.ChangeDutyCycle(0)
        r.ChangeDutyCycle(-a)
    if a==0:
        r.ChangeDutyCycle(0)
        l.ChangeDutyCycle(0)
        break
