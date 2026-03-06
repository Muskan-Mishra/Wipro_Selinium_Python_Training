import pandas as pd
import numpy as np

# 1. Create a DataFrame containing missing (None/NaN) values
data = {
    'Name': ['Amit', 'Neha', 'Raj', 'Priya', 'John'],
    'Age': [25, None, 30, 28, None],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR'],
    'Salary': [50000, 60000, None, 55000, 65000],
    'City': ['Bangalore', 'Mumbai', 'Bangalore', 'Delhi', 'Bangalore']
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


# 2. Detect missing values
print("\nMissing Values (True indicates missing):")
print(df.isnull())


# 3. Replace missing values with 0
df_filled = df.fillna(0)
print("\nDataFrame after replacing missing values with 0:")
print(df_filled)


# 4. Drop rows containing missing values
df_dropped = df.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(df_dropped)


# 5. Sort the DataFrame by Age in ascending order
df_sort_age = df.sort_values(by='Age', ascending=True)
print("\nSorted by Age (Ascending):")
print(df_sort_age)


# 6. Sort the DataFrame by Salary in descending order
df_sort_salary = df.sort_values(by='Salary', ascending=False)
print("\nSorted by Salary (Descending):")
print(df_sort_salary)


# 7. Groupby Department and find average Salary per department
avg_salary = df.groupby('Department')['Salary'].mean()
print("\nAverage Salary per Department:")
print(avg_salary)


# 8. Find total Salary per department using groupby
total_salary = df.groupby('Department')['Salary'].sum()
print("\nTotal Salary per Department:")
print(total_salary)


# 9. Filter employees where Age > 25 AND City = 'Bangalore'
filtered = df[(df['Age'] > 25) & (df['City'] == 'Bangalore')]
print("\nEmployees where Age > 25 AND City = Bangalore:")
print(filtered)


# 10. Create a new column 'Tax' which is 10% of Salary using apply()
df['Tax'] = df['Salary'].apply(lambda x: x * 0.10 if pd.notnull(x) else x)
print("\nDataFrame with Tax column (10% of Salary):")
print(df)