import pandas as pd
import time

print('Load file with OPENPYXL')
start_time = time.time()
df = pd.read_excel('bug.xlsx', engine='openpyxl')
print(len(df))
end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))


print('Load file with XLRD')
start_time = time.time()
df = pd.read_excel('bug.xlsx')
print(len(df))
end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))

