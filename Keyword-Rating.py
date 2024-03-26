import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Read CSV files
main_df = pd.read_csv('restaurantreviews_Iowa_cleaned.csv')
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

# Step 4: Create a combined histogram for top 20 most frequently used keywords
top_keywords = keyword_rating_df['Keyword'].value_counts().nlargest(20).index.tolist()
combined_df = keyword_rating_df[keyword_rating_df['Keyword'].isin(top_keywords)]

# Assign colors to each individual keyword based on ranking
colors = plt.cm.rainbow(np.linspace(0, 1, len(top_keywords)))

plt.figure(figsize=(12, 8))
for i, keyword in enumerate(top_keywords):
    keyword_data = combined_df[combined_df['Keyword'] == keyword]
    keyword_data['Rating'].value_counts().sort_index().plot(kind='bar', color=colors[i], alpha=0.6, label=keyword)

plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.title('Combined Histogram for Top 20 Keywords')
plt.legend(loc='upper right')
plt.savefig('combined_histogram_top_20_keywords.png')
plt.close()
