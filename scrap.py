import os
import pandas as pd

path = os.getcwd()
files = os.listdir(path)

files_xlsx = [f for f in files if f[-4:] == 'xlsx']

df = pd.DataFrame()
for f in files_xlsx:
    data = pd.read_excel(f)
    df = df.append(data)
print df 