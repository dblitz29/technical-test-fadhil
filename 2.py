# this code reads the large csv in chunks so it doesnt take  much memory.
# with chunks, I can still calculate totals and summary without storing everything. O(n)

import pandas as pd

file_path = 'assets\\customers-2000000.csv'
chunk_size = 100000
total_rows = 0
country_count = {}
city_count = {}

for chunk in pd.read_csv(file_path, chunksize=chunk_size):
    total_rows += len(chunk)
    for country in chunk['Country']:
        if country in country_count:
            country_count[country] += 1
        else:
            country_count[country] = 1

    for city in chunk['City']:
        if city in city_count:
            city_count[city] += 1
        else:
            city_count[city] = 1

top_countries = sorted(country_count.items(), key=lambda x: x[1], reverse=True)[:10]
top_cities = sorted(city_count.items(), key=lambda x: x[1], reverse=True)[:10]
print("Total rows:", total_rows, end="\n")
print("Top 10 Countries:", top_countries, end="\n")
print("Top 10 Cities:", top_cities, end="\n")