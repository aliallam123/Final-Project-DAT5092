import pandas as pd
import matplotlib.pyplot as plt
import squarify

df = pd.read_csv('ai_salaries.csv')

avg_salaries = df.groupby('company_location')['salary_in_usd'].mean().sort_values(ascending=False)

top_72 = avg_salaries.head(72)

plt.figure(figsize=(16, 14))
squarify.plot(sizes=top_72, label=top_72.index, alpha=0.8)
plt.title("Global Distribution of Average Company Salaries in AI and ML Jobs")
plt.axis('off')
plt.show()