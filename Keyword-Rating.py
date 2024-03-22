import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read CSV files
main_df = pd.read_csv('filtered_restaurant_reviews.csv')
filter_df = pd.read_csv('CommonWordsandPhrases.csv')

# Step 2: Filter data based on keywords and pair with ratings
keyword_rating_pairs = []
for index, row in main_df.iterrows():
    for keyword in filter_df.iloc[:, 0]:
        if keyword in str(row['text']):  # Check if keyword is in the 'text' column
            keyword_rating_pairs.append({'Keyword': keyword, 'Rating': row['rating']})

# Convert the list of keyword-rating pairs into a DataFrame
keyword_rating_df = pd.DataFrame(keyword_rating_pairs)

# Step 3: Create histograms for each keyword
for keyword, group in keyword_rating_df.groupby('Keyword'):
    plt.figure(figsize=(8, 6))
    group['Rating'].value_counts().sort_index().plot(kind='bar')
    plt.xlabel('Rating')
    plt.ylabel('Frequency')
    plt.title(f'Histogram for Keyword: {keyword}')
    plt.savefig(f'{keyword}_histogram.png')
    plt.close()
