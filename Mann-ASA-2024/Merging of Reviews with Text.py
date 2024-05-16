import pandas as pd

# Read the first CSV file into a DataFrame
file1_df = pd.read_csv("sentiment_and_reviews.csv")

# Read the second CSV file into a DataFrame
file2_df = pd.read_csv("restaurant_reviews_with_sentiment.csv")

# Remove duplicates from the 'text' column in each DataFrame
file1_df = file1_df.drop_duplicates(subset='text')
file2_df = file2_df.drop_duplicates(subset='text')

# Merge the DataFrames based on the 'text' column
merged_df = pd.merge(file1_df, file2_df, on='text', how='inner')

# Remove specified columns
columns_to_remove = ['user_id', 'time', 'pics', 'resp']
merged_df = merged_df.drop(columns=columns_to_remove, errors='ignore')

# Create a new column for the difference between 'Sentiment_x' and 'Sentiment_y'
merged_df['Sentiment_difference'] = merged_df['Sentiment_x'] - merged_df['Sentiment_y']

# Output the merged DataFrame to a new CSV file
merged_df.to_csv("merged_data.csv", index=False)
