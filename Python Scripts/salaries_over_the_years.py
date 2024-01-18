import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ai_salaries.csv')

df['work_year'] = pd.to_datetime(df['work_year'], format='%Y')

plt.figure(figsize=(10,6))
plt.plot(df.groupby(df['work_year'].dt.year)['salary'].median(), marker='o', linestyle='-', color='blue')
plt.title('Median AI/ML Job Salaries Over the Years')
plt.xlabel('Year')
plt.ylabel('Median Salary ($)')
plt.xticks(df['work_year'].dt.year.unique())
plt.grid(True)
plt.show()