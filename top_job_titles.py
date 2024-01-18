import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('ai_salaries.csv')

top_job_titles = df['job_title'].value_counts().nlargest(10)

plt.figure(figsize=(12, 6))
top_job_titles.plot(kind='bar', color='blue')
plt.title('Top 10 Job Titles in AI Jobs')
plt.xlabel('Job Title')
plt.ylabel('Frequency')

plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.show()