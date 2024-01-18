import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ai_salaries.csv')

sns.set(style="whitegrid")

plt.figure(figsize=(12,8))
sns.boxplot(x='experience_level', y='salary_in_usd', data=df, palette='RdYlGn')

plt.xlabel('Experience Level')
plt.ylabel('Salary (USD)')
plt.title('Salary vs. Experience Levels in AI/ML Jobs')

plt.xticks(rotation=45, ha='right')
plt.show()