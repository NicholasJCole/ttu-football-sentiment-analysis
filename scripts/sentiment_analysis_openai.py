import pandas as pd
from openai import OpenAI
import os
import time
import csv

api_key_name = 'OPENAI_API_KEY'
api_key_value = os.getenv(api_key_name)
client = OpenAI()

# Function to perform sentiment analysis using OpenAI API
def analyze_sentiment_openai(text):
    # Ensure that you have set the OPENAI_API_KEY in your environment variables
    # or you can set it here as openai.api_key = 'your-api-key'
    
    response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": f"Your role is to determine the sentiment of posts on a forum dedicated to Texas Tech football.",            
        },
        {
            "role": "user",
            "content": f"Please analyze the sentiment of the following text: \"{text}\"",
        }
    ],
    model="gpt-3.5-turbo",
    )
    
    sentiment = []
    sentiment_response = response.choices[0].message.content
    if "positive" in sentiment_response.lower():
        sentiment = "positive"
    elif "negative" in sentiment_response.lower():
        sentiment = "negative"
    elif "neutral" in sentiment_response.lower():
        sentiment = "neutral"
    elif not sentiment:
        sentiment = "none"
    time.sleep(0.5)
    return sentiment


# # Apply sentiment analysis and save the results in the CSV
# df['Sentiment Score'] = df['post_text_cleaned'].apply(analyze_sentiment_openai)

# # Save the updated CSV
# output_file_path = 'output_data_openai.csv'
# df.to_csv(output_file_path, index=False)

# Load your CSV file
file_path = 'ucf-game-thread-posts_updated.csv'
df = pd.read_csv(file_path)
output_file_path = 'ucf-game-thread-sentiment.csv'

# Open the input CSV file and a new file for output
with open(file_path, mode='r', newline='', encoding='utf-8') as infile, open(output_file_path, mode='w', newline='', encoding='utf-8') as outfile:
    # Create CSV reader and writer
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    # Read the header (first row) from the input file
    headers = next(reader)
    # Add a new column for sentiment in the header
    headers.append('Sentiment')
    writer.writerow(headers)
    # Process each row
    for row in reader:
        # Perform sentiment analysis on the desired column
        # Replace 'column_index' with the index of the column you want to analyze
        sentiment = analyze_sentiment_openai(row[4])
        print("Sentiment is: " + sentiment)
        print(row)
        # Append the sentiment result to the row
        row.append(sentiment)
        # Write the updated row to the output file
        writer.writerow(row)
