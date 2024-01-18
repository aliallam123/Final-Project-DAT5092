import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ai_salaries.csv')

company_size_salary = df.groupby('company_size')['salary_in_usd'].mean().reset_index()

df['company_size'] = pd.Categorical(df['company_size'], categories=['L', 'M', 'S'], ordered=True)

plt.figure(figsize=(8,6))
plt.bar(company_size_salary['company_size'], company_size_salary['salary_in_usd'], color = 'blue')
plt.xlabel('Company Size')
plt.ylabel('Average Salary (USD)')
plt.title('Average Salary in USD by Company Size')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()