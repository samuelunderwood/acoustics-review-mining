## Acoustics Review Mining
This repository is used to share code for the ongoing research for the UNL Quiet Bites project, led by Sam Underwood and Dr. Lily Wang, and its associated collaborations.

### How are things organized?
#### Phase1Filtering.py 
This code is used to read and clean the raw JSON files from the UCSD Google Local Dataset. The original dataset contains reviews across all businesses, but we are currently
only interested in restaurants. This code removes identifiable names of users, and filters the dataset according to the business category from the associated metadata JSON file. 
This code can run on data for one or multiple U.S. states, just adjust the us_states list as needed

#### Clustering.ipynb
This notebook is used to perform k-means text clustering analysis on a cleaned CSV file containing user reviews. It can analyze a sub-sample of reviews to reduce computational time.

#### Cleaning Code.py
This code file further cleans the restaurant reviews by removing all null values in the "reviews" column such as emojis, empty cells, and characters that Python cannot read. 

#### Filtered Reviews.py
This code file opens the cleaned dataset and uses the CommonWordsandPhrases list as a filter. It will return every restaurant review that uses one of the words in the list of CommonWordsandPhrases. 
