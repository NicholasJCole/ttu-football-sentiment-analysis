import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import re
import nltk
from nltk.corpus import stopwords

# Load the CSV file into a DataFrame
csv_file = 'ut-game-thread-sentiment-scores.csv'
df = pd.read_csv(csv_file)

# Concatenate all the text from the "post_text_cleaned" column
all_text = ' '.join(df['post_text_cleaned'].dropna())

# Tokenize the text into words (you may have already done this)
words = re.findall(r'\b\w+\b', all_text.lower())  # Simple word tokenization

# Remove stopwords
filtered_words = [word for word in words if word not in stopwords.words("english")]

# Count the frequency of each word in the filtered text
word_counts = Counter(filtered_words)

# Create a list of (word, frequency) tuples
word_freq_tuples = word_counts.items()

# Sort the list by frequency in descending order
word_freq_tuples = sorted(word_freq_tuples, key=lambda x: x[1], reverse=True)

# Extract the top N words and their frequencies for visualization
top_n = 100
top_words, top_frequencies = zip(*word_freq_tuples[:top_n])

# Create a bar chart to visualize the word frequencies
plt.figure(figsize=(12, 6))
plt.barh(range(len(top_words)), top_frequencies, tick_label=top_words)
plt.gca().invert_yaxis()
plt.xlabel('Frequency')
plt.ylabel('Words')
plt.title('Top {} Words in the Text (Stopwords Removed)'.format(top_n))
plt.tight_layout()
plt.show()
