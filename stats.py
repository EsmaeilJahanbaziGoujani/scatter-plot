import numpy as np  # Import numpy for numerical operations
import matplotlib.pyplot as plt  # Import matplotlib for plotting

# Sample data for the bar chart: labels and statistics for Salary and WorkHours
labels = ['Mean', 'Median', 'Std']  # Labels for the x-axis (statistical measures)
salary_stats = [65000, 60000, 12000]  # Salary statistics: mean, median, standard deviation
workhour_stats = [41, 40, 2.64]  # WorkHours statistics: mean, median, standard deviation

x = np.arange(len(labels))  # Create an array [0, 1, 2] for bar positions
# np.arange: Generates a sequence of numbers for positioning the bars

bar_width = 0.35  # The width of each bar in the bar chart
# bar_width: Controls how wide each bar is in the grouped bar chart

fig, ax1 = plt.subplots(figsize=(8, 6))  # Create a figure and a set of subplots with a specific size
# plt.subplots: Initializes the plotting area and axes

# Salary bars (left y-axis)
bars1 = ax1.bar(x - bar_width/2, salary_stats, width=bar_width, label='Salary', color='orange')
# ax1.bar: Draws bars for Salary statistics, shifted left for grouping
# label: Sets the legend label for this series
# color: Sets the color of the bars

ax1.set_ylabel('Salary')  # Set the label for the left y-axis
ax1.set_xticks(x)  # Set the x-tick positions to match the bar positions
ax1.set_xticklabels(labels)  # Set the x-tick labels to the statistic names
ax1.set_title('Stats: Salary & WorkHours')  # Set the title of the plot
ax1.tick_params(axis='y', labelcolor='orange')  # Set the y-axis tick label color to match Salary bars

# WorkHours bars (right y-axis)
ax2 = ax1.twinx()  # Create a second y-axis sharing the same x-axis
# twinx: Allows plotting data with a different y-scale on the same plot

bars2 = ax2.bar(x + bar_width/2, workhour_stats, width=bar_width, label='WorkHours', color='royalblue')
# ax2.bar: Draws bars for WorkHours statistics, shifted right for grouping
# label: Sets the legend label for this series
# color: Sets the color of the bars


ax2.set_ylabel('WorkHours')  # Set the label for the right y-axis
ax2.tick_params(axis='y', labelcolor='royalblue')  # Set the y-axis tick label color to match WorkHours bars

# Annotate values on top of each Salary bar for clarity
for bar in bars1:
    height = bar.get_height()  # Get the height of the bar (the value it represents)
    ax1.annotate(f'{height:.2f}', xy=(bar.get_x() + bar.get_width()/2, height),
                 xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', color='orange')
    # annotate: Adds the value as text above each bar for easier reading

# Annotate values on top of each WorkHours bar for clarity
for bar in bars2:
    height = bar.get_height()  # Get the height of the bar (the value it represents)
    ax2.annotate(f'{height:.2f}', xy=(bar.get_x() + bar.get_width()/2, height),
                 xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', color='royalblue')
    # annotate: Adds the value as text above each bar for easier reading

# Combine legends from both axes so both Salary and WorkHours are shown in the legend
bars = bars1 + bars2  # Combine both bar containers for the legend
labels_combined = [bar.get_label() for bar in bars]  # Get the label for each bar series
fig.legend([bars1, bars2], ['Salary', 'WorkHours'], loc='upper right')  # Add a combined legend to the figure

plt.tight_layout()  # Adjust the layout to prevent overlap between elements
# tight_layout: Automatically adjusts subplot params for a clean look

plt.show()  # Display the plot window
# show: Renders the plot visually
