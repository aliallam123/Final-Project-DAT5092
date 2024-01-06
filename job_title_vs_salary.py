import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('ai_salaries.csv')

job_salary_mean = df.groupby('job_title')['salary'].mean().sort_values(ascending=False)

top_10_job_salary_mean = job_salary_mean.head(10)

plt.figure(figsize=(12,6))
top_10_job_salary_mean.plot(kind='bar', color='blue')
plt.xlabel('Job Title')
plt.ylabel('Average Salary (USD)')
plt.title('Top 10 Job Titles in AI with Highest Average Salary')
plt.xticks(rotation=45, ha='right')
plt.show()