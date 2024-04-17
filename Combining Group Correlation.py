import pandas as pd

def combine_duplicates(input_csv, output_csv):
    # Read the input CSV file
    df = pd.read_csv(input_csv)

    # Convert the columns from 'B' to 'BD' to numeric
    df.iloc[:, 1:] = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')

    # Combine duplicate values in the 'gmap_id' column and sum values in columns B through BD
    df_combined = df.groupby('gmap_id').sum().reset_index()

    # Save the combined DataFrame to a new CSV file
    df_combined.to_csv(output_csv, index=False)

    print(f"Combined and summed CSV file '{output_csv}' created.")

# Example usage
input_file = 'new_filtered_reviews.csv'
output_file = 'combined_and_summed_filtered_reviews.csv'

combine_duplicates(input_file, output_file)
