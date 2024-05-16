import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("restaurant_reviews_with_keywords_sentiment.csv")

# Check if 'Sentiment' column exists
if 'Sentiment' in df.columns:
    # Remove specified columns
    columns_to_remove = ['user_id', 'time', 'pics', 'resp']
    df = df.drop(columns=columns_to_remove, errors='ignore')

    # Filter rows with non-null 'Sentiment' values
    filtered_df = df.dropna(subset=['Sentiment'])

    # Include additional columns in the output DataFrame
    columns_to_include = ['rating', 'text', 'gmap_id', 'Sentiment']
    output_df = filtered_df[columns_to_include]

    # Output the DataFrame to a new CSV file
    output_df.to_csv("sentiment_and_reviews.csv", index=False)
    print("Sentiment values along with rating, text, and gmap_id saved to sentiment_and_reviews.csv.")
else:
    print("No 'Sentiment' column found in the DataFrame.")
