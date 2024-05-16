import pandas as pd
import matplotlib.pyplot as plt

# Read the merged CSV file into a DataFrame
merged_df = pd.read_csv("merged_data.csv")

# Get unique rating values
unique_ratings = merged_df['rating_y'].unique()

# Create subplots for each boxplot
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15, 10))

# Plot boxplots for each rating and save as separate PNG files
for i, ax in enumerate(axes.flatten()):
    rating = unique_ratings[i]
    filtered_df = merged_df[merged_df['rating_y'] == rating]
    ax.boxplot(filtered_df['Sentiment_y'], vert=False)
    ax.set_title(f'Rating {rating}')
    ax.set_xlabel('Sentiment')
    ax.set_ylabel('Rating')
    ax.grid(True)

    # Save the boxplot as a separate PNG file
    plt.savefig(f'boxplot_rating_{rating}.png')

# Adjust layout
plt.tight_layout()

# Show the boxplots
plt.show()

