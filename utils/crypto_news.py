import requests
from textblob import TextBlob
import os
from datetime import datetime

class CryptoNewsAnalyzer:
    def __init__(self):
        self.api_key = os.getenv('CRYPTO_COMPARE_KEY')
    
    def get_news_sentiment(self, symbol='BTC', limit=3):
        url = f"https://min-api.cryptocompare.com/data/v2/news/?categories={symbol}&limit={limit}"
        response = requests.get(url, headers={'authorization': f'Apikey {self.api_key}'})
        
        if response.status_code != 200:
            return None
            
        articles = response.json().get('Data', [])
        sentiments = []
        
        for article in articles:
            analysis = TextBlob(article['title'])
            sentiments.append(analysis.sentiment.polarity)
        
        avg_sentiment = sum(sentiments)/len(sentiments) if sentiments else 0
        return {
            'average_sentiment': avg_sentiment,
            'articles': articles
        }