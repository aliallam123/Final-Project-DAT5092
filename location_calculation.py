import pandas as pd
df = pd.read_csv('ai_salaries.csv')
unique_countries = df['company_location'].nunique()
print("Number of unique countries:", unique_countries)