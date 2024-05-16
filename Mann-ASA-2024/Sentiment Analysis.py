import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load CommonWordsandPhrases.csv into a DataFrame
common_words_df = pd.read_csv("CommonWordsandPhrases.csv")

# Load restaurantreviews_Iowa_cleaned.csv into a DataFrame
restaurant_reviews_df = pd.read_csv("restaurantreviews_Iowa_cleaned.csv")

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to analyze sentiment for each word in the review text
def analyze_sentiment(review_text):
    sentiment_scores = []
    for word in review_text.split():  # Iterate over words in the review text
        sentiment = analyzer.polarity_scores(word)
        sentiment_scores.append(sentiment['compound'])
    return sum(sentiment_scores) / len(sentiment_scores)

# Apply sentiment analysis to each review in the restaurant reviews DataFrame
restaurant_reviews_df['Sentiment'] = restaurant_reviews_df['text'].apply(analyze_sentiment)

# Output the DataFrame with sentiment scores to a CSV file
restaurant_reviews_df.to_csv("restaurant_reviews_with_sentiment.csv", index=False)
