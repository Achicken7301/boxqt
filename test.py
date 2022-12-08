import pandas as pd


resolution_of_ADC = 4095
system_voltage = 3.3
R_0 = 220
ADC_reading = 595

V_meas = system_voltage * ADC_reading / resolution_of_ADC

mass = 271000 / (R_0 * ((system_voltage / V_meas) - 1))
mass = pow(mass, 1 / 0.69)
print("Voltage measure: " + str(V_meas))
print("Mass: " + str(mass))