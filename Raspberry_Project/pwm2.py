import pwm_functions as pf

pf.config_IO()
pf.config_PWM()

# # Modifica o Duty Cycle
a = int(raw_input('PWM Duty Cycle: '))
print('Inicio do movimento')

pf.mov_inicial(a)
pf.mov_mid(a)
pf.mov_final(a)

print('Fim do programa.')