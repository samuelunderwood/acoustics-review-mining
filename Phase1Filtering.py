import pandas as pd

# List of US states
us_states = ['Texas']  # Add more states as needed

# Read the CSV file with terms to include and exclude
categories_to_include = pd.read_csv('categories_to_include.csv')['term'].tolist()
categories_to_exclude = pd.read_csv('categories_to_exclude.csv')['term'].tolist()

for state in us_states:
    # Convert json to dataframe
    df = pd.read_json(f'Raw Data/review-{state}.json', lines=True)

    # Remove identifiable names | axis 1 removes by column
    df = df.drop('name', axis=1)

    # Convert json to dataframe
    metadata = pd.read_json(f'Raw Data/meta-{state}.json', lines=True)

    # Flatten the lists in the "category" column and convert them to lowercase
    metadata['category'] = metadata['category'].apply(lambda x: [item.lower() for item in x] if isinstance(x, list) else [])

    # Filter the metadata DataFrame to create a list of business IDs with terms in the category
    restaurant_ids = metadata[metadata['category'].apply(lambda x: any(term in x for term in categories_to_include) and not any(term in x for term in categories_to_exclude))]['gmap_id'].tolist()

    # Filter the review dataframe to include only business IDs that appear in the list of restaurant IDs
    restaurantreviews = df[df['gmap_id'].isin(restaurant_ids)]

    # Filter the metadata dataframe to include only businesses that appear in the list of restaurant IDs
    restaurantmetadata = metadata[metadata['gmap_id'].isin(restaurant_ids)]

    # Save the filtered restaurant reviews and metadata to a CSV file
    restaurantreviews.to_csv(f'Processed Data/restaurantreviews_{state}.csv', index=False)
    restaurantmetadata.to_csv(f'Processed Data/restaurantmetadata_{state}.csv', index=False)
