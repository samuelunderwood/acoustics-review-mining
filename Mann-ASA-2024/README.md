Phase1Filtering.py
This code is used to read and clean the raw JSON files from the UCSD Google Local Dataset. The original dataset contains reviews across all businesses, but we are currently only interested in restaurants. This code removes identifiable names of users, and filters the dataset according to the business category from the associated metadata JSON file. This code can run on data for one or multiple U.S. states, just adjust the us_states list as needed

Clustering.ipynb
This notebook is used to perform k-means text clustering analysis on a cleaned CSV file containing user reviews. It can analyze a sub-sample of reviews to reduce computational time.

Cleaning Code.py
This code file further cleans the restaurant reviews by removing all null values in the "reviews" column such as emojis, empty cells, and characters that Python cannot read.

Filtered Reviews.py
This code file opens the cleaned dataset and uses the CommonWordsandPhrases list as a filter. It will return every restaurant review that uses one of the words in the list of CommonWordsandPhrases.

Top 100 Words.py
This code file looks at the cleaned restaurant review file, not the filtered review file, and extracts the top words that are used in all of the restaurant reviews. There is a list that removes words such as "a", "and", "is", "it", etc. Outputs the top words along with their occurrence rates.

Keyword Occurrences.py
This code file also looks at the cleaned restaurant reviews file and then filters through it using the CommonWordsandPhrases list. While filtering through, it counts how many times each of these keywords show up within all of the restaurant reviews.

Keyword-Rating.py
This code file reads the cleaned restaurant reviews file and again filter through it using the CommonWordsandPhrases list. The code pulls out the keywords and pairs them with the associated ratings that they were found with. Ex. finding the word "loud" in a review and it is paired with a 4 star rating. The code then creates a bunch of histograms for each of these keywords and shows how many times the word appears with various ratings. The final part of the code creates a histogram that combines the top number of keywords. Colors for each keyword ranking can be selected.

Keyword Correlations.py and Keword Correlation Matrix.py
These two files of code are starters for running correlations between the words in the CommonWordsandPhrases list. The correlation matrix code is a work in progress.

Group Correlation.py
This code is a follow up to Keyword Correlations.py and Keyword Correlation Matrix.py. This code opens the filtered restaurant reviews file that has only the rviews that contain one of the keywords from the CommonWordsandPhrases list. This code counts how many times one of these words is used in each review and pairs it with a gmap_id. Pairing it with the gmap_id allows the user to see how many times certain words are used at particular locations.

Combining Group Correlation.py
This code is the follow up to Group Correlation.py. It combines all of the duplicate gmap_ids and sums the occurrences of the keywords. The data is less raw. The code also then creates a correlation matrix to see if any of the keywords from the CommonWordsandPhrases list appear with each other in restaurant reviews.

Sentiment Analysis.py
This code file opens the cleaned restaurant reviews file and uses VADER to analysis the sentiment weighing of each review for every restaurant.

Keyword Sentiment Analysis.py
This code file is the follow up to Sentiment Analysis.py. It still opens the cleaned restaurant reviews and also uses VADER to analyze the sentiment of the reviews, but in this code it weighs the sentiment of the sentences that contain one of the words from the CommonWordsandPhrases list.

Revised Keyword Sentiment.py
This code file takes the output from Keyword Sentiment Analysis.py and cleans it up further by removing unwanted columns and removing any null values in the 'rating' column that might have snuck its way through the other code files.

Merging of Reviews with Text.py
This code is the preliminary step for Sentiment Boxplots.py. In this code file, it merges the two output files from Sentiment Analysis.py and Revised Keyword Sentiment.py and merges the two files together based on the 'text' column, which is the restaurant reviews. By doing this, it creates a new file that has the same restaurant reviews, the same gmap_ids, and the same ratings, but has two different sentiment analysis weighings in one file. One of the sentiment analysis weighings is from the overall review and the other being from just the sentence that contains one of the words from the CommonWordsandPhrases list.

Sentiment Boxplots.py
After running the Merging of Reviews with Text.py code, this code opens the output from it. In this code file, separate boxplots are created for each rating, i.e. a boxplot for 1 star rating, one for 2 star rating, etc. In these plots, the x-axis shows the sentiment weight and the boxplot shows where the most frequent occurrence of the sentiment weights occur.
