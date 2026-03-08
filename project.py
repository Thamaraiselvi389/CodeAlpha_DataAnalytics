import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Sales": [1000, 1200, 900, 1400]
}

df = pd.DataFrame(data)

sns.barplot(x="Month", y="Sales", data=df)

plt.title("Monthly Sales")
plt.show()
plt.figure()

plt.plot(df["Month"], df["Sales"], marker='o')

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()
plt.figure()

plt.plot(df["Month"], df["Sales"], marker='o')

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()
plt.figure()

plt.pie(df["Sales"], labels=df["Month"], autopct='%1.1f%%')

plt.title("Sales Distribution")

plt.show()