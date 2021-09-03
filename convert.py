

import pandas as pd
import numpy as np


# Reading the csv file
df_new = pd.read_csv(r"C:\Users\Dhruv Bajaj\Downloads\New folder (2)\full_english.csv")

# saving xlsx file
GFG = pd.ExcelWriter('Names.xlsx')
df_new.to_excel(GFG, index = False)

GFG.save()