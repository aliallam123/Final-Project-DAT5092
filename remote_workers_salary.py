import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ai_salaries.csv')

heatmap_data = df.pivot_table(values='salary_in_usd', index='remote_ratio', aggfunc='mean')

plt.figure(figsize=(12,6))

sns.heatmap(heatmap_data, annot=True, fmt='.2f', cbar_kws={'label': 'Average Salary in USD'})

plt.title('Heatmap: Average Salary vs Ratio of Remote Workers')
plt.xlabel('Average Salary in USD')
plt.ylabel('Ratio of Remote Workers')

"""
key_text = (
    "Key:\n"
    "remote_ratio - The overall amount of work done remotely:\n"
    "0 - No remote work (less than 20%)\n"
    "50 - Partially remote\n"
    "100 - Fully remote (more than 80%)"
)

plt.gcf().text(1.05, 0.5, key_text, fontsize=9, va='center')
"""
##rect=[0, 0, 0.9, 1]

sns.heatmap.set_yticklabels(sns.heatmap.get_yticklabels(), rotation=0)

plt.tight_layout()
plt.show()