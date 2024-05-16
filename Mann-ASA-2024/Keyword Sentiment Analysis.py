import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load CommonWordsandPhrases.csv into a DataFrame
common_words_df = pd.read_csv("CommonWordsandPhrases.csv")

# Extract common words as a set for faster lookup
common_words_set = set(common_words_df.iloc[:, 0].str.lower())  # Read from the first column

# Load restaurantreviews_Iowa_cleaned.csv into a DataFrame
restaurant_reviews_df = pd.read_csv("restaurantreviews_Iowa_cleaned.csv")

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to analyze sentiment for each common word in the review text
def analyze_sentiment(review_text):
    sentiment_scores = []
    for word in review_text.split():  # Iterate over words in the review text
        if word.lower() in common_words_set:  # Check if word is in common words set
            sentiment = analyzer.polarity_scores(word)
            sentiment_scores.append(sentiment['compound'])
    if sentiment_scores:  # Check if sentiment scores list is not empty
        return sum(sentiment_scores) / len(sentiment_scores)
    else:
        return None  # Return None if no common words found in review

# Apply sentiment analysis to each review in the restaurant reviews DataFrame
restaurant_reviews_df['Sentiment'] = restaurant_reviews_df['text'].apply(analyze_sentiment)

# Output the DataFrame with sentiment scores to a CSV file
restaurant_reviews_df.to_csv("restaurant_reviews_with_keywords_sentiment.csv", index=False)
