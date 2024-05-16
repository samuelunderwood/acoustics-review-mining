import pandas as pd

# Step 1: Read CSV files
main_df = pd.read_csv('restaurantreviews_Iowa_cleaned.csv')
filter_df = pd.read_csv('CommonWordsandPhrases.csv')

# Step 2: Filter data based on keywords and count occurrences
keyword_occurrences = {}
for index, row in main_df.iterrows():
    for keyword in filter_df.iloc[:, 0]:
        if keyword in str(row['text']):  # Check if keyword is in the 'text' column
            if keyword in keyword_occurrences:
                keyword_occurrences[keyword] += 1
            else:
                keyword_occurrences[keyword] = 1

# Convert the dictionary of keyword occurrences into a DataFrame
keyword_occurrences_df = pd.DataFrame(list(keyword_occurrences.items()), columns=['Keyword', 'Occurrences'])

# Sort the DataFrame by occurrences in descending order
keyword_occurrences_df = keyword_occurrences_df.sort_values(by='Occurrences', ascending=False)

# Save the DataFrame to a CSV file
keyword_occurrences_df.to_csv('keyword_occurrences.csv', index=False)
