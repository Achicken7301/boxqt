import pandas as pd
import csv

df = pd.read_excel("clean_data\\raw_data.xlsx", sheet_name="output")
resolution_of_ADC = 4095
system_voltage = 3.3
R_0 = 220
# ADC_reading = 595

# print(df.head())

# print("Voltage measure: " + str(V_meas))
# print("Mass: " + str(mass))

f = df["fa"].values
print(len(f))
f_g = []
for f in f:
    if f != 0:
        V_meas = system_voltage * f / resolution_of_ADC
        mass = 271000 / (R_0 * ((system_voltage / V_meas) - 1))
        mass = pow(mass, 1 / 0.69)
        f_g.append(str(mass))
    else:
        f_g.append(0)

print(f_g[0])

# dict = {"f(gram)": f_g}

# df1 = pd.DataFrame(dict)

# # saving the dataframe
# df1.to_csv("clean_data\\filename.csv", index=False)
