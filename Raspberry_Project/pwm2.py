import pwm_functions as pf

pf.config_IO()
r, l = pf.config_PWM()

# # Modifica o Duty Cycle
# a = int(raw_input('PWM Duty Cycle: '))
print('Inicio do movimento')

pf.mov_inicial(r, l, DC = 60, verbose = True)
pf.mov_mid(r, l, DC = 70,  tempo=5, verbose = True)
pf.mov_final(r, l, DC = 70, tempo=5, verbose = True)

print('Fim do programa.')