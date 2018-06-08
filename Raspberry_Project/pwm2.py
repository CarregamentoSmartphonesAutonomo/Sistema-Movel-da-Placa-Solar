import pwm_functions as pf

pf.config_IO()
r, l = pf.config_PWM()

# # Modifica o Duty Cycle
a = int(raw_input('PWM Duty Cycle: '))
print('Inicio do movimento')

pf.mov_inicial(r, l, DC = a, verbose = True)
pf.mov_mid(r, l, DC = a, verbose = True)
pf.mov_final(r, l, DC = a, verbose = True)

print('Fim do programa.')