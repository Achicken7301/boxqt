import csv
import datetime
l = [
  (1, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4), 
  (5, 6, 7, 8, 6, 7, 8, 6, 7, 8, 6, 7, 8, 6, 7, 8),
  (5, 6, 7, 8, 6, 7, 8, 6, 7, 8, 6, 7, 8, 6, 7, 8),
  (5, 6, 7, 8, 6, 7, 8, 6, 7, 8, 6, 7, 8, 6, 7, 8)
  ]

data = zip(*l)

# header = ['a_x', 'a_y', 'a_z', 'g_x', 'g_y', 'g_z']

# filename: dd-mm-YYYY hh:mm:ss
name_format = datetime.datetime.now().strftime("%x %X").replace("/", "-")
name_format = name_format.replace(':', "-")
filename = name_format + ".csv"
with open(filename, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    
    # write multiple rows
    writer.writerows(data)