import pandas as pd
import csv

def read_keywords(keyword_csv):
    with open(keyword_csv, 'r') as file:
        keywords = [row[0] for row in csv.reader(file)]  # Assuming the keywords are in the first row
    return keywords

def filter_reviews_and_create_new_csv(review_csv, keywd_file, output_csv):
    # Read the keywords from the keyword file
    keywords = read_keywords(keywd_file)

    # Read the review CSV file
    df_reviews = pd.read_csv(review_csv)

    # Create a new DataFrame with only the 'gmap_id' column from the reviews CSV file
    df_new = df_reviews[['gmap_id']].copy()

    # Add columns for each keyword
    for keyword in keywords:
        df_new[keyword] = 0

    # Iterate over each row in the original DataFrame and update the keyword columns
    for index, row in df_reviews.iterrows():
        text = row['text']
        for keyword in keywords:
            if keyword in text:
                df_new.at[index, keyword] = 1

    # Save the new DataFrame to a new CSV file
    df_new.to_csv(output_csv, index=False)

    print(f"New CSV file '{output_csv}' created.")

# Example usage
review_file = 'filtered_restaurant_reviews.csv'
keyword_file = 'CommonWordsandPhrases.csv'
output_file = 'new_filtered_reviews.csv'

filter_reviews_and_create_new_csv(review_file, keyword_file, output_file)
