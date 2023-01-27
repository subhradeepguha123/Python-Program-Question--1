import pandas as pd
import numpy as np

#Question-1
df = pd.read_excel(r"C:\Users\Sguha\Downloads\Product GST.xlsx")
print(df)

#Question-2
print(df.info())
print(df.drop_duplicates().value_counts())
print(df.value_counts().isnull())

#Question-3
print(df.mean())
