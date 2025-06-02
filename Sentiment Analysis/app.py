from textblob import TextBlob

def analyze_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)

    # Perform sentiment analysis
    sentiment_score = blob.sentiment.polarity

    # Classify sentiment
    if sentiment_score > 0:
        sentiment = "positive"
    elif sentiment_score < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return sentiment, sentiment_score

# Example sentences for sentiment analysis
sentences = [
    "I love this product, it's amazing!",
    "The service was terrible, I'll never go back again.",
    "Today is a beautiful day.",
    "I feel indifferent about the movie.",
    "The food at the restaurant was decent."
]

# Analyze sentiment for each sentence
for sentence in sentences:
    sentiment, score = analyze_sentiment(sentence)
    print(f"Sentence: {sentence}")
    print(f"Sentiment: {sentiment.capitalize()} (Score: {score})")
    print()
