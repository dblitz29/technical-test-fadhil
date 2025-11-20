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

print("== Missing Values ==")
print(df.isna().sum().sort_values(ascending=False).head(10), end="\n\n")

print("== Description ==")
print(df.describe(), end="\n")