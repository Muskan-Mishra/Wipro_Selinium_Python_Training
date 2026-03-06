import seaborn as sns
import matplotlib.pyplot as plt

# basic plot (line plot)
# Load the sample data set
data = sns.load_dataset("flights")

# Line plot
sns.lineplot(x="year", y="passengers", data=data)
plt.title("Yearly passenger growth")
plt.show()

# Bar plot
data = sns.load_dataset("tips")
sns.barplot(x="day", y="total_bill", data=data)

plt.title("Average bill per day")
plt.show()

# Scatter Plot
data = sns.load_dataset("tips")
sns.scatterplot(x="total_bill", y="tip", data=data)

plt.title("Total Bill vs Tip")
plt.show()

# Histogram
data = sns.load_dataset("tips")
sns.histplot(data["total_bill"], bins=20)

plt.title("Total Bill vs Tip")
plt.show()


# Box Plot
data = sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill", data=data)

plt.title("Bill Distribution by Day")
plt.show()


# Heat Map
data = sns.load_dataset("tips")
corr = data.corr(numeric_only=True)

sns.heatmap(corr, annot=True, cmap="coolwarm")

plt.title("Correlation Heatmap")
plt.show()

#pair plot
data = sns.load_dataset("iris")
sns.pairplot(data)
plt.show()

#violin plot
data = sns.load_dataset("tips")
sns.violinplot(x="day",y="total_bill",data=data)
plt.title("Bill Distribution by Day")
plt.show()

# Count Plot
data = sns.load_dataset("tips")
sns.countplot(x="day", data=data)
plt.title("Number of Customers per Day")
plt.show()


# Regression Plot
data = sns.load_dataset("tips")
sns.regplot(x="total_bill", y="tip", data=data)
plt.title("Regression between Bill and Tip")
plt.show()