# --- This code doesn't work very well and stats chart is not good ---


import pandas as pd  # Import pandas for data manipulation and analysis
import numpy as np  # Import numpy for numerical operations
from sklearn.preprocessing import MinMaxScaler  # Import MinMaxScaler for normalization
import matplotlib.pyplot as plt  # Import matplotlib for plotting

# Read the CSV file 'data.csv' into a DataFrame called df
df = pd.read_csv('data.csv')
# pandas DataFrame: Table-like data structure for storing and analyzing data

# Calculate the mean (average) of each column in the DataFrame
mean_values = df.mean()
# mean: The average value of each column

# Calculate the median (middle value) of each column in the DataFrame
median_values = df.median()
# median: The middle value of each column

# Calculate the standard deviation (spread) of each column in the DataFrame
std_values = df.std()
# std (Standard Deviation): A measure of how spread out the values are

# Print the mean values for all columns
print('Mean:\n', mean_values)
# Print the median values for all columns
print('Median:\n', median_values)
# Print the standard deviation values for all columns
print('Std:\n', std_values)

# Create a MinMaxScaler object for normalizing data between 0 and 1
scaler = MinMaxScaler()
# MinMaxScaler: Scaler for bringing all values into the [0,1] range

# Fit the scaler to the DataFrame and transform the data
normalized_data = scaler.fit_transform(df)
# fit: Calculate the minimum and maximum values for scaling
# transform: Apply the calculated min and max to normalize the data

# Convert the normalized numpy array back to a DataFrame with the same columns
normalized_df = pd.DataFrame(normalized_data, columns=df.columns)
# pandas DataFrame: Table-like structure for holding the normalized values

# Print the normalized DataFrame
print(normalized_df)

# Prepare statistics for the bar chart:
salary_stats = [mean_values['Salary'], median_values['Salary'], std_values['Salary']]
# salary_stats: List of statistical values (mean, median, std) for Salary

workhour_stats = [mean_values['WorkHours'], median_values['WorkHours'], std_values['WorkHours']]
# workhour_stats: List of statistical values (mean, median, std) for WorkHours

labels = ['Mean', 'Median', 'Std']
# labels: X-axis labels for the bar chart

# Create a figure with 1 row and 2 columns of subplots (side by side)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 5))
# subplot: Divides the plotting area into multiple sections for separate plots

fig.suptitle('Scatter & Statistical Visualization')
# suptitle: Main title for the entire figure

# --- First subplot: Scatter plot ---
ax1.scatter(df['Salary'], df['WorkHours'], color='teal')
# scatter: A plot showing the relationship between two numeric variables

ax1.set_xlabel('Salary')
ax1.set_ylabel('WorkHours')
ax1.set_title('Scatter: Salary vs WorkHours')
ax1.grid(True)

# --- Second subplot: Bar chart for statistics ---
bar_width = 0.15  # Width of each bar in the bar chart
# bar_width: The width of each bar in the bar chart

x = np.arange(len(labels))  # The label locations (0, 1, 2 for Mean, Median, Std)
# np.arange: Generates an array of sequential numbers for bar positions

ax2.bar(x - bar_width/2, salary_stats, width=bar_width, label='Salary', color='orange')
# bar: Draws bars for Salary statistics, shifted left

ax2.bar(x + bar_width/2, workhour_stats, width=bar_width, label='WorkHours', color='royalblue')
# bar: Draws bars for WorkHours statistics, shifted right

ax2.set_xticks(x)
ax2.set_xticklabels(labels)
ax2.set_title('Stats: Salary & WorkHours')
ax2.legend()
ax2.set_ylabel('Value')

plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust layout for the main title
# tight_layout: Adjusts subplot spacing to prevent overlap
print('WorkHours', workhour_stats)
plt.show()
# show: Displays the plots
