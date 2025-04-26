from alpha_vantage.cryptocurrencies import CryptoCurrencies
import os

class AlphaVantageClient:
    def __init__(self):
        self.api_key = os.getenv('ALPHA_VANTAGE_KEY')
    
    def get_price(self, symbol):
        cc = CryptoCurrencies(key=self.api_key)
        data, _ = cc.get_digital_currency_daily(symbol=symbol, market='USD')
        return float(list(data.items())[0][1]['4a. close (USD)'])