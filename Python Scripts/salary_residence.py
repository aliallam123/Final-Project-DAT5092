import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ai_salaries.csv')

heatmap_data = df.pivot_table(values='salary_in_usd', index='employee_residence', aggfunc='mean')

plt.figure(figsize=(12,6))

sns.heatmap(heatmap_data, annot=True, fmt='.2f', cbar_kws={'label': 'Average Salary in USD'})

plt.title('Heatmap: Salary vs Employee Residence')
plt.xlabel('Salary in USD')
plt.ylabel('Employee Residence')

plt.tight_layout()
plt.show()