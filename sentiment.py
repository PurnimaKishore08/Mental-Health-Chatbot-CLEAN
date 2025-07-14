from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)

    compound = score['compound']
    if compound >= 0.3:
        return "Positive"
    elif compound <= -0.3:
        return "Negative"
    else:
        return "Neutral"