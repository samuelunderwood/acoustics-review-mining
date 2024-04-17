import pandas as pd
import matplotlib.pyplot as plt

# Read the merged CSV file into a DataFrame
merged_df = pd.read_csv("merged_data.csv")

# Get unique rating values
unique_ratings = merged_df['rating_y'].unique()

# Create subplots for each histogram
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15, 10))

# Plot histograms for each rating and save as separate PNG files
for i, ax in enumerate(axes.flatten()):
    rating = unique_ratings[i]
    filtered_df = merged_df[merged_df['rating_y'] == rating]
    ax.hist(filtered_df['Sentiment_y'], bins=20, color='skyblue', edgecolor='black')
    ax.set_title(f'Rating {rating}')
    ax.set_xlabel('Sentiment')
    ax.set_ylabel('Frequency')

    # Save the histogram as a separate PNG file
    plt.savefig(f'histogram_rating_{rating}.png')

# Adjust layout
plt.tight_layout()

# Show the histograms
plt.show()
