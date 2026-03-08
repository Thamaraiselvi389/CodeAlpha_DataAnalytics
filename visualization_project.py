import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

df = pd.read_csv("sales_data.csv")

print(df)

plt.figure()
ax = sns.barplot(x="Month", y="Sales", data=df)

for i in ax.containers:
    ax.bar_label(i)
plt.title("Monthly Sales")
plt.savefig("sales_bar_chart.png")
plt.show()

plt.figure()
plt.plot(df["Month"], df["Profit"], marker='o')
plt.title("Profit Trend")
plt.savefig("profit_line_chart.png")
plt.show()

plt.figure()
sns.scatterplot(x="Sales", y="Profit", data=df)
plt.title("Sales vs Profit Relationship")
plt.savefig("sales_profit_scatter.png")
plt.show()
plt.figure()

sns.histplot(df["Sales"], bins=5)

plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.savefig("sales_distribution.png")
plt.show()
plt.figure()

correlation = df[["Sales", "Profit"]].corr()

sns.heatmap(correlation, annot=True, cmap="coolwarm")

plt.title("Correlation Between Sales and Profit")
plt.savefig("correlation_heatmap.png")
plt.show()