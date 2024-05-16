import csv
from collections import Counter
import re
from nltk.corpus import stopwords

# Download NLTK stopwords if not already downloaded
import nltk
nltk.download('stopwords')

csv_file_path = 'restaurantreviews_Iowa_cleaned.csv'  # Replace with the actual path to your CSV file
output_csv_path = 'Top_100_Words_from_Iowa.csv'  # New CSV file for top words

def extract_top_words(csv_file, column_index, top_n=100):
    # Read CSV file and extract text from the specified column
    texts = []
    try:
        with open(csv_file, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)

            # Assuming column D corresponds to index 3 (0-based indexing)
            for row in csv_reader:
                if len(row) > column_index:
                    text = row[column_index]
                    texts.append(text)
    except FileNotFoundError:
        print(f"File not found: {csv_file}")
        return []
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []

    # Concatenate all text into a single string
    all_text = ' '.join(texts)

    # Tokenize the text and count occurrences, excluding stop words
    stop_words = set(stopwords.words('english'))
    words = re.findall(r'\b\w+\b', all_text.lower())
    filtered_words = [wd for wd in words if wd not in stop_words]
    word_count = Counter(filtered_words)

    # Get the top N words and their occurrences
    words_top = word_count.most_common(top_n)

    return words_top

def write_to_csv(output_csv, top_wd):
    try:
        with open(output_csv, 'w', newline='', encoding='utf-8') as output_file:
            csv_writer = csv.writer(output_file)
            csv_writer.writerow(['Word', 'Occurrences'])
            csv_writer.writerows(top_wd)
        print(f'Top words written to {output_csv}')
    except Exception as e:
        print(f"Error writing to CSV file: {e}")

# Example usage
column_d_index = 3  # Adjust based on the actual index of column D (0-based indexing)
top_words = extract_top_words(csv_file_path, column_d_index)

# Display the top words and their occurrences
for word, count in top_words:
    print(f'{word}: {count} occurrences')

# Write top words to a new CSV file
write_to_csv(output_csv_path, top_words)
