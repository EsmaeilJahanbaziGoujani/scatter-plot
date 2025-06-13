import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

mean_values = df.mean()
median_values = df.median()
std_values = df.std()

print('mean:\n', mean_values)
print('median:\n', median_values)
print('std:\n', std_values)


scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(df)
normalized_df = pd.DataFrame(normalized_data, columns=df.columns)
print(normalized_df)



plt.scatter(df['Salary'], df['WorkHours'])
plt.xlabel('Salary')
plt.ylabel('WorkHours')
plt.title('Scatter plot between Salary and WorkHours')
plt.grid(True)
plt.show()


