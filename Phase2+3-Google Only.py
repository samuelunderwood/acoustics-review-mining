# ---------------------------------------------------------------
# UCSD Google Local Dataset Cleaning
# ---------------------------------------------------------------

import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

# 'Washington','Texas','New_York','Georgia','Illinois','Tennessee','Nebraska','Iowa','Florida'

state_names = ['New_York']  # Add more state names as needed

for state_name in state_names:
    # Load data for the current state
    googlereviews = pd.read_csv(f'Processed Data/restaurantreviews_{state_name}.csv')
    googlemetadata = pd.read_csv(f'Processed Data/restaurantmetadata_{state_name}.csv')

    # Convert 'time' column from UNIX time (ms) to datetime format
    googlereviews['time'] = pd.to_datetime(googlereviews['time'], unit='ms')

    # Filter out reviews before the year 2007
    googlereviews = googlereviews[googlereviews['time'].dt.year >= 2007]

    # Filter out restaurants with less than ten reviews
    restaurant_counts = googlereviews['gmap_id'].value_counts()
    valid_restaurants = restaurant_counts[restaurant_counts >= 10].index
    df_filtered = googlereviews[googlereviews['gmap_id'].isin(valid_restaurants)]

    # Replace 'â€™' with an apostrophe in the 'text' column
    df_filtered['text'] = df_filtered['text'].str.replace('â€™', "'", regex=False)
    googlemetadata['name'] = googlemetadata['name'].str.replace('â€™', "'", regex=False)
    googlemetadata['address'] = googlemetadata['address'].str.replace('â€™', "'", regex=False)

    # Export to CSV
    df_filtered.to_csv(f'Processed Data/filteredreviews_{state_name}.csv', index=False)
    googlemetadata.to_csv(f'Processed Data/restaurantmetadata_{state_name}.csv', index=False)

# ---------------------------------------------------------------
# UCSD Google Local - Feature Engineering
# ---------------------------------------------------------------

    googlereviews = pd.read_csv(f'Processed Data/filteredreviews_{state_name}.csv')

    noise_keywords = ["loud", "noisy", "noise", "can't hear", "hard to hear", "cannot hear", "deafening", "difficult to hear", "difficult to have a conversation"]
    fault_keywords = ["no background noise","manager","swearing","runny noise","crying out loud", "being loud"]
    quiet_keywords = ["quiet", "peaceful","not too loud", "not too noisy", "not loud", "not noisy"]
    romance_keywords = ["date","romantic","boyfriend","girlfriend","wife","husband","bring your lady","catch-up with a friend", "with a friend"]
    atmosphere_keywords = ["atmosphere", "ambiance"]
    reverb_keywords = ["reverberant","too much echo","echoey","echoes","echoy","high ceiling","echo chamber"]


    # Drop rows with blank values in the "text" column
    googlereviews = googlereviews.dropna(subset=['text'])

    # Create functions to check if a review contains acoustical keywords
    def contains_noise_keyword(text):
        if isinstance(text, str):  # Check if the value is a string
            # Check for noise keywords
            noise_detected = any(keyword in text.lower() for keyword in noise_keywords)
            # Check for fault keywords
            fault_detected = any(keyword in text.lower() for keyword in fault_keywords)
            # Check for quiet keywords
            quiet_detected = any(keyword in text.lower() for keyword in quiet_keywords)
            # If a fault keyword or quiet keyword is detected, return fault_detected
            if fault_detected or quiet_detected:
                return False
            # Otherwise, return whether noise keywords are detected
            return noise_detected
        return False

    def contains_quiet_keyword(text):
        if isinstance(text, str):  # Check if the value is a string
            return any(keyword in text.lower() for keyword in quiet_keywords)
        return False  # Return False for non-string values (NaN)

    def contains_romance_keyword(text):
        if isinstance(text, str):  # Check if the value is a string
            return any(keyword in text.lower() for keyword in romance_keywords)
        return False  # Return False for non-string values (NaN)

    def contains_atmosphere_keyword(text):
        if isinstance(text, str):  # Check if the value is a string
            return any(keyword in text.lower() for keyword in atmosphere_keywords)
        return False  # Return False for non-string values (NaN)

    def contains_reverb_keyword(text):
        if isinstance(text, str):  # Check if the value is a string
            return any(keyword in text.lower() for keyword in reverb_keywords)
        return False  # Return False for non-string values (NaN)

    # Apply functions to create new columns indicating whether each review contains acoustical keywords
    googlereviews['contains_noise'] = googlereviews['text'].apply(contains_noise_keyword)
    googlereviews['contains_quiet'] = googlereviews['text'].apply(contains_quiet_keyword)
    googlereviews['contains_romance'] = googlereviews['text'].apply(contains_romance_keyword)
    googlereviews['contains_atmosphere'] = googlereviews['text'].apply(contains_atmosphere_keyword)
    googlereviews['contains_reverb'] = googlereviews['text'].apply(contains_reverb_keyword)
    googlereviews['review_count'] = googlereviews.groupby('gmap_id')['text'].transform('count')

    googlereviews.to_csv(f'Analysis Data/keywordscoredreviews_{state_name}.csv', index=False)

    # Group by 'gmap_id' and calculate the mean occurrence of noise for each restaurant
    averages = googlereviews.groupby('gmap_id', as_index=False)[['contains_noise', 'contains_quiet','contains_romance','contains_atmosphere','contains_reverb','review_count']].mean()
    #averages.columns = ['gmap_id', 'contains_noise', 'contains_quiet']

    # Save the result to a new CSV file
    averages.to_csv(f'Analysis Data/Google_Averages_{state_name}.csv', index=False)