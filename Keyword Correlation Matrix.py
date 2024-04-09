import csv
import pandas as pd

def read_keywords(keywd_file):
    with open(keywd_file, 'r') as file:
        reader = csv.reader(file)
        keywd = next(reader)  # Assuming the keywords are in the first row
    return keywd

def calculate_correlation(csvfile, keywds):
    # Read the CSV file
    df = pd.read_csv(csvfile)

    # Calculate correlation coefficient between each pair of keywords
    correlations = pd.DataFrame(index=keywds, columns=keywds)

    for keyword1 in keywds:
        for keyword2 in keywds:
            if keyword1 != keyword2:
                correlation = df['text'].str.contains(keyword1).corr(df['text'].str.contains(keyword2))
                correlations.at[keyword1, keyword2] = correlation

    return correlations

# Example usage
csv_file = 'restaurantreviews_Iowa_cleaned.csv'
keyword_file = 'CommonWordsandPhrases.csv'
output_file = 'keyword_correlation_matrix.csv'

# Read keywords from the keyword file
keywords = read_keywords(keyword_file)

# Calculate correlations
correlation_matrix = calculate_correlation(csv_file, keywords)

# Save correlation matrix to CSV file
correlation_matrix.to_csv(output_file)

print("Correlation matrix saved to 'keyword_correlation_matrix.csv'")
