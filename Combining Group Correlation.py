import pandas as pd

def combine_and_correlate(input_csv, output_csv):
    # Read the input CSV file
    df = pd.read_csv(input_csv)

    # Convert the columns from 'B' to 'BD' to numeric
    df.iloc[:, 1:] = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')

    # Combine duplicate values in the 'gmap_id' column
    df_combined = df.groupby('gmap_id').sum().reset_index()

    # Calculate the correlation between columns B through BD
    correlation_matrix = df_combined.iloc[:, 1:].corr()

    # Save the combined DataFrame and correlation matrix to a new CSV file
    with pd.ExcelWriter(output_csv) as writer:
        df_combined.to_excel(writer, index=False, sheet_name='Combined Data')
        correlation_matrix.to_excel(writer, sheet_name='Correlation Matrix')

    print(f"Combined and correlated data saved to '{output_csv}'.")

# Example usage
input_file = 'new_filtered_reviews.csv'
output_file = 'combined_and_correlated_filtered_reviews.xlsx'

combine_and_correlate(input_file, output_file)
