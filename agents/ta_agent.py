from alpha_vantage.techindicators import TechIndicators
import os
from datetime import datetime

class TechnicalAnalysisAgent:
    def __init__(self):
        self.api_key = os.getenv('ALPHA_VANTAGE_KEY')
    
    def analyze(self, symbol):
        ti = TechIndicators(key=self.api_key)
        
        # Get indicators
        rsi, _ = ti.get_rsi(symbol=symbol, interval='15min', time_period=14)
        macd, _ = ti.get_macd(symbol=symbol, interval='15min')
        
        # Process data
        latest_rsi = float(list(rsi.items())[0][1]['RSI'])
        latest_macd = float(list(macd.items())[0][1]['MACD'])
        
        return {
            'rsi': latest_rsi,
            'macd': latest_macd,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }