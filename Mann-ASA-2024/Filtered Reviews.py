import pandas as pd

# Open the first CSV file (restaurant reviews)
data = pd.read_csv('restaurantreviews_Iowa_cleaned.csv')

# Open the second CSV file containing common words and phrases to filter
filter_csv_path = 'CommonWordsandPhrases.csv'

# Read filtering keywords from the second CSV file (Column A)
filter_keywords_df = pd.read_csv(filter_csv_path, header=None)
filter_keywords = filter_keywords_df.iloc[:, 0].tolist()

# Function to apply filtering keywords to text
def apply_filter_criteria(text):
    for keyword in filter_keywords:
        if keyword.lower() in text.lower():  # Case-insensitive matching
            return True  # Return True if any keyword matches
    return False  # Return False if no keyword matches

# Filter the data based on keywords
filtered_data = data[data.iloc[:, 3].apply(apply_filter_criteria)]  # Assuming text is in the fourth column

# Write filtered data to output CSV file
output_csv_path = 'filtered_restaurant_reviews.csv'
filtered_data.to_csv(output_csv_path, index=False)

print(f"Filtered data written to {output_csv_path}")
