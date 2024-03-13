import pandas as pd

csv_file_path = 'restaurantreviews_Iowa.csv'  # Replace with the actual path to your CSV file

try:
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file_path)

    # Drop rows with any null or empty values
    df_cleaned = df.dropna()

    # Save the cleaned DataFrame back to a CSV file
    df_cleaned.to_csv('restaurantreviews_Iowa_cleaned.csv', index=False)

    print("Null values removed. Cleaned CSV saved as 'restaurantreviews_Iowa_cleaned.csv'")
except FileNotFoundError:
    print(f"File not found: {csv_file_path}")
except Exception as e:
    print(f"Error processing CSV file: {e}")
