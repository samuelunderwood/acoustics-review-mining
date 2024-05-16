# ---------------------------------------------------------------
# Phase1Filtering.py
# ---------------------------------------------------------------
#
# Required Input Files:
# 'categories_to_include.csv' || User-specified list of business category strings to include
# 'categories_to_exclude.csv' || User-specified list of business category strings to exclude
#
# This code is used to read and filter the raw JSON files downloaded from the UCSD Google Local Dataset:
# https://datarepo.eng.ucsd.edu/mcauley_group/gdrive/googlelocal/
#
# The original dataset contains reviews across all businesses, but we are currently only interested in restaurants.
# This code removes potentially identifiable names of users, and filters the dataset according to the business
# category from the associated metadata JSON file. This code can run on data for one or multiple U.S. states,
# just adjust the us_states list as needed.
#

import pandas as pd

# List US States to process from UCSD Dataset
us_states = ['Washington']

# Read the CSV file with terms to include and exclude
categories_to_include = pd.read_csv('categories_to_include.csv')['term'].tolist()
categories_to_exclude = pd.read_csv('categories_to_exclude.csv')['term'].tolist()

# Define chunk size
chunk_size = 50000

for state in us_states:
    # Initialize an empty DataFrame to hold the concatenated chunk results
    df = pd.DataFrame()

    # Read review JSON file in chunks
    with open(f'Raw Data/review-{state}.json', 'r') as file:
        reader = pd.read_json(file, lines=True, chunksize=chunk_size)
        for chunk in reader:
            # Remove identifiable names | axis 1 removes by column
            chunk = chunk.drop('name', axis=1)
            df = pd.concat([df, chunk], ignore_index=True)

    # Initialize an empty DataFrame to hold the concatenated chunk results
    metadata = pd.DataFrame()

    # Read metadata JSON file in chunks
    with open(f'Raw Data/meta-{state}.json', 'r') as file:
        reader = pd.read_json(file, lines=True, chunksize=chunk_size)
        for chunk in reader:
            # Flatten the lists in the "category" column and convert them to lowercase
            chunk['category'] = chunk['category'].apply(
                lambda x: [item.lower() for item in x] if isinstance(x, list) else [])
            metadata = pd.concat([metadata, chunk], ignore_index=True)

    # Filter the metadata DataFrame to create a list of business IDs with terms in the category
    restaurant_ids = metadata[metadata['category'].apply(
        lambda x: any(term in x for term in categories_to_include) and not any(
            term in x for term in categories_to_exclude))]['gmap_id'].tolist()

    # Filter the review dataframe to include only business IDs that appear in the list of restaurant IDs
    restaurantreviews = df[df['gmap_id'].isin(restaurant_ids)]

    # Filter the metadata dataframe to include only businesses that appear in the list of restaurant IDs
    restaurantmetadata = metadata[metadata['gmap_id'].isin(restaurant_ids)]

    # Save the filtered restaurant reviews and metadata to a CSV file
    restaurantreviews.to_csv(f'Processed Data/restaurantreviews_{state}.csv', index=False)
    restaurantmetadata.to_csv(f'Processed Data/restaurantmetadata_{state}.csv', index=False)

