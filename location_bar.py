import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ai_salaries.csv')

location_salary_mean = df.groupby('company_location')['salary_in_usd'].mean().sort_values(ascending=False)

top_20_countries = location_salary_mean.head(20)

plt.figure(figsize=(12,6))
top_20_countries.plot(kind='bar', color='darkblue')
plt.xlabel('Job Title')
plt.ylabel('Average Salary (USD)')
plt.title('Global Distribution of Average Company Salaries in AI and ML Jobs')
plt.xticks(rotation=45, ha='right', fontsize=15)
plt.show()