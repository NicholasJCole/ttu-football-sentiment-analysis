import nltk
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from datetime import datetime

# Set the backend to 'tkagg'
plt.switch_backend('tkagg')

# Initialize the VADER sentiment analyzer
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Sample data: List of paragraphs with corresponding timestamps
# Sample data: List of paragraphs with corresponding timestamps
data = [
    {"timestamp": "2023-11-08 10:00:00", "text": "This is a positive sentence."},
    {"timestamp": "2023-11-08 10:15:00", "text": "I'm feeling great today!"},
    {"timestamp": "2023-11-08 10:30:00", "text": "Things are going well."},
    {"timestamp": "2023-11-08 10:45:00", "text": "I'm really sad right now."},
    {"timestamp": "2023-11-08 11:00:00", "text": "The weather is wonderful outside."},
    {"timestamp": "2023-11-08 11:15:00", "text": "I just got a promotion at work."},
    {"timestamp": "2023-11-08 11:30:00", "text": "I love spending time with my family."},
    {"timestamp": "2023-11-08 11:45:00", "text": "Today's news is very disturbing."},
    {"timestamp": "2023-11-08 12:00:00", "text": "I'm excited about my upcoming vacation."},
    {"timestamp": "2023-11-08 12:15:00", "text": "I can't believe I missed my flight."},
    {"timestamp": "2023-11-08 12:30:00", "text": "Spending time in nature makes me happy."},
    {"timestamp": "2023-11-08 12:45:00", "text": "I'm frustrated with the traffic."},
    {"timestamp": "2023-11-08 13:00:00", "text": "I enjoy reading books."},
    {"timestamp": "2023-11-08 13:15:00", "text": "My favorite team won the game."},
    {"timestamp": "2023-11-08 13:30:00", "text": "I received a thoughtful gift."},
    {"timestamp": "2023-11-08 13:45:00", "text": "I'm worried about my upcoming exam."},
    {"timestamp": "2023-11-08 14:00:00", "text": "Listening to music relaxes me."},
    {"timestamp": "2023-11-08 14:15:00", "text": "I'm looking forward to the weekend."},
    {"timestamp": "2023-11-08 14:30:00", "text": "I had a great meal at the new restaurant."},
    {"timestamp": "2023-11-08 14:45:00", "text": "I'm upset about the recent changes at work."},
    {"timestamp": "2023-11-08 15:00:00", "text": "I love spending time with my pets."},
    {"timestamp": "2023-11-08 15:15:00", "text": "I'm disappointed with the service."},
    {"timestamp": "2023-11-08 15:30:00", "text": "I'm grateful for the support of my friends."},
    {"timestamp": "2023-11-08 15:45:00", "text": "I'm anxious about the upcoming presentation."},
    {"timestamp": "2023-11-08 16:00:00", "text": "I had a great workout at the gym."},
    {"timestamp": "2023-11-08 16:15:00", "text": "I'm annoyed by the constant noise."},
    {"timestamp": "2023-11-08 16:30:00", "text": "I'm thrilled about the new project."},
    {"timestamp": "2023-11-08 16:45:00", "text": "I'm sad that I couldn't attend the party."},
    {"timestamp": "2023-11-08 17:00:00", "text": "I'm feeling inspired by the art exhibition."},
    {"timestamp": "2023-11-08 17:15:00", "text": "I'm irritated by the delays."},
    {"timestamp": "2023-11-08 17:30:00", "text": "I'm proud of my achievements."},
]


# Initialize lists to store sentiment scores and timestamps
sentiment_scores = []
timestamps = []
trailing_averages = []

# Helper function to calculate trailing average
def calculate_trailing_average(scores, window_size):
    if len(scores) < window_size:
        return None
    else:
        return sum(scores[-window_size:]) / window_size

# Process data
for entry in data:
    text = entry["text"]
    timestamp = entry["timestamp"]
    sentiment_score = sia.polarity_scores(text)["compound"]
    
    sentiment_scores.append(sentiment_score)
    timestamps.append(datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"))
    
    # Calculate trailing average of the last 5 scores
    trailing_average = calculate_trailing_average(sentiment_scores, 5)
    trailing_averages.append(trailing_average)

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(timestamps, trailing_averages, marker='o', linestyle='-', label='Trailing Avg (5)', color='b')
plt.fill_between(timestamps, trailing_averages, color='b', alpha=0.2)
plt.xlabel('Time', fontsize=14)
plt.ylabel('Sentiment Score', fontsize=14)
plt.title('Sentiment Analysis Over Time with Trailing Average', fontsize=16)
plt.xticks(rotation=45)
plt.ylim(-1, 1)  # Set the Y-axis range to [-1, 1]
plt.grid(False)  # Remove grid lines
plt.legend(fontsize=12)
plt.tight_layout()

# Add a background color for better contrast
ax = plt.gca()
ax.set_facecolor('#f7f7f7')

# Show the plot
plt.show()
