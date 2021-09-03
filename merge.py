import pandas as pd
df = pd.concat(
    map(pd.read_csv, [ r'C:\Users\Dhruv Bajaj\PycharmProjects\pythonProject6\Top_Doctors.csv',r'C:\Users\Dhruv Bajaj\PycharmProjects\pythonProject6\TopDoctors.csv']), ignore_index=True)
print(df)
df.to_csv('TopD.csv', mode='a', header=False)