import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read CSV files
main_df = pd.read_csv('restaurantreviews_Iowa_cleaned.csv')
filter_df = pd.read_csv('CommonWordsandPhrases.csv')

# Step 2: Filter data based on keywords
filtered_rows = []
for index, row in main_df.iterrows():
    if any(keyword in row.iloc[3] for keyword in filter_df.iloc[:, 0]):
        filtered_rows.append(row)

filtered_df = pd.DataFrame(filtered_rows)

# Step 3: Extract data for scatter plot
dependent_variable = filtered_df.iloc[:, 2]  # Assuming the first column is the keyword column
independent_variable = filtered_df.iloc[:, 3]  # Assuming the second column is the rating column

# Step 4: Create scatter plot
plt.scatter(independent_variable, dependent_variable)
plt.xlabel('Rating')
plt.ylabel('Keywords')
plt.title('Scatter Plot of Rating vs Keywords')
plt.show()
