# using pandas because its the simplest way to read a csv and explore the data
# it gives quick respons, functions, check the shape missing values, basic stats

import pandas as pd
import sys

file_path = 'assets\\customers-100000.csv'
df = pd.read_csv(file_path)

print("== Dataset Shape ==")
print(df.shape, end="\n\n")

print("== Dataset Head ==")
print(df.head(5), end="\n\n")

print("== Dataset Info ==")
df.info()
print("\n")

print("Total rows: ", len(df))
print("Top countries: ", df['Country'].value_counts().head(10).to_dict(), end="\n\n")
print("Top cities: ", df['City'].value_counts().head(10).to_dict(), end="\n\n")