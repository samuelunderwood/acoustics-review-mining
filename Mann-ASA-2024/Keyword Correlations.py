import csv
from collections import Counter
import pandas as pd

def read_keywords(keyword_file):
    keywords = []
    with open(keyword_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            keywords.extend(row)
    return keywords

def calculate_correlation(csv_file, keywords):
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Initialize a dictionary to store counts for each keyword
    keyword_counts = {keyword: Counter() for keyword in keywords}

    # Count occurrences of each keyword in the CSV data
    for keyword in keywords:
        for index, row in df.iterrows():
            text = row['text']  # Assuming 'text' is the column containing the text data
            if keyword in text:
                keyword_counts[keyword][index] += 1

    # Calculate correlation coefficient between each pair of keywords
    correlations = {}
    for keyword1 in keywords:
        for keyword2 in keywords:
            if keyword1 != keyword2:
                correlation = df['text'].str.contains(keyword1).corr(df['text'].str.contains(keyword2))
                correlations[(keyword1, keyword2)] = correlation

    return correlations

def save_correlations_to_csv(correlations, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Keyword 1', 'Keyword 2', 'Correlation'])
        for (keyword1, keyword2), correlation in correlations.items():
            writer.writerow([keyword1, keyword2, correlation])

# Example usage
csv_file = 'restaurantreviews_Iowa_cleaned.csv'
keyword_file = 'CommonWordsandPhrases.csv'
output_file = 'keyword_correlations.csv'

# Read keywords from the keyword file
keywords = read_keywords(keyword_file)

# Calculate correlations
correlations = calculate_correlation(csv_file, keywords)

# Save correlations to CSV file
save_correlations_to_csv(correlations, output_file)

print("Keyword correlations saved to 'keyword_correlations.csv'")
