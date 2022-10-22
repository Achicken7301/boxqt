import pandas as pd
import csv

df = pd.read_excel("data\clean_data\\raw_data.xlsx", sheet_name="input")
'''
Header removed
[0:31] -> row_#2 -> row_#32 => 31 rows
'''
# print(df[0:31])
# print(df[31:62])
# print(df[62:93])

final = []
number_of_rows = 31

for i in range(0, len(df), number_of_rows):
    std = df[i:i + number_of_rows].std().values
    final.append(std)

# print(rows)

header = ['std_ax', 'std_ay', 'std_az', 'std_gx', 'std_gy', 'std_gz']

with open('std.csv', 'w') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)
    write.writerow(header)
    write.writerows(final)